# Relatório de Engenharia Reversa — Artefato Fase 0

Data: 2026-05-19  
Artefato analisado: `coinbalance-fase-0-manifesto-primordial (1).zip`  
Status: Histórico  
Classificação: Documento interno técnico

## Objetivo

Aplicar engenharia reversa ao pacote fundacional recebido, identificar sua estrutura real, comparar com a base local e atualizar o projeto sem perder os documentos estratégicos já produzidos.

## Achados

O pacote não continha apenas o Manifesto Primordial. Ele trazia uma árvore técnica mais completa:

- `backend/` com Flask application factory, blueprints, configuração, extensões, testes e modelos iniciais.
- `infra/` com Dockerfile de backend e placeholders de PostgreSQL/Nginx.
- `.github/workflows/ci.yml` com pipeline inicial.
- `pyproject.toml` com configuração de pytest e Ruff.
- `PACKAGE_MANIFEST.json` com inventário e roadmap de versões.
- Documentos institucionais adicionais em `docs/institutional`.
- Cópia temporal do manifesto em `docs/2026/05/manifesto-primordial.md`.

## Delta aplicado

- A estrutura oficial do backend passou a ser `backend/app`.
- A execução local passou a instalar `backend/requirements.txt`.
- O Docker Compose passou a subir backend, PostgreSQL e Redis.
- O endpoint `/api/v1/health` foi preservado e enriquecido com metadados institucionais.
- O endpoint `/api/v1/institutional/scope` foi integrado como superfície explícita do anti-escopo regulado.
- A suíte de testes foi movida para o padrão `backend/tests`.
- A documentação institucional do ZIP foi incorporada.
- Os pins rígidos de dependências do backend foram convertidos em faixas compatíveis, porque `psycopg-binary==3.2.3` não instala no Python local 3.14.

## Preservado da base local

Os documentos estratégicos criados antes da importação foram mantidos e posteriormente sanitizados para a estrutura canônica:

- `docs/institutional/resiliencia-institucional.md`
- `docs/architecture/`
- `docs/product/digital-twin-mvp/`
- `docs/telemetry/`
- `docs/governance/`
- `security/incident-response-playbook.md`
- `docs/commercial/pilots/`
- `docs/roadmap/`
- `docs/project/kickoff/`
- `docs/administrative/`

Esses artefatos agora funcionam como camada de visão, LLMOps, resiliência e piloto comercial sobre a Fase 0 técnica.

## Decisão de integração

Adotar a árvore técnica do ZIP como canônica para a Fase 0, mantendo as extensões estratégicas locais como documentação complementar. Essa decisão reduz ambiguidade entre protótipo técnico, governança institucional e visão de evolução.

## Próximas recomendações

- Rodar testes com `python -m pytest` após instalar `backend/requirements.txt`.
- Validar `docker compose up --build` com `.env` criado a partir de `.env.example`.
- Na próxima versão, iniciar `0.2.0-alpha` com RBAC, organizações e `AuditEvent` persistente.
