# APS Visualização de Dados e Data Storytelling

## Etapa 5 – Plano de Análise e Visualização

---

### 📂 Contexto do Projeto

O projeto **Estaciona+** é uma solução SaaS para otimização de vagas de estacionamento rotativo em Porto Alegre, baseada em dados da EPTC, Zona Azul e Siga Pay. O objetivo da visualização é fornecer uma interface clara para apoio à tomada de decisão nos níveis estratégico, tático e operacional do projeto, utilizando dados reais e sintéticos extraídos e tratados conforme o framework BI definido na APS.

Os dados são baseados no documento “MBA BI APS 01 Estaciona+ Framework\_v3”.

---

## 🔹 1. Objetivos do Plano

- Planejar análises para apoio à decisão com base em dados da Zona Azul e da simulação de ocupação.
- Definir visualizações integradas no Streamlit para facilitar o entendimento dos dados.
- Documentar as ferramentas utilizadas para reuso e reproducibilidade.

---

## 📊 2. Lista de Análises Previstas

| Categoria   | Análise                                         | Objetivo                             | Ferramenta              |
| ----------- | ----------------------------------------------- | ------------------------------------ | ----------------------- |
| Estratégica | Ocupação de vagas por bairro (EPTC + Zona Azul) | Avaliar desempenho e uso do serviço  | Streamlit + Altair      |
| Estratégica | Receita gerada por região / tarifa média        | Estimar rentabilidade e precificação | Power BI / Excel        |
| Tática      | Comparativo planejado x realizado               | Acompanhar avanço dos OKRs e metas   | Power BI                |
| Tática      | Progresso de tarefas (Kanban + Burndown)        | Visualizar andamento do projeto      | Miro / Trello / Jira    |
| Operacional | Alertas de prazos críticos                      | Reduzir atrasos e organizar rotina   | Streamlit + Termômetro  |
| Operacional | Checklist de integrantes e agenda integrada     | Facilitar gestão pessoal             | Google Calendar / Figma |

---

## 📚 3. Protótipos de Visualização (com Streamlit)

A aplicação é desenvolvida em Python com Streamlit e estruturada em:

### 3.1 Módulos

- `dashboard.py`: dashboard principal (EPTC + Zona Azul)
- `ab_test.py`: módulo com visualização de testes A/B
- `status_fontes.py`: status de integração das fontes

### 3.2 Visualizações

- KPI cards (Altair / Streamlit): média de vagas ocupadas, receita, tarifa
- Linhas de ocupação por bairro (Altair)
- Heatmap de ocupacão horária (Altair)
- Checklist de tarefas (st.checkbox)
- Termômetro de alerta de atrasos (customizado)

### 3.3 Layout Sugerido

- **Aba 1: Visão Geral**

  - KPIs Gerais
  - Ocupação por bairro (linha)
  - Receita e tarifa média

- **Aba 2: Operacional**

  - Checklist
  - Alertas de pendências
  - Agenda e links úteis

- **Aba 3: Tática**

  - Burndown chart (plotly)
  - Kanban simplificado

---

## 📏 4. Mapa de Decisões Apoiado por Dados

| Decisão                          | Dados Suporte                | Visualização             |
| -------------------------------- | ---------------------------- | ------------------------ |
| Redistribuição de recursos       | Ocupação por bairro / tarifa | Gráfico de barras        |
| Alerta de atrasos                | Checklist e datas de entrega | Termômetro / Lista       |
| Ajuste de sprint                 | Burndown chart               | Linha de progresso       |
| Priorizacão de funcionalidades   | Receita x demanda por bairro | Scatterplot / KPI        |
| Alocação de check-ins com equipe | Check-ins semanais e humor   | Gráfico de humor (emoji) |

---

## 🌐 5. Ferramentas Utilizadas

| Função       | Ferramentas                   |
| ------------ | ----------------------------- |
| Visualização | Streamlit, Altair, Plotly     |
| BI           | Power BI, Looker Studio       |
| Prototipação | Miro, Figma, Canva            |
| Táticas      | Trello, Jira, Notion          |
| Integração   | Python, Snowflake, PostgreSQL |

---

## 🏆 6. Repositório GitHub - Documentação .MD

### `/README.md`

````md
# Estaciona+ DataViz & Storytelling

Dashboard interativo para visualização de KPIs da Zona Azul de Porto Alegre, integrado ao projeto de BI e DW.

## Componentes:
- KPIs (Ocupadas, Livres, Receita)
- Heatmaps
- Teste A/B
- Tarefas e Checklist

## Tecnologias:
- Python 3.10
- Streamlit
- Altair
- Snowflake
- Power BI

## Rodar localmente:
```bash
pip install -r requirements.txt
streamlit run dashboard.py
````

## Estrutura

- `dashboard.py`: visualização principal
- `data/`: amostras sintéticas e APIs
- `README.md`: este arquivo

## Licença

[MIT License](LICENSE)

```

---

> Este documento integra a Etapa 5 da APS de Visualização de Dados, conforme orientação metodológica da disciplina. Baseado no framework completo da APS de BI do Estaciona+.

```
