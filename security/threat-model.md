# Modelo Inicial de Ameaças

Data: 2026-05-19  
Versão: 0.1.0-alpha  
Status: Inicial  
Classificação: Documento interno de segurança

## Escopo

Fase 0 da CoinBalance: documentação fundacional, backend Flask mínimo, API `/api/v1/health`, políticas e estrutura de evolução.

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

- Autenticação real.
- RBAC.
- Persistência de auditoria.
- Upload de dados.
- Reconciliação funcional.

Esses itens entram a partir das fases `0.2.0-alpha` e `0.3.0-alpha`.
