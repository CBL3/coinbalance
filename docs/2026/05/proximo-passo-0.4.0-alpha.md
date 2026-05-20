# Próximo passo: 0.4.0-alpha — Reconciliação

Data: 2026-05-20
Versão: 0.4.0-alpha
Status: Proposto  
Classificação: Documento interno de planejamento

## Objetivo

Iniciar a fase de reconciliação informacional com regras, execuções e findings analisáveis, preservando o anti-escopo regulado e garantindo auditoria por organização.

## Contexto

A versão `0.3.0-alpha` já entregou a fundação de ingestão de evidências, controles de permissão e auditoria de ações. A próxima etapa deve evoluir essa base para capturar divergências, avaliar severidade e suportar revisão humana.

## Entregas principais

- Modelos e endpoints para:
  - `ReconciliationRule`
  - `ReconciliationRun`
  - `ReconciliationFinding`
- Ciclo de findings:
  - criação de regra
  - execução de reconciliação
  - registro de divergência
  - status de tratamento (`new`, `investigating`, `resolved`, `ignored`)
  - auditoria de cada etapa
- Versionamento de regras e histórico de execução.
- UI/endpoint de listagem de findings por organização.
- Testes automatizados de RBAC, escopo organizacional e auditoria.

## Escopo

Inclui:

- avaliação informacional de divergências de dados
- classificação de severidade e status
- registros de responsáveis e evidências associadas
- auditoria de execução e leitura
- preservação do anti-escopo regulado (sem movimentação de ativos, sem pagamento/compensação, sem custódia)

Fora do escopo:

- ações financeiras automáticas
- liquidação ou liquidação de saldos em sistemas externos
- custódia de ativos
- conformidade regulatória plena sem revisão jurídica adicional

## Critérios de sucesso

- endpoints de reconciliação entregues e documentados
- testes cobrindo:
  - criação de regra
  - execução de reconciliação
  - leitura de findings por organização
  - proteção por permissões e escopo
- auditoria persistente de cada operação de reconciliação
- versão do projeto alinhada a `0.4.0-alpha` após entrega

## Implementação inicial

- `ReconciliationRule` para regras de revisão e severidade padrão.
- `ReconciliationRun` para execuções de regras e histórico de resultados.
- Registro de `ReconciliationFinding` a partir de execuções de reconciliação.
- Auditoria de criação de regras e execuções por organização.
- Endpoints de listagem de regras, execuções e findings.

## Marco imediato

1. Definir esquema de dados de regra, execução e finding.
2. Implementar API de criação de regras e execução de reconciliação.
3. Registrar eventos de auditoria para cada operação.
4. Criar testes de integração para fluxo completo.
5. Atualizar documentação de API, roadmap e threat model.

## Observação de segurança

A reconciliação deve atuar como um serviço informacional e investigativo. Qualquer fluxo que possa ser interpretado como ato material ou financeiro exige ADR separado e revisão de compliance.
