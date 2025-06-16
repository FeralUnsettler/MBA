# APS Visualização de Dados e Data Storytelling
## Etapa 5: Plano de Análise e Visualização

### Projeto: Estaciona+
**Tema Central:** Plataforma SaaS inteligente para otimização de vagas em Zona Azul
**Propósito:** Mobilidade urbana, inovação, integração em tempo real com dados públicos (EPTC, Zona Azul, SigaPay)

---

## Lista de Análises Previstos
| Análise | Objetivo | Ferramenta | Responsável |
|--------|----------|------------|--------------|
| Ocupação de vagas por bairro/hora | Identificar picos de uso e rotatividade | Streamlit + Snowflake | BI/DataEng |
| Receita por bairro | Analisar desempenho financeiro da Zona Azul | Streamlit + Altair | Financeiro |
| Tempo médio de busca | Otimizar experiência do usuário | Logs + Estimativa | UX/Produto |
| Eficiência das fontes (EPTC, SigaPay) | Avaliar disponibilidade e latência | Dashboard simulado | DevOps |
| A/B Test Notificações | Avaliar impacto de funcionalidades | Streamlit Table | UX/Produto |
| Progresso do projeto (burndown e tarefas) | Monitorar execução | Excel ou Power BI | Gestão |

---

## Rascunho de Visualizações Esperadas

### Função Estratégica (Topo)
- **KPI Geral de Ocupação:** Termômetro de uso das vagas (ocupadas/livres)
- **Receita Total vs Meta:** Gráfico de progresso (barra preenchida ou gauge)
- **OKR de Inovação:** Indicador de integrações ativas e tempo real
- **Mapa de Calor por Bairro:** Visualização de hotspots de demanda

### Função Tática (Meio)
- **Kanban Simples:** Tarefas por área com status (concluído, pendente, bloqueado)
- **Gráfico de Gantt ou Burndown:** Progresso por sprint
- **Distribuição de Carga de Trabalho:** Gráfico de barras por integrante
- **Check-in semanal:** Termômetro de humor/percepção (faces ou ícones)

### Função Operacional (Rodapé)
- **Agenda Integrada:** Calendário com deadlines e eventos
- **Alertas Visuais:** Lista de tarefas críticas com semáforos (verde, amarelo, vermelho)
- **Checklist por Integrante:** Tabelas com status de entrega
- **Histórico e Links:** Lista clicável de documentos compartilhados

---

## Mapa de Decisões Apoiadas
| Decisão | Dado/Auxílio BI |
|---------|------------------|
| Onde expandir Zona Azul | Heatmap de ocupação |
| Ajuste de tarifas por bairro | Receita/ocupacao x padrão histórico |
| Prioridade de funcionalidades | Teste A/B e feedbacks |
| Ajuste de roadmap | Burndown + atraso de tarefas |
| Alocação de recursos | Carga por área/tempo execução |

---

## Ferramentas Sugeridas
- **Streamlit + Snowflake** para visualização operacional e protótipo funcional
- **Power BI / Excel** para visão estratégica e tática (Gantt, burndown, dashboard de progresso)
- **Figma/FigJam ou Canva** para design dos rascunhos de layout
- **Google Sheets + Forms** para check-in semanal e coleta de feedbacks

---

## Considerações Visuais
- **Cores:** Verde (ok), Amarelo (atenção), Vermelho (crítico)
- **Filtros dinâmicos:** Por bairro, por tarefa, por sprint
- **Disposição:** Topo (estratégico), meio (tático), rodapé (operacional)
- **Gráficos preferenciais:** Barras, linhas, gauges, heatmaps, indicadores

---

**Conclusão:**
Este modelo de visualização e storytelling de dados se alinha à proposta interdisciplinar da APS de BI, com impacto direto na tomada de decisões da equipe e do projeto Estaciona+, promovendo clareza, acompanhamento de metas e foco na entrega de valor em mobilidade urbana inteligente.

