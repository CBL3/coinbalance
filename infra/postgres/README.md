# PostgreSQL — CoinBalance

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de infraestrutura

O PostgreSQL é o banco principal da Fase 1 / 0.2.0-alpha. Dados críticos devem nascer com:

- `organization_id`, quando aplicável;
- timestamps;
- trilha de auditoria;
- soft delete para entidades críticas;
- versionamento ou histórico quando necessário.
