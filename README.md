# CoinBalance

**Versão atual:** `0.4.0-alpha`  
**Status:** Fase 2 — Ingestão e reconciliação informacional inicial  
**Classificação:** Documento estratégico interno / scaffold técnico inicial
**Padrão documental:** [docs/documentation-standard.md](docs/documentation-standard.md)

CoinBalance é uma plataforma tecnológica de inteligência operacional, governança algorítmica, rastreabilidade, reconciliação informacional de dados, evidências, visualização executiva e suporte à decisão.

Este repositório segue o [Manifesto Primordial](MANIFESTO_PRIMORDIAL.md) e incorpora o pacote fundacional analisado em [relatorio-engenharia-reversa-artefato-fase-0.md](docs/2026/05/relatorio-engenharia-reversa-artefato-fase-0.md).

## Anti-escopo regulado

Nesta fase, a CoinBalance não movimenta recursos, não custodia ativos, não intermedeia operações, não liquida transações, não inicia pagamentos, não emite ativos virtuais e não substitui instituições reguladas.

Qualquer aproximação com atividade regulada exige ADR próprio, análise jurídica, matriz de riscos, segregação arquitetural e documentação específica.

## Decisões estruturantes

- Raiz permanente do projeto: `coinbalance/`
- Versão atual do software: `0.3.0-alpha`
- Versionamento do software: SemVer 2.0.0
- Documentação institucional e evidências: `docs/YYYY/MM/`
- ADRs: `docs/adr/`
- API inicial: `/api/v1/`
- Novos endpoints de reconciliação: `/api/v1/reconciliation/rules`, `/api/v1/reconciliation/runs`, `/api/v1/reconciliation/findings`, `/api/v1/reconciliation/run`

## Stack inicial

- Backend: Flask application factory em `backend/app`.
- Persistência alvo: PostgreSQL.
- Extensões preparadas: Flask-SQLAlchemy e Flask-Migrate.
- Migrations iniciais: Alembic/Flask-Migrate em `migrations/`.
- Infra local: Docker Compose com backend, PostgreSQL e Redis.
- CI: GitHub Actions em `.github/workflows/ci.yml`.
- Documentação: `docs/YYYY/MM`, `docs/adr`, `security`, `compliance`.
- Scaffolds técnicos: autenticação JWT/RBAC, diário de integridade por hash e interface HAL.

## Execução local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
$env:DATABASE_URL='sqlite:///:memory:'
$env:COINBALANCE_VERSION='0.4.0-alpha'
python -m flask --app backend/wsgi.py run --host 127.0.0.1 --port 8000
```

Health check:

```text
GET http://127.0.0.1:8000/api/v1/health
```

Resposta esperada:

```json
{
  "service": "coinbalance-api",
  "status": "ok",
  "version": "0.4.0-alpha",
  "api_version": "v1",
  "regulated_activity": false
}
```

Escopo institucional:

```text
GET http://127.0.0.1:8000/api/v1/institutional/scope
```

Identidade autenticada:

```text
GET http://127.0.0.1:8000/api/v1/identity/me
Authorization: Bearer <jwt>
```

Eventos de auditoria por escopo organizacional:

```text
GET http://127.0.0.1:8000/api/v1/audit/events
Authorization: Bearer <jwt>
```

Interface HAL para eventos operacionais de hardware:

```text
POST http://127.0.0.1:8000/api/v1/hardware/interface
```

Payload mínimo:

```json
{
  "hardware_id": "XYRON-001",
  "event_type": "NFC_READ",
  "payload": {
    "tag_id": "04:XX:YY:ZZ"
  }
}
```

A interface aceita eventos operacionais agnósticos para ingestão futura. Ela não executa operação material, financeira ou transacional.

## Docker Compose

```powershell
Copy-Item .env.example .env
docker compose up --build
```

## Estrutura

```text
backend/                  API Flask, módulos de domínio e testes
migrations/               Migrations Alembic/Flask-Migrate
frontend/                 Placeholder controlado para camada futura
infra/                    Docker, PostgreSQL e Nginx
docs/2026/05/             Documentos temporais fundacionais
docs/adr/                 Registros de decisões arquiteturais
security/                 Políticas e modelo de ameaças
compliance/               Controles de linguagem, dados e novas funcionalidades
docs/architecture/        Arquitetura de agentes, LLMOps e resiliência
docs/product/             Escopo do MVP e produto
docs/telemetry/           Pipeline e schema de eventos
docs/governance/          Políticas institucionais de IA e governança
docs/commercial/          Pilotos, contratos e ROI
docs/roadmap/             Roadmap, KPIs e métricas
docs/project/             Kickoff e coordenação
docs/administrative/      Contatos e arquivos administrativos
```

Mapa completo: [docs/repository-organization.md](docs/repository-organization.md).

## Referências normativas e técnicas

- Semantic Versioning 2.0.0: https://semver.org/
- Flask Application Factories: https://flask.palletsprojects.com/en/stable/patterns/appfactories/
- Flask Blueprints: https://flask.palletsprojects.com/en/stable/blueprints/
- NIST SSDF SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
