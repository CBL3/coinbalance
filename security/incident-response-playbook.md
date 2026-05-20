# Playbook de Incidentes

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de segurança

## Objetivo

Responder rapidamente a falhas de segurança, qualidade, disponibilidade, custo ou governança envolvendo agentes, modelos, dados, integrações e Gêmeo Digital.

## Severidade

| Severidade | Critério | Tempo alvo |
| --- | --- | --- |
| SEV1 | Vazamento, ação irreversível indevida, perda de integridade ou indisponibilidade crítica | Contenção imediata |
| SEV2 | Degradação relevante, falha de fallback, erro de decisão alto risco | Resposta no mesmo dia |
| SEV3 | Erro limitado, custo anômalo, falha de conector sem impacto material | Resposta planejada |
| SEV4 | Quase-incidente, alerta informativo, melhoria de controle | Backlog |

## Identificação

Sinais de alerta:

- Aumento anômalo de custo ou tokens.
- Queda de confiança ou aumento de fallback.
- Prompt injection detectado.
- Acesso negado recorrente.
- Evento sem `trace_id` ou policy version.
- Divergência entre estado reconstruído e estado real.
- Modelo produzindo ação sem evidência suficiente.

## Contenção

1. Congelar o `trace_id` ou workflow afetado.
2. Revogar ferramenta, token ou permissão envolvida.
3. Alternar para modo somente leitura quando houver risco material.
4. Acionar fallback local ou fila assíncrona.
5. Preservar logs, snapshots e artefatos para auditoria.
6. Bloquear treinamento ou reuso de dados do incidente até revisão.

## Comunicação

- SEV1: Sponsor, Tech Lead, Infra, Compliance e cliente afetado conforme contrato.
- SEV2: Tech Lead, PO, Infra e Compliance.
- SEV3/SEV4: owner do serviço e registro em backlog.

Toda comunicação deve separar fato confirmado, hipótese, impacto conhecido, contenção aplicada e próxima atualização.

## Remediação

- Corrigir política, prompt, conector, schema, permissão ou modelo.
- Reexecutar workflow em ambiente seguro quando possível.
- Comparar estado reconstruído com snapshot confiável.
- Validar correção com teste automatizado ou checklist manual.
- Registrar alteração com dono e data.

## Lições aprendidas

Para cada SEV1/SEV2:

- Causa raiz.
- Detecção: como foi percebido e como deveria ser percebido antes.
- Contenção: o que funcionou e o que atrasou.
- Prevenção: controle, teste ou métrica nova.
- Owner e prazo.

## Regra de integridade do "outro lado"

Se o estado reconstruído após falha, migração ou replay não bater com checksum lógico, permissões e evidências esperadas, o sistema não deve continuar a execução. O estado entra em quarentena até revisão humana.
