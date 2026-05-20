# Changelog

Todas as mudanças relevantes da CoinBalance devem ser registradas neste arquivo.

O projeto segue Semantic Versioning 2.0.0.

## [Não lançado]

### Corrigido

- Reescopo do antigo ledger técnico para diário de integridade por hash, removendo vocabulário de transação financeira incompatível com o anti-escopo regulado.
- Inclusão explícita de `PyJWT` nas dependências do backend.
- Correção do caminho de bootstrap do seed fundacional de identidade quando executado diretamente.

### Adicionado

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
