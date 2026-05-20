# Organização do Repositório

Data: 2026-05-20  
Versão: 0.2.0-alpha  
Status: Vigente  
Classificação: Documento interno de governança documental

## Regra de raiz

A raiz deve conter apenas artefatos de entrada, configuração e execução:

- `README.md`, `MANIFESTO_PRIMORDIAL.md`, `VERSION`, `CHANGELOG.md`, `PACKAGE_MANIFEST.json`.
- Configuração: `.env.example`, `.gitignore`, `pyproject.toml`, `docker-compose.yml`.
- Diretórios operacionais: `backend/`, `migrations/`, `frontend/`, `infra/`, `security/`, `compliance/`, `docs/`, `.github/`.

Documentos de trabalho não devem ficar soltos na raiz.

## Diretórios canônicos

| Diretório | Uso |
| --- | --- |
| `backend/` | API Flask, modelos, testes e dependências do backend |
| `migrations/` | Migrations Alembic/Flask-Migrate do schema relacional |
| `frontend/` | Placeholder e futura camada de interface |
| `infra/` | Docker, PostgreSQL, Nginx e infraestrutura local |
| `security/` | Segurança operacional, segredos, threat model e incident response |
| `compliance/` | Checklists e controles ativos de compliance |
| `docs/2026/05/` | Registros temporais da Fase 0 |
| `docs/adr/` | Architecture Decision Records |
| `docs/institutional/` | Posicionamento, cláusulas institucionais e resiliência |
| `docs/architecture/` | Arquitetura técnica, orquestração e matriz de modelos |
| `docs/product/` | Produto, MVP e gêmeo digital |
| `docs/telemetry/` | Schemas, pipelines, auditoria e telemetria |
| `docs/governance/` | Governança de IA e políticas institucionais |
| `docs/commercial/` | Pilotos comerciais, contrato e ROI |
| `docs/roadmap/` | Roadmap, KPIs e SLAs |
| `docs/project/` | Kickoff, participantes e coordenação |
| `docs/administrative/` | Contatos e arquivos administrativos |

## Convenções

- Usar nomes de arquivo em kebab-case, sem espaços.
- Preferir caminhos ASCII para novos arquivos.
- Manter documentos temporais em `docs/YYYY/MM/`.
- Criar ADR para decisão difícil de reverter.
- Evitar duplicar o mesmo documento em mais de um lugar, exceto manifesto canônico e cópia temporal aprovada.
- Não commitar caches, bytecode, diretórios temporários, `.env` ou artefatos locais.

## Sanitização aplicada

As pastas numeradas exploratórias foram migradas:

- `00 Kickoff/` -> `docs/project/kickoff/`
- `01 Arquitetura/` -> `docs/architecture/`
- `02 MVP Gêmeo Digital/` -> `docs/product/digital-twin-mvp/`
- `03 Dados e Telemetria/` -> `docs/telemetry/`
- `04 Governança e Compliance/` -> `docs/governance/` e `security/`
- `05 Pilotos Comerciais/` -> `docs/commercial/pilots/`
- `06 Roadmap e Métricas/` -> `docs/roadmap/`
- `99 Arquivos Administrativos/` -> `docs/administrative/`
- `RESILIENCIA_INSTITUCIONAL.md` -> `docs/institutional/resiliencia-institucional.md`
