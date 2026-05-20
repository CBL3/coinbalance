# ADR-005: Identidade, RBAC e auditoria persistente

Status: Aprovado  
Data: 2026-05-20

## Contexto

A versão `0.2.0-alpha` precisa transformar o scaffold fundacional em controle operacional verificável, sem avançar para atividade regulada. A CoinBalance precisa identificar atores, vincular usuários a organizações, aplicar permissões e registrar eventos críticos de forma persistente.

## Decisão

Implementar a primeira base de identidade, organizações, RBAC e auditoria persistente no monólito modular Flask, com migrations Alembic/Flask-Migrate e testes automatizados de escopo organizacional.

## Justificativa

Identidade e auditoria são pré-condições para ingestão, reconciliação informacional, evidências, riscos e controles. Antes de processar dados sensíveis ou fluxos de piloto, a plataforma precisa provar quem acessou, qual permissão foi aplicada, qual organização estava no escopo e qual evento foi registrado.

## Escopo aprovado

- `Organization`, `User`, `Role` e `Permission`.
- Relacionamentos de usuário-papel e papel-permissão.
- Permissões globais e permissões vinculadas à organização.
- Endpoint autenticado de identidade.
- Endpoint protegido de auditoria.
- `AuditEvent` persistente.
- Migration inicial do schema.
- Testes de RBAC e isolamento organizacional.

## Fora de escopo

- Login com senha, SSO, MFA ou gestão completa de sessão.
- Interface administrativa de usuários.
- Autorização em todos os futuros módulos de negócio.
- Produção multi-tenant completa.
- Qualquer operação financeira, patrimonial ou transacional.

## Consequências

- Rotas sensíveis devem declarar permissão exigida.
- Eventos críticos devem registrar organização, ator, entidade, tipo de evento e metadados.
- Usuários sem `system:admin` ficam limitados ao próprio `organization_id`.
- Próximas funcionalidades devem reutilizar os helpers de RBAC e auditoria em vez de criar controles paralelos.

## Riscos relacionados

- Uso de JWT sem provedor de identidade definitivo.
- Necessidade de hardening posterior para rotação de chaves, expiração, revogação e SSO.
- Necessidade de validar migrations em PostgreSQL real antes de produção.
