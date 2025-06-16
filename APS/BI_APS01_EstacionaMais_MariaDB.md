# Painel Streamlit adaptado para se conectar ao MariaDB na Hostinger** e exibir os dados da tabela `fato_zona_azul`.

---

## ✅ 1\. Instale as dependências

No seu ambiente local ou virtualenv:

pip install streamlit mysql-connector-python pandas

---

## ✅ 2\. Estrutura do painel Streamlit

### `painel_zona_azul.py`

import streamlit as st

import pandas as pd

import mysql.connector

from datetime import datetime

\# \--- Configurações do layout \---

st.set\_page\_config(layout="wide")

st.title("🚗 Estaciona+ | Dashboard Zona Azul (Hostinger \+ MariaDB)")

\# \--- Conexão com o banco MariaDB (Hostinger) \---

def conectar\_banco():

    return mysql.connector.connect(

        host="seu\_host",        \# Ex: "srv123.main-hosting.eu" ou "localhost"

        user="seu\_usuario",     \# Ex: "u123456789\_luciano"

        password="sua\_senha",

        database="seu\_banco"    \# Ex: "u123456789\_estaciona"

    )

\# \--- Carrega dados da tabela \---

@st.cache\_data(ttl=600)

def carregar\_dados():

    conexao \= conectar\_banco()

    query \= "SELECT \* FROM fato\_zona\_azul ORDER BY data\_hora DESC"

    df \= pd.read\_sql(query, conexao)

    conexao.close()

    return df

df \= carregar\_dados()

\# \--- Exibição dos dados e métricas \---

st.subheader("🔍 Resumo das últimas 24h")

col1, col2, col3 \= st.columns(3)

col1.metric("Ocupação Média (%)", f"{(df\['ocupadas'\].sum() / df\['total\_vagas'\].sum() \* 100):.1f}%")

col2.metric("Receita Total", f"R$ {df\['receita'\].sum():,.2f}")

col3.metric("Tarifa Média", f"R$ {df\['tarifa\_media'\].mean():.2f}")

\# \--- Filtros por bairro \---

bairros \= st.multiselect("Filtrar por bairro:", df\['bairro'\].unique(), default=df\['bairro'\].unique())

df\_filtrado \= df\[df\['bairro'\].isin(bairros)\]

\# \--- Gráfico interativo (linha do tempo de ocupação) \---

import altair as alt

grafico \= alt.Chart(df\_filtrado).mark\_line(point=True).encode(

    x='data\_hora:T',

    y='ocupadas:Q',

    color='bairro:N',

    tooltip=\['bairro', 'data\_hora', 'ocupadas', 'livres', 'receita'\]

).properties(

    title="📈 Ocupação ao longo do tempo",

    width=800,

    height=400

)

st.altair\_chart(grafico, use\_container\_width=True)

\# \--- Tabela com os dados completos \---

st.markdown("\#\#\# 🧾 Tabela completa")

st.dataframe(df\_filtrado)

\# \--- Rodapé \---

st.markdown("---")

st.caption("Painel gerado com Streamlit • Dados sintéticos da Zona Azul • Desenvolvido por Luciano")

---

## ✅ 3\. Como rodar localmente

No terminal, execute:

streamlit run painel\_zona\_azul.py

---

## ✅ 4\. Como rodar no servidor (opcional)

Se quiser hospedar isso em um servidor com suporte a Python, recomendo:

* VPS com suporte a Streamlit \+ Python  
* Ou rodar local e compartilhar via [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## ✅ 5\. Dica extra: `.streamlit/secrets.toml` (alternativo para ocultar credenciais)

\[mariadb\]

host \= "seu\_host"

user \= "seu\_usuario"

password \= "sua\_senha"

database \= "seu\_banco"

No código:

import streamlit as st

import mysql.connector

def conectar\_banco():

    cred \= st.secrets\["mariadb"\]

    return mysql.connector.connect(

        host=cred\["host"\],

        user=cred\["user"\],

        password=cred\["password"\],

        database=cred\["database"\]

    )

---
