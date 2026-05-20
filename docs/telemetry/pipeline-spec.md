# Especificação do pipeline de telemetria, RLHF/RLAIF e auditoria

Data: 2026-05-19  
Versão: 0.1.0-alpha  
Status: Inicial  
Classificação: Documento interno de arquitetura e dados

## Objetivo

Registrar eventos suficientes para reconstruir decisões, medir qualidade, controlar custo, alimentar avaliações e permitir melhoria contínua sem vazar dados sensíveis.

Schema canônico: [event-schema.json](event-schema.json).

## Fontes

- API Gateway: autenticação, tenant, rate limit, payload validado.
- Orquestrador: workflow, agentes chamados, ferramentas, políticas e fallback.
- Model Router: modelo escolhido, motivo, custo, latência e confiança.
- Agentes: entrada sanitizada, saída, evidências, validações e bloqueios.
- Usuários: feedback, aprovação, rejeição e correções.
- Sistemas externos: status de integração, erros, reconciliação e confirmações.

## Storage

- Eventos brutos: append-only, imutável, retenção definida por política.
- Eventos sanitizados: base analítica para dashboard e avaliação.
- Artefatos sensíveis: storage criptografado com referência por hash, não colado em prompts sem política.
- On-prem: armazenamento local com exportação apenas de métricas agregadas e aprovadas.

## Processos

1. Ingestão
   - Recebe eventos no schema versionado.
   - Rejeita eventos sem `trace_id`, `tenant_id`, `event_type` ou timestamp válido.

2. Validação
   - Confere schema, política, classificação de dados e idempotência.
   - Marca eventos suspeitos para quarentena.

3. Enriquecimento
   - Adiciona custo, latência, versão de prompt, versão de política e hash de evidência.

4. Métricas
   - Consolida KPIs operacionais, segurança, custo e qualidade.

5. Feedback
   - Captura aprovação, rejeição, correção humana e outcome real.
   - Separa feedback de treinamento, avaliação e auditoria.

6. RLAIF/RLHF
   - RLAIF para avaliação automática de aderência a políticas e qualidade textual.
   - RLHF apenas com dados aprovados, anonimizados e com consentimento/política.
   - Nenhum dado sensível entra em treinamento sem autorização explícita.

7. Cadência de melhoria
   - Avaliações semanais no MVP.
   - Revisão mensal de roteamento de modelos.
   - Retreinamento/fine-tuning somente após dataset aprovado e baseline mensurado.

## Sinais mínimos

- Taxa de conclusão por workflow.
- Taxa de fallback.
- Custo médio por workflow e por tenant.
- Latência p50/p95.
- Precisão operacional validada.
- Erros por conector.
- Incidentes, quase-incidentes e bloqueios por política.
- Reversões e tempo de recuperação.
