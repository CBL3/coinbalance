# Política de Desenvolvimento Seguro

Data: 2026-05-19  
Versão: 0.1.0-alpha  
Status: Vigente  
Classificação: Documento interno de segurança

## Objetivo

Definir controles mínimos para desenvolvimento seguro da CoinBalance desde a Fase 0.

## Controles mínimos

- Revisão de código antes de merge.
- Testes automatizados para comportamento crítico.
- Gestão de segredos fora do código.
- Varredura de dependências.
- Logs estruturados e sem dados sensíveis desnecessários.
- Separação de ambientes.
- Documentação de decisões arquiteturais por ADR.
- Checklist de risco para novas funcionalidades.

## Regras de implementação

- Nenhuma funcionalidade regulada pode ser implementada sem ADR e análise jurídica.
- Nenhum segredo pode ser commitado.
- Dados sensíveis devem ser classificados antes de persistência, log ou envio a terceiros.
- Operações destrutivas devem ser idempotentes, auditáveis e protegidas por autorização.

## Evidências

- Pull requests revisados.
- Relatórios de testes.
- Changelog atualizado.
- ADRs aprovados.
- Registro de riscos e controles.
