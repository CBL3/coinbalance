# Checklist de Novas Funcionalidades

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno de compliance

Antes de implementar qualquer funcionalidade, responder:

- A funcionalidade movimenta, custodia, liquida, inicia pagamento, intermedeia operação ou emite ativo?
- A funcionalidade pode ser interpretada como saldo garantido, ordem financeira, câmbio, investimento ou prestação regulada?
- A funcionalidade usa dados sensíveis, regulados ou de terceiros?
- A funcionalidade exige autenticação, autorização, RBAC ou segregação por organização?
- A funcionalidade gera evento auditável?
- Há evidência, hash, origem e responsável quando aplicável?
- Há impacto no changelog?
- Há decisão difícil de reverter que exige ADR?
- Há necessidade de atualizar a matriz de riscos e controles?
- Há teste automatizado ou critério de aceite verificável?

## Regra de bloqueio

Se qualquer resposta indicar aproximação com atividade regulada, a implementação deve ser suspensa até análise jurídica, ADR e segregação arquitetural.
