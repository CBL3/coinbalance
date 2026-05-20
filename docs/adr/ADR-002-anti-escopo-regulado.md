# ADR-002: Anti-escopo regulado

Status: Aprovado  
Data: 2026-05-19

## Contexto

A CoinBalance usa termos próximos a domínios financeiros, mas seu propósito inicial é inteligência operacional, governança, rastreabilidade, reconciliação informacional, evidências e suporte à decisão.

## Decisão

Formalizar que a Fase 0 não implementa, vende ou demonstra funcionalidades de atividade regulada.

## Justificativa

O anti-escopo reduz risco jurídico, reputacional e arquitetural. A plataforma deve amadurecer como infraestrutura de confiança antes de qualquer aproximação com camadas reguladas.

## Regras

- Não movimentar recursos.
- Não custodiar ativos.
- Não iniciar pagamentos.
- Não intermediar operações.
- Não liquidar transações.
- Não emitir ativos virtuais.
- Não representar saldo garantido.

## Consequências

- Linguagem comercial e técnica deve ser controlada.
- Funcionalidades próximas de domínio regulado exigem novo ADR e análise jurídica.
- O health check e documentação devem comunicar o escopo não regulado.

## Riscos relacionados

- Pressão comercial por atalhos.
- Ambiguidade terminológica.
- Demonstrações que pareçam execução financeira.
