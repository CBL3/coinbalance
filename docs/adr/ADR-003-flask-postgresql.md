# ADR-003: Flask e PostgreSQL

Status: Aprovado  
Data: 2026-05-20

## Contexto

A Fase 0 precisa de backend mínimo, API versionada e caminho claro para persistência transacional nas fases seguintes.

## Decisão

Adotar Flask para a API inicial e PostgreSQL como banco relacional alvo a partir das próximas fases.

## Justificativa

Flask entrega simplicidade e baixo atrito para o endpoint inicial. PostgreSQL é adequado para trilhas de auditoria, relacionamentos entre organizações, evidências, riscos, controles e reconciliações.

## Alternativas consideradas

- FastAPI.
- Django.
- Banco NoSQL como fonte primária.

## Consequências

- A Fase 0 mantém API mínima sem banco obrigatório.
- A Fase 0 deve evitar acoplamento que dificulte migrations futuras.
- A Fase 0 prepara a semântica de API antes da modelagem persistente.

## Riscos relacionados

- Flask sem disciplina pode crescer sem estrutura.
- PostgreSQL exigirá migrations e governança de schema na 0.2.
