# Política de Uso de IA

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno de governança

## Objetivo

Definir limites institucionais para uso de IA na CoinBalance, protegendo clientes, dados, operação, reputação e decisões materiais. A IA pode recomendar, explicar, simular e acelerar; ações irreversíveis exigem controle explícito.

## Escopo

Esta política cobre:

- Agentes internos e externos.
- Modelos proprietários, open source e on-prem.
- Prompts, ferramentas, RAG, memórias, integrações e automações.
- Dados de clientes, contratos, telemetria, métricas e evidências.
- Pilotos comerciais e ambientes de staging/produção.

## Classificação de risco

| Nível | Exemplo | Regra |
| --- | --- | --- |
| Baixo | Resumo de documento público | Execução automática permitida com log |
| Médio | Classificação operacional sem impacto financeiro direto | Execução com validação e amostragem |
| Alto | Recomendação contratual, financeira ou de compliance | Revisão humana obrigatória |
| Crítico | Transação irreversível, vazamento, alteração de permissão | Bloqueio por padrão e aprovação formal |

## Limites de agentes

- Agentes não podem criar, alterar ou excluir permissões sem aprovação.
- Agentes não podem executar transações financeiras irreversíveis no MVP.
- Agentes não podem enviar dados sensíveis a modelos externos sem política explícita.
- Agentes devem operar com menor privilégio e ferramentas allowlisted.
- Agentes devem registrar justificativa, evidência e versão de política.

## Responsabilidades

- Sponsor Executivo: aceita risco institucional e remove impedimentos.
- Product Owner: prioriza casos de uso e critérios de sucesso.
- Tech Lead: garante arquitetura, integração e controles técnicos.
- ML Engineer: governa modelos, avaliações, datasets e roteamento.
- Infra/DevOps: protege ambientes, segredos, rede, backups e observabilidade.
- Compliance/Legal: valida política, contratos, retenção e auditoria.
- Customer Success: mede adoção, ROI e qualidade no piloto.

## Dados e privacidade

- Classificar dados antes de uso em prompt ou ferramenta.
- Redigir, mascarar ou tokenizar PII quando possível.
- Separar dados brutos, sanitizados, métricas e artefatos de treinamento.
- Proibir treinamento com dados de cliente sem base contratual e aprovação.
- Registrar consentimento, retenção e propósito de uso.

## Explicabilidade e auditoria

Cada decisão relevante precisa ter:

- `trace_id`.
- Dados de entrada referenciados por hash ou storage seguro.
- Modelo, versão de prompt, política e ferramenta utilizada.
- Evidências consultadas.
- Motivo da decisão ou motivo do bloqueio.
- Aprovação humana quando aplicável.

## Consumo consciente de LLMs

- Preferir regras, parsers, cache e busca estruturada antes de LLM.
- Usar modelos menores para triagem e roteamento.
- Escalar para modelos maiores somente por risco, ambiguidade ou baixa confiança.
- Medir custo por workflow e por tenant.
- Revisar mensalmente tarefas que podem ser rebaixadas para modelo menor.

## Revisão

Esta política deve ser revisada no fim de cada piloto, após qualquer incidente relevante e antes de mover workflows de staging para produção.
