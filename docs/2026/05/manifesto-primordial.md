# Manifesto Primordial — CoinBalance

**Data:** 19 de maio de 2026  
**Versão do projeto:** 0.1.0-alpha  
**Status:** Aprovado como documento fundacional da Fase 0  
**Classificação:** Documento estratégico interno  
**Natureza:** Manifesto institucional, técnico e operacional primordial  
**Raiz oficial:** `coinbalance/`

---

## 1. Preâmbulo

A CoinBalance nasce como uma plataforma tecnológica de inteligência operacional, governança algorítmica, rastreabilidade, reconciliação informacional, evidências, visualização executiva e suporte à decisão.

Seu propósito primordial é transformar dados dispersos, registros frágeis, processos opacos e decisões não auditáveis em uma infraestrutura verificável de confiança, controle, memória institucional e governança mensurável.

A CoinBalance não nasce para movimentar recursos, custodiar ativos, intermediar operações, liquidar transações, iniciar pagamentos, emitir ativos virtuais ou substituir instituições reguladas.

A CoinBalance nasce para organizar, preservar, reconciliar, evidenciar e iluminar a complexidade operacional.

---

## 2. Princípio de identidade

O nome institucional permanente do projeto é:

```text
coinbalance/
```

A expressão “CoinBalance V2” permanece apenas como referência histórica de reposicionamento, não como raiz técnica, identidade institucional permanente ou namespace principal.

A identidade do projeto deve permanecer estável mesmo quando o software evoluir, a API ganhar novas versões, a documentação acumular ciclos anuais e a arquitetura amadurecer.

---

## 3. Princípio de separação das camadas

A CoinBalance será governada por três camadas conceituais:

1. **Plataforma tecnológica**  
   Camada principal e inicial, voltada a software, APIs, painéis, registros, evidências, logs, trilhas de auditoria, ingestão, reconciliação informacional e suporte à decisão.

2. **Infraestrutura de governança**  
   Camada responsável por políticas, riscos, controles, documentação, papéis, responsabilidades, segurança da informação, continuidade e preservação de conhecimento estratégico.

3. **Atividade eventualmente regulada**  
   Camada condicional, segregada e futura, aplicável apenas se houver análise jurídica específica, controles compatíveis, parceiros autorizados, autorização aplicável e documentação própria.

Nenhuma funcionalidade da Camada 3 poderá ser implementada por inferência, ambiguidade ou pressão comercial.

---

## 4. Princípio de não caracterização regulada

Em sua fase inicial, a CoinBalance não deve ser descrita, vendida, demonstrada, documentada ou implementada como:

- instituição financeira;
- exchange;
- custodiante;
- corretora;
- instituição de pagamento;
- iniciadora de pagamento;
- emissora de ativo virtual;
- emissora de moeda digital;
- prestadora direta de serviço regulado;
- intermediadora financeira;
- participante direto de Pix, SPI ou Open Finance;
- entidade de liquidação;
- operadora de câmbio;
- gestora de recursos;
- operadora de recursos de terceiros.

Qualquer aproximação funcional, comercial ou técnica com esses domínios deverá abrir nova frente regulatória, novo ADR, nova matriz de riscos, análise jurídica própria e segregação arquitetural.

---

## 5. Princípio de versionamento

O software seguirá Semantic Versioning 2.0.0.

A versão inicial da CoinBalance é:

```text
0.1.0-alpha
```

O versionamento do software deve comunicar impacto técnico, compatibilidade e maturidade da entrega.

A documentação, atas, evidências, registros fiscais, relatórios e materiais de auditoria seguirão organização temporal:

```text
docs/YYYY/MM/
```

A API será versionada por contrato técnico:

```text
/api/v1/
```

ADRs permanecerão sequenciais e independentes de ano fiscal ou versão de software:

```text
docs/adr/ADR-000-titulo-da-decisao.md
```

---

## 6. Princípio de auditabilidade

Nenhuma afirmação de governança, segurança, rastreabilidade, evidência ou controle será considerada válida sem registro verificável.

A CoinBalance deve preservar:

- origem dos dados;
- responsáveis;
- datas e horários;
- versões;
- trilhas de auditoria;
- eventos relevantes;
- decisões;
- evidências;
- hashes;
- justificativas;
- relações entre riscos e controles.

A plataforma deve ser construída para permitir reconstrução histórica de eventos críticos.

---

## 7. Princípio de evidência

Toda evidência relevante deve possuir, sempre que aplicável:

- identificador único;
- organização vinculada;
- origem;
- responsável;
- data de criação;
- metadados;
- classificação de sensibilidade;
- hash;
- política de retenção;
- vínculo com risco, controle, decisão ou evento.

Evidência sem contexto é arquivo.  
Evidência com origem, hash, metadados e trilha é governança.

---

## 8. Princípio de reconciliação informacional

A reconciliação da CoinBalance é informacional, operacional e documental.

Ela não representa liquidação financeira, validação patrimonial oficial, custódia, execução de ordem, confirmação de saldo garantido ou movimentação de recursos.

A reconciliação deve identificar:

- divergências;
- lacunas;
- duplicidades;
- inconsistências;
- pendências;
- exceções;
- eventos não tratados;
- necessidade de revisão humana.

Toda divergência relevante deve possuir status, severidade, responsável, histórico e evidência ou justificativa.

---

## 9. Princípio de segurança desde a concepção

A segurança da CoinBalance não será adereço posterior.

Ela deve estar presente na arquitetura, no código, nos testes, nas revisões, nos pipelines, na gestão de dependências, na autenticação, na autorização, na gestão de segredos, nos logs, na observabilidade e na resposta a incidentes.

A Fase 0 reconhece como controles mínimos:

- revisão de código;
- testes automatizados;
- gestão de segredos fora do código;
- varredura de dependências;
- trilhas de auditoria;
- RBAC planejado;
- segregação de ambientes;
- logs estruturados;
- documentação de decisões;
- política de desenvolvimento seguro.

---

## 10. Princípio de governança documental

A CoinBalance deve tratar documentação como ativo de controle, não como subproduto.

Documentos institucionais, técnicos, regulatórios, fiscais, arquiteturais e operacionais devem ser organizados de forma previsível, datada, versionada e auditável.

A estrutura documental primordial é:

```text
docs/
├── 2026/
│   └── 05/
├── adr/
├── institutional/
└── compliance/
```

---

## 11. Princípio de decisão arquitetural registrada

Toda decisão difícil de reverter deverá gerar ADR.

ADRs devem registrar:

- contexto;
- decisão;
- justificativa;
- alternativas consideradas, quando aplicável;
- consequências;
- riscos relacionados;
- status.

A memória arquitetural da CoinBalance deve ser preservada para que decisões futuras possam ser avaliadas à luz do racional original.

---

## 12. Princípio de linguagem controlada

A linguagem institucional da CoinBalance é parte do controle de risco.

Usar preferencialmente:

- plataforma tecnológica;
- inteligência operacional;
- governança algorítmica;
- rastreabilidade;
- reconciliação informacional;
- evidências;
- auditoria operacional;
- visualização executiva;
- suporte à decisão.

Evitar ou condicionar a análise jurídica:

- liquidação;
- custódia;
- exchange;
- corretora;
- pagamento;
- câmbio;
- investimento;
- saldo garantido;
- ordem financeira;
- movimentação de recursos;
- prestação regulada de serviços financeiros.

---

## 13. Princípio de evolução por fases

A evolução da CoinBalance seguirá fases rastreáveis.

### 0.1.0-alpha — Fundação

- raiz `coinbalance/`;
- manifesto primordial;
- README;
- VERSION;
- CHANGELOG;
- ADRs 001–004;
- documentação institucional;
- matriz inicial de riscos;
- backend Flask mínimo;
- Docker Compose;
- API `/api/v1/health`;
- políticas iniciais de segurança.

### 0.2.0-alpha — Identidade, organizações e auditoria

- usuários;
- organizações;
- papéis;
- permissões;
- RBAC;
- AuditEvent integrado;
- migrations;
- testes de isolamento;
- trilhas reais de operações críticas.

### 0.3.0-alpha — Fontes e ingestão

- DataSource;
- DataBatch;
- upload controlado;
- hash de arquivo;
- validação de schema;
- classificação de dados;
- logs de importação.

### 0.4.0-alpha — Reconciliação

- ReconciliationRule;
- ReconciliationRun;
- ReconciliationFinding;
- divergências;
- severidade;
- responsáveis;
- revisão humana;
- histórico de tratamento.

### 0.5.0-beta — Evidências, riscos e controles

- Evidence Vault;
- Risk;
- Control;
- DecisionRecord;
- pacote de evidências;
- dashboard inicial;
- relatórios executivos.

### 1.0.0 — MVP institucional auditável

- governança operacional mínima;
- trilhas de auditoria consistentes;
- evidências com hash;
- reconciliação informacional funcional;
- documentação organizada;
- riscos e controles rastreáveis;
- API estável inicial.

---

## 14. Princípio de manifesto vivo, porém controlado

Este manifesto poderá evoluir, mas não poderá ser alterado de forma casual.

Toda alteração relevante deverá:

1. atualizar o changelog;
2. gerar decisão documentada;
3. preservar histórico;
4. indicar impacto em riscos;
5. manter coerência com o anti-escopo regulado;
6. respeitar a raiz institucional `coinbalance/`.

---

## 15. Declaração primordial

A CoinBalance existe para transformar complexidade em clareza, dados em evidência, registros em memória, divergências em governança e decisões em rastros verificáveis.

A CoinBalance não nasce como promessa financeira.  
Nasce como infraestrutura de confiança.

A CoinBalance não começa pela movimentação de recursos.  
Começa pela integridade da informação.

A CoinBalance não busca parecer regulada antes da hora.  
Busca estar tecnicamente preparada, documentalmente íntegra e institucionalmente prudente.

Este é o marco primordial da Fase 0.

---

## 16. Arquivos de referência

Este manifesto se apoia nos seguintes artefatos iniciais:

- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `docs/2026/05/memorando-institucional-inicial.md`
- `docs/2026/05/plano-viabilidade-tecnica.md`
- `docs/2026/05/matriz-riscos-controles.md`
- `docs/adr/ADR-001-monolito-modular.md`
- `docs/adr/ADR-002-anti-escopo-regulado.md`
- `docs/adr/ADR-003-flask-postgresql.md`
- `docs/adr/ADR-004-versionamento-estruturado-e-estrutura-de-raiz.md`
- `security/secure-development-policy.md`
- `security/secrets-policy.md`
- `security/threat-model.md`
- `compliance/checklist-novas-funcionalidades.md`
- `compliance/linguagem-permitida-proibida.md`
- `compliance/classificacao-dados.md`
