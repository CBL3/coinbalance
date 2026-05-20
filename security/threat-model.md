# Modelo Inicial de Ameaças

Data: 2026-05-20
Versão: 0.3.0-alpha
Status: Inicial  
Classificação: Documento interno de segurança

## Escopo

Fase 2 da CoinBalance: ingestão e reconciliação informacional inicial com backend Flask modular, API versionada (`/api/v1/health`, `/api/v1/identity/me`, `/api/v1/audit/events`, `/api/v1/evidence`, `/api/v1/reconciliation/run`, `/api/v1/reconciliation/findings`) e políticas de segurança.

## Ativos

- Manifesto Primordial.
- Documentação institucional.
- Código da API.
- Versionamento e changelog.
- Políticas de segurança e compliance.
- Futuras trilhas de auditoria e evidências.

## Ameaças iniciais

| Ameaça | Impacto | Mitigação inicial |
| --- | --- | --- |
| Uso de linguagem regulada indevida | Risco jurídico e comercial | Linguagem controlada e checklist |
| Exposição de segredos | Comprometimento de ambientes | `.gitignore`, `.env.example`, política de segredos |
| Endpoint sem versão | Quebra de compatibilidade futura | `/api/v1/health` |
| Falta de rastreabilidade documental | Perda de memória institucional | ADRs e changelog |
| Dependência vulnerável | Risco de supply chain | Varredura e revisão de dependências |
| Crescimento sem arquitetura | Dívida técnica | Monólito modular e ADRs |

## Fora do escopo atual

- Operações financeiras reguladas, custódia, liquidação ou compensação.
- Reconciliação autônoma de saldos e fechamento contábil pleno.

Esses itens permanecem fora do escopo na fase `0.3.0-alpha`, que se concentra em ingestão controlada, evidências trianguladas e registro de findings de reconciliação.
