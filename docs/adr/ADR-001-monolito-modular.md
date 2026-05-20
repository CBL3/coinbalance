# ADR-001: Monólito modular

Status: Aprovado  
Data: 2026-05-20

## Contexto

A CoinBalance está na Fase 0 e precisa validar fundamentos institucionais, API mínima, segurança, documentação e governança sem carregar complexidade operacional prematura.

## Decisão

Adotar monólito modular como arquitetura inicial.

## Justificativa

Um monólito modular permite evoluir domínios como organizações, auditoria, ingestão, reconciliação, evidências, riscos e controles com fronteiras internas claras, mas sem custo inicial de microsserviços.

## Alternativas consideradas

- Microsserviços desde o início.
- Aplicação serverless fragmentada.
- Protótipo sem fronteiras modulares.

## Consequências

- Menor complexidade de deploy na Fase 0.
- Necessidade de disciplina modular no código.
- Possibilidade de extração futura de módulos quando houver escala ou exigência operacional.

## Riscos relacionados

- Acoplamento excessivo se fronteiras internas não forem respeitadas.
- Crescimento desordenado se módulos não tiverem owners.
