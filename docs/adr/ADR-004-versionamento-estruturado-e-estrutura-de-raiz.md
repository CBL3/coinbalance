# ADR-004: Versionamento estruturado e estrutura de raiz

Status: Aprovado  
Data: 2026-05-20

## Contexto

A CoinBalance precisa separar versionamento de software, documentação temporal, API e decisões arquiteturais.

## Decisão

Adotar:

- Semantic Versioning para software.
- `VERSION` na raiz.
- `CHANGELOG.md` para mudanças.
- `/api/v1/` para contrato de API.
- `docs/YYYY/MM/` para documentação temporal.
- `docs/adr/ADR-000-titulo.md` para decisões arquiteturais.
- `coinbalance/` como identidade institucional permanente.

## Justificativa

Separar esses eixos evita confusão entre maturidade do produto, histórico documental, compatibilidade de API e memória decisória.

## Consequências

- Toda mudança material deve atualizar changelog.
- Toda decisão difícil de reverter deve gerar ADR.
- Documentos institucionais não devem ficar dispersos sem data ou contexto.

## Riscos relacionados

- Duplicidade documental.
- Alterações sem rastreabilidade.
- Mistura indevida entre versão de API e versão de software.
