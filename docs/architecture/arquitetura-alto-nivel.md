# Arquitetura alvo (alto nível)

Data: 2026-05-19  
Versão: 0.1.0-alpha  
Status: Vigente  
Classificação: Documento interno de arquitetura

## Leitura atual do projeto

O repositório atual já possui uma Fase 0 executável e documentada. A base técnica inclui backend Flask modular, API versionada, Docker Compose, CI inicial, documentação institucional e controles de segurança/compliance.

A stack alvo segue organizada em:

- Backend Flask em `backend/app`.
- API `/api/v1/health`, `/api/v1/institutional/scope` e `/api/v1/hardware/interface`.
- PostgreSQL como persistência alvo.
- Redis como infraestrutura planejada para filas/cache.
- Docker Compose em `docker-compose.yml`.
- CI em `.github/workflows/ci.yml`.
- Scaffolds de identidade, RBAC, autenticação JWT e diário de integridade por hash.
- Orquestração de agentes para um MVP de Gêmeo Digital.
- Roteamento híbrido entre modelos proprietários e open source.
- Pipeline de telemetria, feedback, RLAIF/RLHF e auditoria.
- Governança de IA, incident response, pilotos comerciais, KPIs e roadmap.
- Opção futura de empacotamento on-prem para clientes com alta exigência de privacidade.

O ponto crítico é transformar intenção em contratos técnicos: APIs, schemas, controles, critérios de aceitação, observabilidade e rotas de fallback.

## Princípio de resiliência

Resiliência aqui significa conseguir reconstruir a camada lógica de uma unidade, serviço ou processo a partir de estado confiável, eventos auditáveis e contratos versionados. Antes de migrar, restaurar ou reexecutar uma unidade lógica, o sistema deve capturar identidade, contexto, permissões, estado, dependências, trilha de auditoria e critérios de integridade. Após a reconstrução, a operação só continua se os checksums lógicos, políticas e evidências estiverem consistentes.

## Componentes

1. API Gateway
   - Autenticação, autorização, rate limit, tenant isolation e validação de payload.
   - Entrada única para aplicações, integrações e operadores humanos.

2. Orquestrador
   - Coordena agentes, ferramentas, filas, políticas e fallback.
   - Mantém estado de execução por `trace_id`, `tenant_id`, `workflow_id` e `policy_version`.

3. Model Router
   - Escolhe modelo por risco, custo, latência, privacidade e qualidade esperada.
   - Escala de decisão: regra determinística, modelo pequeno/local, modelo proprietário, execução humana.
   - Deve registrar motivo da escolha e orçamento consumido.

4. Adaptadores de modelos
   - Interface única para modelos proprietários, open source e on-prem.
   - Normaliza entrada, saída, erros, custos, latência, limites e evidências.

5. Policy Engine
   - Centraliza limites de agentes, dados permitidos, ferramentas permitidas, aprovações e exceções.
   - Nenhum agente executa ação material sem política explícita.

6. Memória e conhecimento
   - RAG com documentos aprovados, versionados e classificados por sensibilidade.
   - Memória operacional curta por sessão e memória institucional auditável por tenant.

7. Telemetria e auditoria
   - Eventos append-only com `trace_id`, `actor_id`, `agent_id`, decisão, evidência e outcome.
   - Métricas de custo, latência, acurácia, rejeições, overrides humanos e incidentes.

8. Camada de integração
   - Conectores para ERP, CRM, documentos, contratos, bases financeiras, sensores ou unidades eletrônicas.
   - Cada conector precisa de contrato de capacidade: ler, sugerir, simular, executar, reverter.

9. Plano on-prem
   - Pacote com gateway, orquestrador, modelos permitidos, vector store, observabilidade local e sincronização seletiva.
   - Nenhum dado sensível sai do ambiente sem política e registro.

## Fluxo lógico principal

1. Usuário ou sistema inicia um workflow.
2. API Gateway valida identidade, tenant, escopo e limites.
3. Orquestrador cria `trace_id` e consulta o Policy Engine.
4. Model Router escolhe o menor recurso capaz de resolver a tarefa com segurança.
5. Agentes executam leitura, raciocínio, simulação e proposta de ação.
6. Ação material exige validação determinística, evidência e aprovação conforme risco.
7. Resultado, custo, decisão e feedback são gravados em telemetria.
8. Falhas acionam fallback, fila, rollback ou contenção.

## Requisitos não funcionais

- Segurança: tenant isolation, least privilege, criptografia, secrets manager, logs imutáveis.
- Confiabilidade: retries idempotentes, circuit breakers, filas, snapshots e restauração testada.
- Auditabilidade: cada decisão precisa ser reconstituível por `trace_id`.
- Custo consciente: orçamento por workflow, cache, compactação de contexto e escalonamento seletivo de modelos.
- Portabilidade: adaptadores desacoplados de fornecedor.
- Operação institucional: runbooks, owners, SLAs, matriz RACI e revisão periódica.

## Lacunas atuais da arquitetura alvo

- Ainda não há persistência real, migrations ou banco inicial.
- Ainda não há autenticação, RBAC ou isolamento multi-organização completos e aplicados às rotas de negócio.
- Ainda não há orquestrador de agentes executável.
- Ainda não há ingestão, reconciliação funcional ou Evidence Vault.
- Ainda não há avaliação automatizada de prompts/modelos.
