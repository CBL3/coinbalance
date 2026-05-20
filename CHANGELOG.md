# Changelog

Todas as mudanças relevantes da CoinBalance devem ser registradas neste arquivo.

O projeto segue Semantic Versioning 2.0.0.

## [0.4.0-alpha] - 2026-05-20

### Adicionado

- Modelos iniciais `ReconciliationRule` e `ReconciliationRun` para suportar regras de reconciliação e execuções.
- Endpoints de criação e listagem de regras (`/api/v1/reconciliation/rules`) e execuções (`/api/v1/reconciliation/runs`).
- Fluxo de execução de reconciliação que persiste `ReconciliationRun` e `ReconciliationFinding` e grava auditoria associada.
- Testes de permissão, escopo organizacional e auditoria para regras e execuções de reconciliação.

## [0.3.0-alpha] - 2026-05-20

### Adicionado

- Endpoints de ingestão de evidências e execução de reconciliação (`/api/v1/evidence`, `/api/v1/reconciliation/run`, `/api/v1/reconciliation/findings`).
- Permissões RBAC para `evidence:upload`, `reconciliation:run` e `reconciliation:read`.
- Serialização de domínios `Evidence` e `ReconciliationFinding`.
- Auditoria de upload de evidência e execução de reconciliação via `AuditEvent`.
- Testes de permissão e escopo organizacional para ingestão e reconciliação.

### Atualizado

- Versão do projeto para `0.3.0-alpha`.
- Documentação principal e arquitetura para refletir o novo escopo de ingestão e reconciliação.

### Corrigido

- Ajustes de fluxo de autorização para organização no upload de evidência e execução de reconciliação.

## [0.2.0-alpha] - 2026-05-20

### Adicionado

- Migration inicial Alembic/Flask-Migrate para organizações, usuários, papéis, permissões, auditoria, evidências, reconciliação e diário de integridade.
- Endpoint autenticado `/api/v1/identity/me`.
- Endpoint protegido `/api/v1/audit/events` com RBAC e isolamento por organização.
- Helpers de permissão, escopo organizacional e serialização para `User`, `Role`, `Permission` e `Organization`.
- Registro persistente de `AuditEvent` via `AuditEvent.record_event`.
- Testes de autenticação, autorização, isolamento organizacional e acesso administrativo.
- ADR-005 para identidade, RBAC e auditoria persistente.

### Corrigido

- Reescopo do antigo ledger técnico para diário de integridade por hash, removendo vocabulário de transação financeira incompatível com o anti-escopo regulado.
- Inclusão explícita de `PyJWT` nas dependências do backend.
- Correção do caminho de bootstrap do seed fundacional de identidade quando executado diretamente.

### Mantido

- Testes do diário de integridade.
- Documentação inicial da interface HAL em `README.md`.
- Atualização do manifesto de pacote para refletir os arquivos técnicos presentes.

## [0.1.0-alpha] - 2026-05-19

### Adicionado

- Manifesto Primordial como documento fundacional da Fase 0.
- README, VERSION e CHANGELOG.
- Estrutura documental `docs/YYYY/MM`, `docs/adr`, `docs/institutional` e `docs/compliance`.
- ADRs 001 a 004.
- Políticas iniciais de segurança e compliance.
- Backend Flask mínimo em estrutura canônica `backend/app`.
- Endpoint `/api/v1/health`.
- Endpoint `/api/v1/institutional/scope`.
- Docker Compose com backend, PostgreSQL e Redis.
- CI inicial com GitHub Actions.
- `pyproject.toml` com configuração de testes.
- Modelos iniciais de domínio: `User`, `Organization`, `Evidence`, `ReconciliationFinding` e `AuditEvent`.
- Relatório de engenharia reversa do pacote fundacional.
- Sanitização da raiz: documentos exploratórios migrados para a taxonomia canônica em `docs/`.
- Mapa de organização do repositório em `docs/repository-organization.md`.
- Padrão de documentação vigente em `docs/documentation-standard.md`.

### Segurança

- Anti-escopo regulado formalizado.
- Política de segredos fora do código.
- Modelo inicial de ameaças.
- Checklist de novas funcionalidades com gatilho regulatório.
- Health check expõe `regulated_activity=false`.
