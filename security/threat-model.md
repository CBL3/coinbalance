# Modelo Inicial de Ameaças

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de segurança

## Escopo

Fase 1 da CoinBalance: identidade, RBAC e auditoria persistente sobre backend Flask modular, API versionada (`/api/v1/health`, `/api/v1/identity/me`, `/api/v1/audit/events`) e políticas de segurança.

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

- Upload de dados.
- Reconciliação funcional.

Esses itens permanecem fora do escopo na fase `0.2.0-alpha` e entrarão a partir da fase `0.3.0-alpha`.
