# Padrão de Documentação

Data: 2026-05-20  
Versão: 0.2.0-alpha  
Status: Vigente  
Classificação: Documento interno de governança documental

## Objetivo

Definir o padrão de criação, revisão, localização e linguagem dos documentos da CoinBalance.

## Metadados mínimos

Documentos novos devem declarar, no início:

- Data.
- Versão do projeto ou versão do documento.
- Status.
- Classificação.
- Owner ou área responsável, quando aplicável.

ADRs seguem formato próprio e devem manter `Status` e `Data`.

## Status permitidos

- `Vigente`: documento operacional em uso.
- `Fundacional`: documento base aprovado para a Fase 0.
- `Histórico`: registro preservado, mas não usado como regra atual.
- `Inicial`: documento válido, ainda sujeito a expansão.
- `Substituído`: documento mantido apenas por rastreabilidade.

## Classificação

- `Público`: pode ser compartilhado externamente sem restrição.
- `Interno`: uso interno geral.
- `Confidencial`: estratégia, arquitetura, risco, cliente ou controles internos.
- `Restrito`: segredos, credenciais, dados sensíveis ou material crítico.

## Linguagem

Usar a linguagem controlada definida em `compliance/linguagem-permitida-proibida.md`.

Termos próximos de atividade regulada só devem aparecer em:

- Manifesto Primordial.
- ADR-002.
- Documentos explícitos de anti-escopo.
- Checklists de compliance.
- Registros históricos com contexto claro.

## Localização

Usar o mapa oficial em `docs/repository-organization.md`.

Documentos soltos na raiz são exceção e devem ser limitados a:

- `README.md`
- `MANIFESTO_PRIMORDIAL.md`
- `CHANGELOG.md`
- `VERSION`
- `PACKAGE_MANIFEST.json`

## Convenções de nome

- Usar kebab-case.
- Evitar espaços em nomes novos.
- Preferir ASCII em caminhos novos.
- Manter cópias temporais em `docs/YYYY/MM/`.

## Revisão

Toda mudança relevante de documentação deve:

- Atualizar o changelog quando afetar a organização do projeto.
- Atualizar `PACKAGE_MANIFEST.json` quando criar, mover ou remover arquivo relevante.
- Atualizar links internos impactados.
- Preservar histórico quando a mudança tiver valor de auditoria.
