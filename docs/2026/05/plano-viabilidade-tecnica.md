# Plano de Viabilidade Técnica

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno técnico

## Objetivo

Validar a viabilidade técnica da CoinBalance como plataforma auditável de inteligência operacional e reconciliação informacional, começando por uma API mínima, documentação fundacional, políticas de segurança e estrutura de evolução rastreável.

## Hipóteses

- Um monólito modular é suficiente para a Fase 0 e reduz complexidade operacional.
- Flask permite implementar uma API mínima com baixo custo e rápida evolução.
- PostgreSQL será o banco relacional alvo para as próximas fases, especialmente por consistência, transações e rastreabilidade.
- A arquitetura deve nascer sem funcionalidade regulada.

## Entregas da Fase 0

- Manifesto Primordial.
- README, VERSION e CHANGELOG.
- ADRs 001 a 004.
- Políticas iniciais de segurança e compliance.
- Backend Flask mínimo.
- Endpoint `/api/v1/health`.
- Docker Compose.
- Teste automatizado do health check.

## Critérios de sucesso

- API responde com metadados institucionais e versão.
- Anti-escopo regulado aparece em documentação e resposta operacional.
- Estrutura documental segue `docs/YYYY/MM` e `docs/adr`.
- Novas funcionalidades têm checklist de risco antes da implementação.

## Atualização 2026-05-20

A versão `0.2.0-alpha` introduziu usuários, organizações, papéis, permissões, RBAC, `AuditEvent` persistente, migration inicial e testes de isolamento organizacional.

## Próxima fase técnica

A versão `0.3.0-alpha` deve iniciar fontes de dados e ingestão controlada, mantendo classificação de dados, hashes, logs de importação e auditoria por organização.
