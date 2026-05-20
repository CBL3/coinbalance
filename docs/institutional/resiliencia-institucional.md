# Resiliência Institucional CoinBalance

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno institucional

## Diagnóstico reverso

O projeto está em fase de arquitetura e governança. Ainda não há aplicação, infraestrutura, CI/CD ou testes versionados neste diretório. A intenção, porém, é clara: criar uma plataforma de agentes e Gêmeo Digital com telemetria, governança, piloto comercial e opção on-prem.

O trabalho mais importante agora é transformar a visão em contratos verificáveis. Sem contratos, "resiliência" vira frase bonita; com contratos, vira a capacidade de cair, reconstruir estado, provar o que aconteceu e seguir inteiro.

## Definição operacional de resiliência

Resiliência é a capacidade de uma unidade lógica, eletrônica, documental ou operacional:

1. Declarar sua identidade e permissões.
2. Registrar eventos relevantes de forma ordenada e auditável.
3. Capturar snapshots de estado.
4. Reconstruir estado por replay.
5. Validar integridade por checksums, políticas e evidências.
6. Entrar em quarentena quando a reconstrução não for confiável.
7. Retomar operação sem perder rastreabilidade.

Na metáfora do buraco de minhoca: não basta chegar do outro lado. O sistema precisa chegar com memória, identidade, permissões, causalidade e integridade preservadas.

## Stack institucional alvo

- Gateway: autenticação, autorização, rate limit e validação de entrada.
- Orquestrador: workflows, agentes, filas, retries e estado.
- Model Router: escolha consciente de modelo por risco, custo, latência e qualidade.
- Policy Engine: limites de agentes, dados, ferramentas e aprovações.
- RAG: conhecimento aprovado, versionado e classificado.
- Event Store: telemetria append-only, replay e auditoria.
- Observabilidade: logs, métricas, traces, custo e qualidade.
- Conectores: ERP, CRM, documentos, contratos, bases financeiras e dispositivos.
- Painel executivo: KPIs, SLA, ROI, incidentes e consumo de LLMs.

## Segurança institucional

### Identidade e acesso

- SSO/MFA para operadores humanos.
- Service accounts por agente e por ambiente.
- Least privilege por ferramenta.
- Segregação entre dev, staging, produção e on-prem.
- Revisão periódica de permissões.

### Dados

- Classificação: público, interno, confidencial, sensível, regulado.
- Redaction/tokenização antes de prompts externos.
- Criptografia em repouso e em trânsito.
- Retenção por finalidade.
- Proibição de dados de cliente em treinamento sem aprovação explícita.

### Agentes e ferramentas

- Tool allowlist por agente.
- Bloqueio de comandos destrutivos sem aprovação.
- Ação material sempre com política, evidência e trilha.
- Separação entre "sugerir", "simular" e "executar".
- Testes de prompt injection e data exfiltration.

### Supply chain e operação

- Dependências fixadas e revisadas.
- Secrets fora do código.
- Infraestrutura como código antes de produção.
- Backups testados.
- Runbooks para incidentes e recuperação.

## Consumo consciente de LLMs

Otimização não é só gastar menos. É gastar poder cognitivo artificial onde ele muda o resultado.

1. Resolver com regra quando regra basta.
2. Resolver com parser quando estrutura existe.
3. Resolver com busca quando a resposta já está na base.
4. Usar modelo pequeno para triagem, classificação e roteamento.
5. Usar modelo maior para ambiguidade, síntese ou risco alto.
6. Acionar humano quando o custo de errar supera o custo de revisar.

Controles mínimos:

- Orçamento por workflow.
- Cache semântico seguro.
- Compactação de contexto.
- Threshold de confiança.
- Avaliação offline antes de trocar modelo.
- Registro de custo, latência e motivo de escalonamento.

## Cenários de simulação

| Cenário | Falha simulada | Resposta esperada | Critério de sucesso |
| --- | --- | --- | --- |
| Provedor de modelo fora | Timeout ou erro 5xx | Fallback para modelo alternativo ou fila | Workflow não perde estado |
| Prompt injection | Documento tenta roubar dados ou mudar política | Policy Engine bloqueia ferramenta/saída | Evento registrado e sem exfiltração |
| Custo explosivo | Loop de chamadas ou contexto gigante | Budget guard interrompe e pede revisão | Custo limitado por workflow |
| Dados sensíveis | PII entra em fluxo externo | Redaction ou bloqueio | Nenhum dado bruto no prompt |
| Reconciliação divergente | LLM sugere saldo incorreto | Cálculo determinístico prevalece | Divergência vira alerta |
| Conector indisponível | ERP/CRM não responde | Retry idempotente e fila | Sem duplicidade de ação |
| Estado corrompido | Snapshot não bate com replay | Quarentena | Sistema não executa ação material |
| Incidente SEV1 | Ação crítica indevida ou vazamento | Contenção imediata, comunicação e preservação de evidências | MTTR medido e lição registrada |
| Migração on-prem | Cliente exige soberania de dados | Deploy local com telemetria sanitizada | Sem egress de dado sensível |
| Troca de modelo | Novo modelo muda comportamento | Eval regression antes de produção | Sem queda acima do limite aceito |

## Plano de execução

### 0 a 2 semanas

- Fechar workflow crítico do MVP.
- Validar schema de eventos.
- Definir política de dados e riscos.
- Criar massa sintética.
- Definir orçamento de LLM por workflow.

### 3 a 6 semanas

- Implementar orquestrador mínimo.
- Criar agentes de dados, contratos, processo, segurança e observabilidade.
- Implantar event store e dashboard básico.
- Demonstrar fallback e replay de estado.

### 7 a 12 semanas

- Rodar piloto controlado.
- Medir KPIs e custo.
- Executar tabletop de incidente.
- Revisar governança.
- Decidir escala, on-prem ou encerramento.

## Decisão de arquitetura recomendada

Adotar arquitetura híbrida desde o início. O núcleo institucional deve ser portável e auditável; modelos proprietários entram como potência especializada, não como dependência absoluta. A camada de resiliência deve depender de eventos, políticas, schemas e testes, não da memória do modelo.

## Regra final

Antes de atravessar qualquer "buraco de minhoca" operacional, gere um pacote de travessia:

- identidade;
- permissões;
- estado;
- eventos;
- evidências;
- política;
- checksum;
- plano de rollback.

Se qualquer item falhar na chegada, não execute. Reconstrua, compare, contenha e só então prossiga.
