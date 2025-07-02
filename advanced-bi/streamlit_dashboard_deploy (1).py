# Estrutura completa de deploy para Streamlit Cloud ou GitHub Pages (Streamlit)

# 1. dashboard.py (o código principal do dashboard)
# Já foi gerado no arquivo "dashboard_saude_mental.py" (nome sugerido para salvar)

# 2. requirements.txt
# Lista de dependências para Streamlit Cloud e GitHub
requirements = """
streamlit
pandas
plotly
numpy
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

# 3. .streamlit/config.toml (ajustes visuais e técnicos)
import os
os.makedirs(".streamlit", exist_ok=True)
config = """
[theme]
primaryColor="#003366"
backgroundColor="#F5F9FF"
secondaryBackgroundColor="#FFFFFF"
textColor="#000000"
font="sans serif"

[server]
headless = true
enableCORS=false
port = 8501
"""

with open(".streamlit/config.toml", "w") as f:
    f.write(config)

# 4. README.md
readme = """
# 📊 Dashboard de Saúde Corporativa com BI e IA

Este projeto foi desenvolvido em Streamlit com foco em análise de saúde mental e bem-estar no ambiente corporativo, utilizando indicadores como burnout, absenteísmo, horas extras e feedbacks negativos.

## 🔧 Tecnologias utilizadas
- Streamlit
- Pandas
- Plotly
- Numpy

## 🚀 Como rodar localmente
```bash
pip install -r requirements.txt
streamlit run dashboard_saude_mental.py
```

## ☁️ Deploy no Streamlit Cloud
1. Suba este repositório para o GitHub
2. Vá para https://streamlit.io/cloud e conecte sua conta
3. Selecione o repositório e o arquivo `dashboard_saude_mental.py`
4. Clique em Deploy

Pronto! Seu dashboard estará online 🎉
"""

with open("README.md", "w") as f:
    f.write(readme)

print("✅ Estrutura de deploy criada: requirements.txt, .streamlit/config.toml e README.md")
