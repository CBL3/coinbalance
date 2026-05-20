# Relatório de Sanitização Documental

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Histórico  
Classificação: Documento interno de governança documental

## Objetivo

Registrar a sanitização das documentações da CoinBalance após a consolidação da Fase 0 e da estrutura canônica do repositório.

## Escopo

Foram revisados documentos na raiz, em `docs/`, `security/`, `compliance/`, `infra/` e `frontend/`.

## Ações aplicadas

- Criação do padrão vigente em `docs/documentation-standard.md`.
- Atualização do índice documental em `docs/README.md`.
- Normalização do mapa em `docs/repository-organization.md`.
- Padronização de metadados em documentos operacionais: `Data`, `Versão`, `Status` e `Classificação`.
- Atualização de documentos que ainda descreviam o projeto como não executável.
- Normalização de grafia institucional para `CoinBalance`.
- Correção da matriz de modelos para reforçar reconciliação informacional, sem validação patrimonial ou saldo.
- Atualização de referências internas para caminhos canônicos.
- Atualização de `PACKAGE_MANIFEST.json` e `CHANGELOG.md`.

## Documentos históricos preservados

O Manifesto Primordial e sua cópia temporal foram preservados como documentos fundacionais. Registros históricos podem citar nomes antigos de pastas quando o objetivo for explicar a migração.

## Resultado

A documentação agora separa:

- norma vigente;
- registro histórico;
- arquitetura alvo;
- produto;
- telemetria;
- segurança;
- compliance;
- governança;
- comercial;
- roadmap;
- coordenação de projeto.

## Critério de aceite

- Todos os documentos ativos possuem localização canônica.
- Os documentos operacionais principais possuem metadados.
- Não há placeholders genéricos pendentes.
- O manifesto de pacote representa a árvore atual.
- Testes e schemas continuam válidos.
