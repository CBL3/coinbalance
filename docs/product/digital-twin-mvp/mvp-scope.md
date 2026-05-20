# Escopo do MVP

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de produto

## Objetivo

Construir um Gêmeo Digital operacional capaz de representar um processo crítico da CoinBalance, simular decisões, registrar trilhas de auditoria e reconstruir estado lógico após falhas sem perda de integridade.

## Fluxo crítico

Onboarding e acompanhamento de cliente piloto:

1. Receber dados iniciais e documentos.
2. Classificar perfil, risco, pendências e próximos passos.
3. Extrair campos relevantes de contratos ou artefatos operacionais.
4. Gerar plano de ação e checklist auditável.
5. Simular impacto em KPIs antes de qualquer ação material.
6. Registrar decisões e feedback em telemetria.

## Agentes

- Agente de Dados: valida schema, qualidade, completude, PII e origem.
- Agente de Contratos: extrai obrigações, riscos, SLAs e exceções.
- Agente de Processo: mantém o estado do Gêmeo Digital e sugere próximos passos.
- Agente de Segurança: aplica políticas, bloqueia ações fora de escopo e exige aprovação.
- Agente de Observabilidade: consolida eventos, custos, latência, confiança e incidentes.

## Critérios de aceitação

- Todo workflow gera `trace_id` único e auditável.
- Toda ação material tem justificativa, evidência e política associada.
- Dados sensíveis são classificados antes de entrar em prompts.
- O sistema consegue replay de eventos para reconstruir estado do piloto.
- Falha de modelo proprietário aciona fallback ou fila sem perda de estado.
- Painel mínimo mostra tempo para valor, precisão operacional, adoção, MTTR e custo por workflow.
- Demo executa em staging com massa de dados sintética.

## Fora do escopo do MVP

- Treinamento próprio de modelo fundacional.
- Execução autônoma de transações financeiras irreversíveis.
- Marketplace de agentes.
- Suporte completo multi-tenant sem piloto controlado.

## Prazo

6 a 8 semanas para MVP demonstrável, com pilotos controlados e sem prometer autonomia total antes de evidência operacional.
