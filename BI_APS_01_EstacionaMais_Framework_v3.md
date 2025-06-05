**Proposta de Valor do Estaciona+**  
---

**Para**  
 Motoristas de veículos automotores

**que**  
 precisam encontrar vagas para estacionamento em Zona Azul

**o Estaciona+**  
 é uma **plataforma SaaS**

**que**  
 ajuda os motoristas a encontrarem vagas de forma ágil e dinâmica,  
 por meio da integração em tempo real com os dados da EPTC e da Zona Azul

**Diferente de**  
 o Siga Pay,

**meu produto**  
 faz a integração em tempo real dos dados da EPTC, Zona Azul e Siga Pay para encontrar vagas com

• agilidade e precisão baseada no tempo de permanência  
 • análise de dados históricos e atuais  
 • otimização inteligente das vagas disponíveis

…além de outras funcionalidades a serem definidas para oferecer uma experiência completa e eficiente.

# APS  **Etapa 1 – Entendimento e Delimitação** **Duração estimada: 1 h**

---

## Decisões que o projeto precisa tomar e como o BI pode apoiar cada uma

| Decisão do Estaciona+ | Como o BI pode apoiar |
| :---- | :---- |
| **1\. Seleção das fontes de dados e frequência de ingestão**  – EPTC, Zona Azul e SigaPay: quais APIs, quais endpoints, qual “refresh rate”? | • Monitorar disponibilidade e latência de cada fonte via dashboards em tempo real. • Alertas automáticos em caso de falhas ou atrasos na ingestão de dados. |
| **2\. Definição de KPIs de sucesso do serviço**  – Ex.: tempo médio de busca de vaga, taxa de ocupação, tempo médio de permanência. | • Relatórios periódicos de evolução dos KPIs históricos e comparação com metas definidas. • Drill-down para identificar picos de uso por área e horário. |
| **3\. Estratégia de previsão de disponibilidade**  – Qual modelo de ML usar, quais variáveis (clima, eventos, dia da semana, padrões de uso). | • Análise exploratória dos dados para identificação de correlações e variáveis mais relevantes. • Dashboard de performance do modelo (acurácia, recall) e retraining programado. |
| **4\. Prioridade de funcionalidades de UX/UI**  – Notificações, mapa interativo, filtro por tipo de vaga (PCD, idoso). | • Coleta e análise de comportamento de uso (heatmaps, cliques, tempo de sessão) para balizar quais funcionalidades geram maior engajamento. • A/B tests analisados em tempo real. |
| **5\. Políticas de segurança e compliance de dados**  – Criptografia, GDPR/Lei Geral de Proteção de Dados, \\\[…\] |  |

| **5\. Políticas de segurança e compliance de dados**   
– Criptografia, LGPD, controle de acesso, anonimização de dados sensíveis. | • Relatórios de auditoria de acesso a dados.  
• Monitoramento de incidentes de segurança e tendência de requisições falhas ou não autorizadas. | \\| \*\*6. Definição da arquitetura escalável (Data Lake, DW e Camada de BI)\*\*  
– Infraestrutura on-premises vs. cloud, tecnologia. | • Análise de custos x performance das diferentes opções via cenários simulados.  
• Dashboards de utilização de recursos (storage, CPU, memória), para otimização contínua. | \\| \*\*7. Acordos de nível de serviço (SLAs) com parceiros\*\*  
– EPTC, concessionárias, SigaPay: frequência de entrega, qualidade mínima. | • Painel de SLAs com indicadores de cumprimento (uptime, latência, percentual de dados válidos).  
• Alertas quando os níveis de serviço estiverem próximos ao limite. | \\| \*\*8. Governança de dados e responsabilidade\*\*  
– Quem é dono de cada dado, processo de aprovação de mudanças, catálogo de metadados. | • Catálogo de metadados integrado ao BI para navegar pela origem dos dados.  
• Relatórios de ciclo de vida de dados (data lineage) e de qualidade (completude, consistência). | \\| \*\*9. Modelo de monetização e pricing do serviço\*\*  
– Gratuito com ads, assinatura premium, pay-per-use. | • Análise de receita por cliente e churn rate em dashboards interativos.  
• Simulações de cenários de preço e impacto na adoção usando dados históricos. | \\| \*\*10. Métrica de produtividade da equipe de desenvolvimento\*\*  
– Lead time de deploy, volume de features entregues, bugs por release. | • Relatórios de fluxo de trabalho (CI/CD) e de qualidade de código.

• Painel de acompanhamento de sprints e indicadores de eficiência (cycle time, velocity). |

---

### Áreas que demandarão suporte de BI

* **Experiência do Usuário (UX)** • Heatmaps, A/B tests e métricas de engajamento para priorizar melhorias iterativas.  
    
* **Segurança e Compliance** • Monitoramento de acessos, auditorias e conformidade com LGPD/GDPR via painéis dedicados.  
    
* **Produtividade da Equipe** • Dashboards de performance de desenvolvimento (CI/CD, testes automatizados, bugs) para orientar práticas ágeis.  
    
* **Resultados do Produto** • Acompanhamento de adoção, retenção, monetização e ROI, com análises históricas e projeções de receita.

---

Este quadro consolida as principais decisões estratégicas do Estaciona+ e mostra como um sistema de BI e Data Warehouse pode apoiar cada etapa do ciclo de vida do produto, desde a concepção até a operação contínua.  
Para o desenvolvimento do **Estaciona+**, um serviço inteligente de otimização de vagas de estacionamento em Porto Alegre, é essencial estabelecer um plano robusto de coleta e integração de dados. O objetivo é consolidar informações em tempo real da **EPTC**, **Zona Azul** e **SigaPay**, proporcionando aos usuários uma experiência eficiente e informada ao buscar vagas disponíveis.

---

## 🧠 Visão Geral do Estaciona+

**Objetivo**: Integrar dados de mobilidade urbana para fornecer aos usuários informações precisas sobre disponibilidade de vagas, tempo de permanência e outras funcionalidades que otimizem o uso do estacionamento rotativo na cidade.

---

## 📊 Fontes de Dados e Integração

### 1\. **EPTC (Empresa Pública de Transporte e Circulação)**

* **Dados Disponíveis**:

* Localização e quantidade de vagas de estacionamento rotativo.  
* Horários de funcionamento e regras específicas por região.  
* Informações sobre vagas reservadas para idosos e pessoas com deficiência.  
* Dados de fiscalização e monitoramento de vagas.

* **Acesso aos Dados**:

* Portal de Dados Abertos de Porto Alegre: [dadosabertos.poa.br](https://dadosabertos.poa.br)  
* EPTC Transparente: [eptctransparente.com.br](https://eptctransparente.com.br)  
* Contato direto para solicitações específicas: eptc@eptc.prefpoa.com.br([Prefeitura de Porto Alegre](https://www.prefeitura.poa.br/eptc?utm_source=chatgpt.com))

### 2\. **Zona Azul**

* **Dados Disponíveis**:

* Distribuição das vagas de estacionamento rotativo na cidade.  
* Tarifas atualizadas por tempo de permanência.  
* Regras de utilização e horários de funcionamento.([Prefeitura de Porto Alegre](https://prefeitura.poa.br/eptc/estacionamento-rotativo-area-azul?utm_source=chatgpt.com))

* **Acesso aos Dados**:

* Informações públicas disponíveis no site da Prefeitura de Porto Alegre: [prefeitura.poa.br](https://prefeitura.poa.br/eptc/estacionamento-rotativo-area-azul)  
* Contato com a concessionária responsável para dados mais detalhados.

### 3\. **SigaPay**

* **Dados Disponíveis**:

* Transações de ativação de estacionamento.  
* Histórico de pagamentos e tempo de permanência dos usuários.  
* Notificações de irregularidades e regularizações efetuadas.

* **Acesso aos Dados**:

* Contato direto com a equipe do SigaPay para estabelecer parcerias e acesso a APIs: contato@sigapay.com.br  
* Informações gerais disponíveis no site: [sigapay.com.br](https://sigapay.com.br/)

---

## 🧱 Arquitetura de Dados Proposta

### 1\. **Camada de Ingestão de Dados**

* **Objetivo**: Coletar dados em tempo real das fontes mencionadas.

* **Ferramentas Sugeridas**:

* APIs RESTful fornecidas pelas entidades.  
* Webhooks para eventos em tempo real.  
* ETL (Extract, Transform, Load) para dados históricos.

### 2\. **Data Lake**

* **Objetivo**: Armazenar grandes volumes de dados brutos, estruturados e não estruturados.

* **Tecnologias Sugeridas**:

* Amazon S3, Google Cloud Storage ou Azure Data Lake.

### 3\. **Data Warehouse (DW)**

* **Objetivo**: Organizar e estruturar os dados para análises e geração de insights.

* **Tecnologias Sugeridas**:

* Amazon Redshift, Google BigQuery ou Snowflake.

### 4\. **Business Intelligence (BI)**

* **Objetivo**: Visualizar dados e métricas para tomada de decisões.

* **Ferramentas Sugeridas**:

* Tableau, Power BI ou Looker.

---

## 🚀 Funcionalidades Planejadas do Estaciona+

* **Localização de Vagas em Tempo Real**: Mapeamento das vagas disponíveis com base nos dados integrados.  
* **Previsão de Disponibilidade**: Utilização de algoritmos de machine learning para prever a disponibilidade de vagas em determinados horários e locais.  
* **Notificações Personalizadas**: Alertas sobre vencimento do tempo de estacionamento, vagas próximas e oportunidades de regularização.  
* **Análise de Comportamento**: Estudo dos padrões de uso das vagas para otimizar a rotatividade e eficiência do sistema.

---

## 📅 Cronograma de Implementação

| Fase | Duração Estimada |
| ----- | ----- |
| Planejamento e Parcerias | 1 mês |
| Desenvolvimento da Arquitetura de Dados | 2 meses |
| Integração com Fontes de Dados | 1 mês |
| Desenvolvimento do Aplicativo | 2 meses |
| Testes e Ajustes Finais | 1 mês |
| Lançamento e Monitoramento | Contínuo |

---

Este plano visa estabelecer uma base sólida para o desenvolvimento do Estaciona+, garantindo a integração eficiente dos dados disponíveis e proporcionando uma experiência aprimorada aos usuários na busca por vagas de estacionamento em Porto Alegre.

Etapa 2:

**Etapa 2 – Plano de Coleta de Dados** **Duração estimada: 1 h**

---

## 1\. Visão Geral

Nesta etapa, definimos quais dados precisamos coletar (internos e externos), onde encontrá-los, quem ficará responsável pelo acesso e quais ferramentas usaremos para ingestão.

---

## 2\. Tabela de Dados

| Tipo | Dado | Localização / Fonte | Responsável | Ferramenta de Acesso |
| :---- | :---- | :---- | :---- | :---- |
| **Interno** | Registro de transações do Estaciona+ | Banco de dados relacional do app (PostgreSQL) | Equipe de Backend | SQL / ORM (SQLAlchemy) / Airflow |
| **Interno** | Logs de uso do mapa e buscas de vagas | Elasticsearch ou arquivo de logs (JSON) | Equipe de DevOps | Filebeat → ELK Stack / Fluentd |
| **Interno** | Métricas de performance da API (latência, erros, throughput) | Prometheus \+ Grafana | Equipe de DevOps | PromQL / Grafana API |
| **Interno** | Dados de cadastro de usuários (plaqueamento, perfil, preferências) | PostgreSQL | Equipe de Backend | SQL / ORM |
| **Interno** | Eventos de interação UX/UI (cliques nos filtros, sessões ativas) | Google Analytics 4 / Mixpanel | Equipe de Produto | GA4 API / Mixpanel SDK |
| **Externo** | Localização e quantidade de vagas de estacionamento rotativo | Portal Dados Abertos de POA (EPTC) | Equipe de Dados | API REST / CSV JSON via HTTP |
| **Externo** | Tarifas e regras de Zona Azul | Site Prefeitura (EPTC) / Concessionária Zona Azul | Equipe de Parcerias | Scraping automatizado / API da concessionária |
| **Externo** | Transações, tempos de permanência e regularizações do SigaPay | API SigaPay (por contrato de parceria) | Equipe de Parcerias | API REST (OAuth2) / Webhooks |
| **Externo** | Eventos urbanos (shows, jogos, feiras) que impactam demanda por vagas | API de Agenda Cultural de POA / API de Eventos da FIERGS | Equipe de Inteligência de Negócio | HTTP REST / JSON |
| **Externo** | Condições meteorológicas (chuva, temperatura, vento) | API de Clima (OpenWeatherMap, Climatempo, etc.) | Equipe de Ciência de Dados | API REST / SDK Python |
| **Externo** | Tráfego em tempo real (fluxo de veículos, bloqueios de via) | EPTC Transparente / Waze for Cities API | Equipe de Dados | API REST / Kafka |
| **Externo** | Base geoespacial de ruas, calçadas e pontos de interesse | OpenStreetMap / Geoportal POA | Equipe de Geoprocessamento | Overpass API / QGIS / PostGIS |

---

## 3\. Fluxo de Acesso e Ferramentas

1. **Orquestração**  
     
   * **Airflow** para orquestrar jobs de ingestão histórica (ETL) e incremental (CDC).  
   * **Argo Workflows** ou **Prefect** para pipelines em cloud.

   

2. **Ingestão em Lote**  
     
   * Conectar via **REST APIs** ou ingestão de dumps (CSV/JSON) do Portal de Dados Abertos.  
   * Carregar no **Data Lake** (S3 / GCS) na zona “raw”.

   

3. **Ingestão em Tempo Real**  
     
   * **Webhooks** do SigaPay para transações de estacionamento.  
   * **Kafka** para captar eventos de logs e métricas de API.  
   * **Filebeat** → **Logstash** → **Elasticsearch** para logs de uso.

   

4. **Transformação e Armazenamento**  
     
   * **dbt** ou **Spark** para transformação incremental e historização.  
   * Carregar dados tratados em **Data Warehouse** (BigQuery / Redshift / Snowflake).

   

5. **Catálogo e Governança**  
     
   * **Data Catalog** (AWS Glue / DataHub) para registrar metadados, proprietários e dicionário de dados.  
   * **IAM** e políticas de acesso (RBAC) para controle de quem pode consultar cada área.

---

## 4\. Responsabilidades Principais

* **Equipe de Backend**: expor endpoints e manter integridade dos dados internos.  
* **Equipe de DevOps/Data Engineering**: provisionar infraestrutura, pipelines de ingestão e monitoramento.  
* **Equipe de Ciência de Dados/BI**: modelagem de dados, catálogos, dashboards e análises preditivas.  
* **Equipe de Parcerias**: negociar SLAs, acesso a APIs e credenciais com EPTC, Zona Azul e SigaPay.  
* **Equipe de Produto/UX**: configurar GA4, Mixpanel e traduzir requisitos de engajamento em eventos mensuráveis.

---

Com este plano de coleta detalhado, o Estaciona+ terá uma base sólida de dados internos e externos, organizada e automatizada, pronta para alimentar o Data Warehouse e suportar análises de BI e modelos de previsão.

Produto  
**Plano de Coleta de Dados – Tabela Resumida**

| Fonte dos Dados | Tipo de Dado | Onde Está | Quem Coleta | Ferramentas Previstas |
| :---- | :---- | :---- | :---- | :---- |
| **Banco de dados do Estaciona+** | Transações de uso, cadastro de usuários, tempo de permanência | PostgreSQL do aplicativo | Equipe de Backend | SQL/ORM (SQLAlchemy), Airflow |
| **Elasticsearch / Logs do app** | Logs de uso do mapa, buscas e eventos de API | Cluster Elasticsearch ou arquivos JSON | Equipe de DevOps | Filebeat → Logstash → ELK Stack |
| **Prometheus \+ Grafana** | Métricas de performance (latência, erros, throughput) | Servidores de monitoramento | Equipe de DevOps | PromQL, Grafana API |
| **Google Analytics 4 / Mixpanel** | Eventos UX/UI (cliques, sessões, fluxos de navegação) | Plataformas GA4 e Mixpanel | Equipe de Produto | GA4 API, Mixpanel SDK |
| **Portal Dados Abertos de POA (EPTC)** | Localização e quantidade de vagas de Zona Azul | API REST / CSV/JSON | Equipe de Dados | Python Requests / Airflow |
| **Site da Prefeitura / Concessionária Zona Azul** | Tarifas, regras e horários do estacionamento rotativo | Site EPTC / API concessionária | Equipe de Parcerias | Scraping automatizado / API REST |
| **API SigaPay (via parceria)** | Transações de pagamento, regularizações, tempo de ocupação | Endpoints SigaPay | Equipe de Parcerias | REST API (OAuth2), Webhooks |
| **API de Eventos Culturais e Esportivos (POA, FIERGS)** | Agenda de shows, jogos e feiras que impactam demanda | API públicas | Equipe de Inteligência | REST API, JSON parsing |
| **API de Clima (OpenWeatherMap, Climatempo, etc.)** | Condições meteorológicas em tempo real | Endpoints de serviço de clima | Equipe de Ciência de Dados | SDK Python / REST API |
| **EPTC Transparente / Waze for Cities API** | Fluxo de veículos, bloqueios, incidentes de trânsito | API REST / Streams Kafka | Equipe de Dados | Kafka, REST API |
| **OpenStreetMap / Geoportal POA** | Base geoespacial de ruas, calçadas e pontos de interesse | Overpass API / Geoportal | Equipe de Geoprocessamento | QGIS, PostGIS, Overpass API |

**Legenda:**

* **Equipe de Backend/DevOps**: implementação e manutenção dos pipelines internos.  
* **Equipe de Dados/Ciência de Dados/BI**: ingestão, modelagem e dashboards.  
* **Equipe de Parcerias/Produto**: negociação de acesso e definição de eventos de uso.  
* **Ferramentas**: orquestração via Airflow, processamento via dbt/Spark, storage em Data Lake (S3/GCS) e Data Warehouse (BigQuery/Redshift/Snowflake).

