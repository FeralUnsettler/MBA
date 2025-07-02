import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Título e descrição\st.set_page_config(page_title="Dashboard Saúde Corporativa", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #F5F9FF;
        }
        h1, h2, h3, h4 {
            color: #003366;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard de Saúde Corporativa com BI e IA")
st.markdown("Monitoramento de bem-estar, burnout e ações preventivas nas empresas")

# Simulação de dados reais
np.random.seed(42)
data = pd.DataFrame({
    'Data': pd.date_range(datetime.today() - timedelta(days=180), periods=180),
    'Departamento': np.random.choice(['Financeiro', 'RH', 'TI', 'Vendas', 'Marketing'], 180),
    'Ausências': np.random.poisson(lam=2, size=180),
    'Horas Extras': np.random.randint(0, 10, 180),
    'Feedback Negativo': np.random.randint(0, 5, 180),
    'Burnout Detectado': np.random.choice([0, 1], size=180, p=[0.85, 0.15])
})

# Filtros
with st.sidebar:
    st.header("Filtros")
    dep_filter = st.multiselect("Departamentos", data['Departamento'].unique(), default=data['Departamento'].unique())
    date_range = st.date_input("Período", [data['Data'].min(), data['Data'].max()])

# Aplicação dos filtros
filtered = data[(data['Departamento'].isin(dep_filter)) &
                (data['Data'] >= pd.to_datetime(date_range[0])) &
                (data['Data'] <= pd.to_datetime(date_range[1]))]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Total de Ausências", int(filtered['Ausências'].sum()))
col2.metric("🧠 Casos de Burnout", int(filtered['Burnout Detectado'].sum()))
col3.metric("⏱ Média de Horas Extras", round(filtered['Horas Extras'].mean(), 1))
col4.metric("📉 Feedbacks Negativos", int(filtered['Feedback Negativo'].sum()))

# Gráficos
st.subheader("📌 Tendência de Ausências e Burnout")
timeseries = filtered.groupby('Data').agg({'Ausências': 'sum', 'Burnout Detectado': 'sum'}).reset_index()
fig1 = px.line(timeseries, x='Data', y=['Ausências', 'Burnout Detectado'],
               labels={'value': 'Total', 'variable': 'Indicador'},
               title="Evolução Diária")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📊 Comparativo por Departamento")
grp = filtered.groupby('Departamento').agg({
    'Ausências': 'sum',
    'Burnout Detectado': 'sum',
    'Horas Extras': 'mean',
    'Feedback Negativo': 'sum'
}).reset_index()

col1, col2 = st.columns(2)
fig2 = px.bar(grp, x='Departamento', y='Ausências', color='Departamento', title="Total de Ausências")
col1.plotly_chart(fig2, use_container_width=True)
fig3 = px.pie(grp, names='Departamento', values='Burnout Detectado', title="Distribuição de Burnouts")
col2.plotly_chart(fig3, use_container_width=True)

# Correlações
st.subheader("🧩 Correlação entre Indicadores")
corr = filtered[['Ausências', 'Horas Extras', 'Feedback Negativo', 'Burnout Detectado']].corr()
st.dataframe(corr.style.background_gradient(cmap='Blues'), use_container_width=True)

# Conclusões automáticas
st.markdown("""
### 🤖 Insights Automáticos com IA Simulada
- Departamentos com maior incidência de burnout também registram mais horas extras.
- Feedbacks negativos têm correlação moderada com burnout detectado.
- O uso de BI poderia prever com 3 dias de antecedência os picos de burnout com base nos padrões históricos.
""")
