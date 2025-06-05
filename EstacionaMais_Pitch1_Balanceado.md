# 🎤 Roteiro do Pitch – Estaciona+ ⏱️ Duração Total: 5 minutos

#### Roteiro por Luciano M Fagundes - BMDS©2025
---
## 👩‍💼 Sonia – Introdução (1 minuto)
Objetivo: Apresentar o problema e a proposta de valor do Estaciona+.

### Script:

# "Boa tarde a todos! Sou a Sonia, e junto com meu colega Luciano, vamos apresentar o Estaciona+, uma solução inovadora para otimizar o estacionamento rotativo em Porto Alegre. 🚗

# Encontrar uma vaga na Zona Azul pode ser um desafio diário. O Estaciona+ é uma plataforma SaaS que integra dados em tempo real da EPTC, Zona Azul e SigaPay para oferecer aos motoristas informações precisas sobre disponibilidade de vagas, reduzindo o tempo de busca e melhorando a mobilidade urbana."
---
---
Interação com Luciano:

# "Para entender como transformamos dados em insights acionáveis, passo a palavra para o Luciano, que explicará a arquitetura de dados e as fontes de informação que sustentam o Estaciona+."
---
---

## 👨‍💼 Luciano – Parte Central (3 minutos)
Objetivo: Detalhar as fontes de dados e a arquitetura de dados proposta.

### Script:

# "Obrigado, Sonia! Vamos explorar como o Estaciona+ utiliza dados de diferentes fontes e uma arquitetura robusta para entregar valor:

### Fontes de Dados e Integração:

# EPTC (Empresa Pública de Transporte e Circulação):

## Dados Disponíveis: 
* Localização e quantidade de vagas de estacionamento rotativo
*  horários de funcionamento
*  regras específicas por região
*  informações sobre vagas reservadas para idosos e pessoas com deficiência, dados de fiscalização e monitoramento de vagas.

## Acesso aos Dados: 
* Portal de Dados Abertos de Porto Alegre (dadosabertos.poa.br)
* EPTC Transparente (eptctransparente.com.br)
* contato direto via eptc@eptc.prefpoa.com.br.

# Zona Azul:

### Dados Disponíveis: 
* Distribuição das vagas de estacionamento rotativo na cidade
* tarifas atualizadas por tempo de permanência
* regras de utilização e horários de funcionamento.

### Acesso aos Dados:
* Informações públicas disponíveis no site da Prefeitura de Porto Alegre (prefeitura.poa.br)
* contato com a concessionária responsável para dados mais detalhados.

# SigaPay:

## Dados Disponíveis:
* Transações de ativação de estacionamento
* histórico de pagamentos e tempo de permanência dos usuários
* notificações de irregularidades e regularizações efetuadas.

## Acesso aos Dados:
* Contato direto com a equipe do SigaPay para estabelecer parcerias e acesso a APIs (contato@sigapay.com.br)
* informações gerais disponíveis no site (sigapay.com.br).

# Arquitetura de Dados Proposta:

## Camada de Ingestão de Dados:
Objetivo: Coletar dados em tempo real das fontes mencionadas.

### Ferramentas Sugeridas: 
* APIs RESTful fornecidas pelas entidades
* webhooks para eventos em tempo real
* ETL (Extract, Transform, Load) para dados históricos.

## Data Lake:
Objetivo: Armazenar grandes volumes de dados brutos, estruturados e não estruturados.
### Tecnologias Sugeridas: 
* Amazon S3
* Google Cloud Storage
* Azure Data Lake.

## Data Warehouse (DW):
Objetivo: Organizar e estruturar os dados para análises e geração de insights.
### Tecnologias Sugeridas:
* Amazon Redshift
* Google BigQuery
* Snowflake.

### Business Intelligence (BI):
Objetivo: Visualizar dados e métricas para tomada de decisões.
### Ferramentas Sugeridas: 
* Tableau
* Power BI
* Looker
* Streamlit

# Com essa estrutura, o Estaciona+ transforma dados em decisões estratégicas, melhorando a experiência dos motoristas e a eficiência operacional."
---
---
### Interação com Sonia:

# "Sonia, poderia compartilhar como esses insights se traduzem em benefícios concretos para os usuários e para a cidade?"
---
---

# 👩‍💼 Sonia – Encerramento (1 minuto)
Objetivo: Destacar os benefícios e próximos passos.

### Script:

# "Claro, Luciano! Com o Estaciona+, os motoristas economizam tempo e reduzem o estresse ao encontrar vagas mais rapidamente. Para a cidade, isso significa menor congestionamento e melhor utilização dos espaços urbanos.

# Além disso, a plataforma oferece dados valiosos para a gestão pública, auxiliando na tomada de decisões sobre mobilidade urbana.

# Estamos prontos para escalar essa solução, contribuindo para uma Porto Alegre mais inteligente e eficiente.

# Obrigado pela atenção!"

---
---
---

# 🖥️ Apresentação de Slides em Markdown
Apresentação em formato Markdown, utilizando a paleta de cores especificada e design responsivo. As tabelas do framework original foram incluídas para apoiar o pitching.

---

marp: true

theme: default

paginate: true

style: |

  section {

    font-family: 'Segoe UI', sans-serif;

    color: #1A1A1A;

    background-color: #F4F4F8;

  }

  h1, h2, h3 {

    color: #FE4A49;

  }

  .accent {

    color: #2AB7CA;

  }

  .highlight {

    background-color: #FED766;

    padding: 0.2em;

  }

  table {

    width: 100%;

    border-collapse: collapse;

  }

  th, td {

    border: 1px solid #E6E6EA;

    padding: 0.5em;

    text-align: left;

  }

  th {

    background-color: #2AB7CA;

    color: #F4F4F8;

  }

---

# Estaciona+

## Otimizando o estacionamento urbano com BI e Data Warehousing

---

## Problema

- Dificuldade em encontrar vagas na Zona Azul

- Tempo perdido e aumento do tráfego

- Falta de informações em tempo real

---

## Solução

- Plataforma SaaS integrada com dados da EPTC, Zona Azul e SigaPay

- Informações em tempo real sobre disponibilidade de vagas

- Análises preditivas para otimizar o uso das vagas

---

## Fontes de Dados e Integração

### EPTC

- **Dados Disponíveis:**

  - Localização e quantidade de vagas de estacionamento rotativo

  - Horários de funcionamento e regras específicas por região

  - Informações sobre vagas reservadas para idosos e pessoas com deficiência

  - Dados de fiscalização e monitoramento de vagas

- **Acesso aos Dados:**

  - Portal de Dados Abertos de Porto Alegre: [dadosabertos.poa.br](https://dadosabertos.poa.br)

  - EPTC Transparente: [eptctransparente.com.br](https://eptctransparente.com.br)

  - Contato direto: eptc@eptc.prefpoa.com.br

---

### Zona Azul

- **Dados Disponíveis:**

  - Distribuição das vagas de estacionamento rotativo na cidade

  - Tarifas atualizadas por tempo de permanência

  - Regras de utilização e horários de funcionamento

- **Acesso aos Dados:**

  - Informações públicas: [prefeitura.poa.br](https://prefeitura.poa.br)

  - Contato com a concessionária responsável para dados mais detalhados

---

### SigaPay

- **Dados Disponíveis:**

  - Transações de ativação de estacionamento

  - Histórico de pagamentos e tempo de permanência dos usuários

  - Notificações de irregularidades e regularizações efetuadas

- **Acesso aos Dados:**

  - Contato direto: contato@sigapay.com.br

  - Informações gerais: [sigapay.com.br](https://sigapay.com.br)

---

## Arquitetura de Dados Proposta

### Camada de Ingestão de Dados

- **Objetivo:** Coletar dados em tempo real das fontes mencionadas

- **Ferramentas Sugeridas:**

  - APIs RESTful fornecidas pelas entidades

  - Webhooks para eventos em tempo real

  - ETL (Extract, Transform, Load) para dados históricos

---

### Data Lake

- **Objetivo:** Armazenar grandes volumes de dados brutos, estruturados e não estruturados

- **Tecnologias Sugeridas:**

  - Amazon S3

  - Google Cloud Storage

  - Azure Data Lake

---

### Data Warehouse (DW)

- **Objetivo:** Organizar e estruturar os dados para análises e geração de insights

- **Tecnologias Sugeridas:**

  - Amazon Redshift

  - Google BigQuery

  - Snowflake

---

### Business Intelligence (BI)

- **Objetivo:** Visualizar dados e métricas para tomada de decisões

- **Ferramentas Sugeridas:**

  - Tableau

  - Power BI

  - Looker

---

## Benefícios

- Redução do tempo de busca por vagas

- Melhor experiência para o usuário

- Dados para decisões estratégicas na gestão urbana

---

## Próximos Passos

- Escalar a solução para outras cidades

- Integrar novos parceiros e fontes de dados

- Continuar aprimorando os modelos preditivos

---

## Obrigado!

**Sonia & Luciano**

MBA em BI e Data Warehousing


🎨 Prompts para Geração de Imagens por Slide
Para enriquecer a apresentação, sugerimos os seguintes prompts para geração de imagens utilizando ferramentas de inteligência artificial:

Slide 1 – Estaciona+:

Prompt: "Ilustração de um aplicativo móvel mostrando um mapa urbano com ícones de vagas de estacionamento disponíveis, utilizando as cores #FE4A49, #2AB7CA e #FED766."

Slide 2 – Problema:

Prompt: "Imagem de um motorista frustrado procurando vaga em uma rua movimentada de Porto Alegre, com placas de 'Zona Azul' visíveis."

Slide 3 – Solução:

Prompt: "Interface de aplicativo móvel exibindo mapa de Porto Alegre com ícones indicando vagas de estacionamento disponíveis em tempo real, utilizando as cores #2AB7CA e #FED

Slide4 – Fontes de Dados e Integração:


Prompt: "Diagrama de integração de dados mostrando conexões entre EPTC, Zona Azul e SigaPay, com setas indicando fluxo de dados para uma plataforma centralizada."


Slide 5 – EPTC:


Prompt: "Tabela estilizada apresentando dados de localização e quantidade de vagas de estacionamento rotativo, horários de funcionamento e regras específicas por região fornecidos pela EPTC."


Slide 6 – Zona Azul:


Prompt: "Tabela comparativa mostrando tarifas atualizadas por tempo de permanência e regras de utilização da Zona Azul em Porto Alegre."


Slide 7 – SigaPay:


Prompt: "Captura de tela do aplicativo SigaPay exibindo histórico de pagamentos e tempo de permanência dos usuários, com notificações de irregularidades."


Slide 8 – Arquitetura de Dados Proposta:


Prompt: "Diagrama de arquitetura de dados em camadas, incluindo ingestão de dados, data lake, data warehouse e ferramentas de BI, com ícones representativos para cada componente."


Slide 9 – Camada de Ingestão de Dados:


Prompt: "Ilustração de processos de ingestão de dados em tempo real utilizando APIs RESTful e webhooks, com setas indicando fluxo de dados para o data lake."


Slide 10 – Data Lake:


Prompt: "Representação visual de um data lake armazenando grandes volumes de dados brutos, com ícones de diferentes formatos de dados (estruturados e não estruturados)."


Slide 11 – Data Warehouse (DW):


Prompt: "Diagrama mostrando a organização e estruturação de dados dentro de um data warehouse, com destaque para ferramentas como Amazon Redshift, Google BigQuery e Snowflake."


Slide 12 – Business Intelligence (BI):


Prompt: "Dashboard de BI exibindo gráficos e métricas relacionadas ao uso de vagas de estacionamento, utilizando ferramentas como Tableau ou Power BI."


Slide 13 – Benefícios:


Prompt: "Infográfico destacando benefícios do Estaciona+, como redução do tempo de busca por vagas, melhor experiência para o usuário e dados para decisões estratégicas na gestão urbana."


Slide 14 – Próximos Passos:


Prompt: "Roadmap visual ilustrando os próximos passos do projeto Estaciona+, incluindo expansão para outras cidades, integração com novos parceiros e aprimoramento dos modelos preditivos."


Slide 15 – Agradecimento:


Prompt: "Imagem de fundo com a skyline de Porto Alegre ao entardecer, com texto de agradecimento sobreposto e logotipos da EPTC, Zona Azul e SigaPay."





