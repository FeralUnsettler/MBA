```bash
#!/bin/bash

mkdir -p estaciona-plus/app
cd estaciona-plus || exit

# Criar app/dashboard.py
cat <<EOF > app/dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("🚗 Estaciona+ | Dashboard BI")

def gerar_dados_ocupacao():
    bairros = ['Centro', 'Moinhos', 'Cidade Baixa', 'Menino Deus', 'Bom Fim']
    registros = []
    start = datetime.now() - timedelta(days=7)
    for i in range(1000):
        bairro = np.random.choice(bairros)
        data_hora = start + timedelta(minutes=10*i)
        total_vagas = 100
        ocupadas = np.clip(int(50 + 30 * np.sin(i/50) + np.random.normal(0,5)), 0, total_vagas)
        registros.append([bairro, data_hora, total_vagas, ocupadas])
    df = pd.DataFrame(registros, columns=['bairro', 'data_hora', 'total_vagas', 'ocupadas'])
    df['livres'] = df['total_vagas'] - df['ocupadas']
    return df

df_ocupacao = gerar_dados_ocupacao()

st.markdown("### KPIs Gerais")
col1, col2, col3 = st.columns(3)
col1.metric("Média de Vagas Ocupadas", f"{int(df_ocupacao['ocupadas'].mean())}")
col2.metric("Média de Vagas Livres", f"{int(df_ocupacao['livres'].mean())}")
col3.metric("Tempo Médio de Busca de Vaga", "4.2 min")

st.markdown("### Status das Fontes de Dados")
status_data = {
    'EPTC': 'Online',
    'Zona Azul': 'Online',
    'Siga Pay': 'Offline - Latência Alta'
}
for fonte, status in status_data.items():
    color = "green" if "Online" in status else "red"
    st.markdown(f"- **{fonte}**: <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)

bairros = st.multiselect("Selecione bairros para análise", options=df_ocupacao['bairro'].unique(), default=df_ocupacao['bairro'].unique())
df_filtrado = df_ocupacao[df_ocupacao['bairro'].isin(bairros)]

st.markdown("### Ocupação de Vagas por Bairro")
line_chart = alt.Chart(df_filtrado).mark_line().encode(
    x='data_hora:T',
    y='ocupadas:Q',
    color='bairro:N',
    tooltip=['bairro', 'data_hora', 'ocupadas']
).properties(height=400, width=900)
st.altair_chart(line_chart, use_container_width=True)

st.markdown("### Alertas")
st.info("🟢 EPTC está operando normalmente.")
st.info("🟢 Zona Azul está operando normalmente.")
st.error("🔴 Siga Pay com latência alta, possível atraso na atualização de dados.")

st.markdown("### Resultado Simulado A/B Test - Notificações Push")
ab_data = pd.DataFrame({
    'Grupo': ['Controle', 'Teste'],
    'Taxa de Adoção': [0.34, 0.47],
    'Tempo Médio Sessão (min)': [5.1, 6.4]
})
st.table(ab_data)

st.markdown("---")
st.markdown("**Dashboard inicial do Estaciona+ alinhado com framework de BI e APS proposto.**")
EOF

# Criar requirements.txt
cat <<EOF > requirements.txt
streamlit
pandas
numpy
altair
EOF

# Criar Dockerfile
cat <<EOF > Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./app ./app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
EOF

# Criar README.md
cat <<EOF > README.md
# Estaciona+ Dashboard BI

Dashboard interativo para monitoramento do Estaciona+, plataforma para otimização de vagas de estacionamento.

## Como rodar localmente

### Pré-requisitos

- Python 3.8+
- pip

### Passos

\`\`\`bash
git clone <repo-url>
cd estaciona-plus
pip install -r requirements.txt
streamlit run app/dashboard.py
\`\`\`

Acesse o dashboard em: http://localhost:8501

---

## Rodando com Docker

\`\`\`bash
docker build -t estaciona-plus .
docker run -p 8501:8501 estaciona-plus
\`\`\`

Acesse o dashboard em http://localhost:8501

---

## Funcionalidades

- KPIs de ocupação
- Monitoramento status das fontes de dados
- Gráficos de ocupação histórica por bairro
- Alertas simulados
- Resultados de A/B test simulados
EOF

echo "Setup concluído! Para iniciar o projeto, execute:"
echo "cd estaciona-plus && streamlit run app/dashboard.py"
```