import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(page_title="Dashboard de Preferência Cerebral", layout="wide")

# --- Dados Extraídos ---
NOME_PARTICIPANTE = "Luciano Martins Fagundes"
CONTEXTO = "Teste Preferência Cerebral Comportamental - 2ª Turma MBAs UniSenac - abril/2025"

# Dados Quantitativos
profile_data = {
    'Perfil': ['Lobo', 'Golfinho', 'Águia', 'Tubarão'],
    'Percentual': [40, 28, 20, 12],
    'Categoria': ['Razão', 'Emoção', 'Emoção', 'Razão'] # Adicionando categoria para possível uso futuro
}
df_profiles = pd.DataFrame(profile_data)

category_data = {
    'Categoria': ['Razão', 'Emoção'],
    'Percentual': [52, 48]
}
df_categories = pd.DataFrame(category_data)

# Dados Qualitativos (Resumidos)
qualitative_data = {
    "Lobo (40% - Razão)": {
        "Características": "Detalhista, organizado, metódico, pontual, busca conhecimento, conservador.",
        "Pontos Fortes": "Consistência, Qualidade, Organização, Segurança, Responsabilidade.",
        "Pontos de Melhoria": "Dificuldade de adaptação a mudanças, perfeccionismo pode impedir progresso.",
        "Motivações": "Certeza, compreensão exata, análise de riscos, busca por acerto.",
        "Valores": "Ordem e controle."
    },
    "Golfinho (28% - Emoção)": {
        "Características": "Sensível, relacional, focado em equipe, tradicionalista, colaborativo.",
        "Pontos Fortes": "Comunicação interpessoal, Motivação da equipe, Conciliação de conflitos.",
        "Pontos de Melhoria": "Esconder conflitos, dificuldade com pressão, manipulação por sentimentos.",
        "Motivações": "Segurança, aceitação social, consenso, reconhecimento da equipe.",
        "Valores": "Ambiente harmônico, trabalho em equipe."
    },
    "Águia (20% - Emoção)": {
        "Características": "Criativo, intuitivo, holístico, foco no futuro, flexível, informal.",
        "Pontos Fortes": "Antecipar o futuro, Criatividade.",
        "Pontos de Melhoria": "Falta de atenção ao presente, impaciência, teimosia ao defender ideias.",
        "Motivações": "Liberdade de expressão, ausência de controles rígidos, ambiente criativo, delegar detalhes.",
        "Valores": "Criatividade e Liberdade."
    },
    "Tubarão (12% - Razão)": {
        "Características": "Rápido, senso de urgência, ação/iniciativa, impulsivo, focado em desafios, autossuficiente.",
        "Pontos Fortes": "Foco em resultados, Motivação, Superar burocracia.",
        "Pontos de Melhoria": "Socialmente complicado, impaciente, relacionamento difícil.",
        "Motivações": "Liberdade para agir, desafios, competição, variedade, evitar repetição.",
        "Valores": "Resultados."
    }
}


# --- Layout do Dashboard ---
st.title("Dashboard de Preferência Cerebral")
st.subheader(f"Resultados de: {NOME_PARTICIPANTE}")
st.caption(CONTEXTO)

st.markdown("---")

# --- Gráficos Analíticos ---
st.header("Análise Gráfica dos Resultados")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição dos Perfis (%)")
    # Gráfico de Pizza para Perfis
    fig_pie = px.pie(df_profiles,
                     values='Percentual',
                     names='Perfil',
                     title='Distribuição Percentual por Perfil Comportamental',
                     color='Perfil', # Opcional: colorir por perfil
                     color_discrete_map={'Lobo':'#1f77b4', # Azul
                                         'Golfinho':'#2ca02c', # Verde
                                         'Águia':'#ff7f0e', # Laranja
                                         'Tubarão':'#d62728'} # Vermelho
                     )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Equilíbrio Razão vs. Emoção (%)")
    # Gráfico de Barras para Categorias
    fig_bar = px.bar(df_categories,
                     x='Categoria',
                     y='Percentual',
                     title='Equilíbrio entre Razão e Emoção',
                     text='Percentual', # Mostra o valor na barra
                     color='Categoria',
                     color_discrete_map={'Razão':'#1f77b4', 'Emoção':'#2ca02c'})
    fig_bar.update_traces(texttemplate='%{text}%', textposition='outside') # Formata o texto
    fig_bar.update_layout(yaxis_title="Percentual (%)", xaxis_title="Categoria Principal")
    st.plotly_chart(fig_bar, use_container_width=True)


st.markdown("---")

# --- Detalhes dos Perfis (Qualitativo) ---
st.header("Características Detalhadas dos Perfis")

for perfil, detalhes in qualitative_data.items():
    with st.expander(f"**{perfil}**"):
        for chave, valor in detalhes.items():
            st.markdown(f"**{chave}:** {valor}")

st.markdown("---")
st.caption("Dashboard gerado com base nos dados do teste de preferência cerebral.")