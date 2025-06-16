
#!/bin/bash
echo "Criando estrutura de diretórios..."
mkdir -p estaciona_plus_viz/app
mkdir -p estaciona_plus_viz/data

echo "Gerando arquivos..."
echo 'import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

st.set_page_config(layout=\"wide\")
st.title(\"🚗 Estaciona+ | Zona Azul — Dashboard BI\")

@st.cache_data(ttl=600)
def gerar_dados_sinteticos():
    bairros = {
        'Centro': 1200,
        'Cidade Baixa': 900,
        'Bom Fim': 800,
        'Moinhos': 1000,
        'Menino Deus': 600,
        'Outros': 2493
    }
    registros = []
    inicio = datetime.now() - timedelta(hours=2)
    for bairro, total in bairros.items():
        for i in range(12):  # intervalos de 10min
            data_hora = inicio + timedelta(minutes=i*10)
            ocupadas = int(total * 0.75 + (i % 5) * 10)
            livres = total - ocupadas
            receita = ocupadas * 4.0
            registros.append([bairro, data_hora, total, ocupadas, livres, receita, 4.00])
    return pd.DataFrame(registros, columns=[\"bairro\", \"data_hora\", \"total_vagas\", \"ocupadas\", \"livres\", \"receita\", \"tarifa_media\"])

df = gerar_dados_sinteticos()

st.markdown(\"### KPIs Gerais\")
col1, col2, col3 = st.columns(3)
col1.metric(\"Ocupação Média (%)\", f\"{(df['ocupadas'].sum()/df['total_vagas'].sum()*100):.1f}%\")
col2.metric(\"Receita Total\", f\"R$ {df['receita'].sum():,.2f}\")
col3.metric(\"Tarifa Média\", f\"R$ {df['tarifa_media'].mean():.2f}\")

bairros = st.multiselect(\"Bairros\", df['bairro'].unique(), default=df['bairro'].unique())
df_f = df[df['bairro'].isin(bairros)]

st.markdown(\"### Ocupação por Bairro\")
chart = alt.Chart(df_f).mark_line().encode(
    x='data_hora:T',
    y='ocupadas:Q',
    color='bairro:N',
    tooltip=['bairro', 'data_hora', 'ocupadas', 'receita']
).properties(height=400)
st.altair_chart(chart, use_container_width=True)' > estaciona_plus_viz/app/dashboard.py
echo 'streamlit>=1.24.0
pandas
altair' > estaciona_plus_viz/requirements.txt
echo '# Estaciona+ DataViz & Storytelling

Dashboard interativo para visualização de KPIs da Zona Azul de Porto Alegre, integrado ao projeto de BI e DW.

## Componentes:
- KPIs (Ocupadas, Livres, Receita)
- Heatmaps
- Filtros por bairro

## Tecnologias:
- Python 3.10+
- Streamlit
- Altair

## Rodar localmente:
```bash
pip install -r requirements.txt
streamlit run app/dashboard.py
```

## Estrutura
- `app/dashboard.py`: visualização principal
- `data/`: amostras sintéticas
- `README.md`: este arquivo

## Licença
MIT License' > estaciona_plus_viz/README.md

echo "Pronto. Para executar:"
echo "cd estaciona_plus_viz && pip install -r requirements.txt && streamlit run app/dashboard.py"
