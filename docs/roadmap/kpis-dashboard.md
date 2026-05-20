# KPIs e SLAs

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de métricas

## KPIs de valor

| Métrica | Definição | Meta inicial |
| --- | --- | --- |
| Tempo para valor | Tempo entre início do piloto e primeiro workflow útil validado | <= 14 dias |
| Precisão operacional | Percentual de saídas aceitas ou corrigidas minimamente por humano | >= 85% no piloto |
| Adoção | Usuários-alvo que executam o fluxo ao menos uma vez por semana | >= 60% |
| ROI | Ganho estimado menos custo do piloto | Positivo ou com tese clara |

## KPIs de segurança e resiliência

| Métrica | Definição | Meta inicial |
| --- | --- | --- |
| MTTR | Tempo médio para recuperar workflow após incidente | <= 4h em piloto |
| Replay success rate | Percentual de estados reconstruídos por eventos sem divergência | >= 99% |
| Policy block rate | Bloqueios corretos por política | Monitorar tendência |
| Incidentes SEV1 | Incidentes críticos | 0 |
| Eventos sem trace | Eventos sem rastreabilidade mínima | 0 |

## KPIs de LLMOps

| Métrica | Definição | Meta inicial |
| --- | --- | --- |
| Custo por workflow | Custo médio de modelos e ferramentas por execução | Teto por caso de uso |
| Taxa de fallback | Percentual de chamadas redirecionadas por erro, custo ou risco | Monitorar por modelo |
| Latência p95 | Tempo de resposta no percentil 95 | Definir por workflow |
| Escalation rate | Percentual de tarefas que precisam de modelo maior ou humano | Reduzir com evidência |
| Cache hit rate | Percentual de respostas aproveitadas com segurança | Aumentar sem afetar qualidade |

## SLAs do piloto

- Disponibilidade alvo em staging/piloto: 95% durante janelas combinadas.
- Resposta a SEV1: imediata após detecção.
- Resposta a SEV2: mesmo dia útil.
- Revisão de métricas: semanal.
