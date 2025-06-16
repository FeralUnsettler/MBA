# APS Visualização de Dados e Data Storytelling
## Etapa 5: Plano de Análise e Visualização

### Projeto: Estaciona+
**Tema Central:** Plataforma SaaS para otimização de vagas em Zona Azul
**Propósito:** Mobilidade urbana inteligente, integração de dados abertos, experiência do usuário, sustentabilidade e eficiência urbana

---

## Lista de Análises Previstos

| Análise | Objetivo | Ferramenta | Responsável |
|--------|----------|------------|--------------|
| Ocupação de vagas por bairro e hora | Identificar picos de uso e otimizacão de rotação | Power BI / Snowflake / Streamlit | BI/DataEng |
| Receita por bairro / hora | Avaliar rentabilidade por região | Power BI / Excel | Financeiro |
| Comparativo entre tarifário e arrecadação | Verificar impacto das políticas de preço | Power BI / Snowflake | Produto/Negócios |
| Tempo médio de busca por vaga | Medir eficiência da experiência do usuário | GA4 / Logs / Streamlit | UX |
| Desempenho de fontes de dados (EPTC, Zona Azul, SigaPay) | Analisar latência e disponibilidade | Grafana / Logs / Streamlit | DevOps |
| A/B Testes (ex: notificação push) | Validar funcionalidades e experiências | Streamlit / Google Forms | UX |
| Progresso do projeto | Monitorar execução por fase e entrega | Power BI / Excel / Trello | PM |
| Engajamento da equipe | Check-ins, carga de trabalho, bloqueios | Forms / Excel / Canva | Liderança |

---

## Rascunho de Visualizações Esperadas

### Painel Estratégico (Topo)
- Indicadores de OKRs (Receita, Ocupação, Tempo de Busca)
- Gauge de metas versus valores atuais
- Termômetro de integração de fontes (EPTC / SigaPay)
- Mapa de calor da cidade com hotspots de demanda
- Linha de progresso do roadmap

### Painel Tático (Meio)
- Gráfico de burndown por sprint
- Kanban simplificado com status por equipe
- Gráfico de barras: tarefas por área e status (em andamento, bloqueadas...)
- Termômetro semanal de humor e percepção de progresso (com emoji, smiley ou nota)
- Heatmap de alinhamento: BI vs UX vs SI vs Liderança

### Painel Operacional (Rodapé)
- Calendário de prazos e eventos
- Checklist individual por integrante
- Alertas de pendências próximas (cores por criticidade)
- Links rápidos para documentos compartilhados e fontes de dados

---

## Mapa de Decisões Apoiadas

| Decisão | Dados que apoiam |
|---------|------------------|
| Onde ampliar a Zona Azul | Mapa de calor de ocupação |
| Ajuste de tarifas por bairro | Receita x Ocupação por hora |
| Adoção de funcionalidade nova | A/B Test + check-in de usabilidade |
| Reorganização de tarefas | Carga de trabalho e atrasos |
| Priorizacão de integração com fontes | Latência e uptime das APIs |

---

## Ferramentas Propostas
- **Power BI** (indicadores estratégicos, burndown, comparativos)
- **Streamlit** (painel operacional dinâmico, simulações, coleta de A/B test)
- **Excel / Google Sheets** (check-ins, status de tarefas)
- **Figma / Canva** (design inicial dos dashboards, layout visual)
- **Grafana** (monitoramento de APIs e integrações)

---

## Boas Práticas de Visualização Aplicadas
- Cores com significado: verde (ok), amarelo (atenção), vermelho (crítico)
- Gráficos de barras, linhas, gauges e mapas
- Filtros por semana, tarefa, integrante ou objetivo
- Seções bem separadas por nível de decisão (estratégico, tático, operacional)

---

**Conclusão:**
Este plano de visualização integra elementos de storytelling, KPIs, monitoramento operacional e acompanhamento de projeto. A APS visa conectar decisões de mobilidade urbana com dados objetivos, promovendo transparência, foco em resultados e engajamento das equipes de forma clara, acessível e orientada à ação.