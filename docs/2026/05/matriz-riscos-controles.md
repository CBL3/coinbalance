# Matriz Inicial de Riscos e Controles

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Inicial  
Classificação: Documento interno de risco

| Risco | Severidade | Controle inicial | Evidência esperada | Owner |
| --- | --- | --- | --- | --- |
| Caracterização indevida como serviço regulado | Alta | Anti-escopo regulado, linguagem controlada e ADR obrigatório | Manifesto, checklist e materiais revisados | Compliance |
| Segredo exposto em código | Alta | `.gitignore`, `.env.example`, política de segredos | Revisão de código e varredura | Infra/DevOps |
| Decisão arquitetural sem memória | Média | ADR obrigatório para decisões difíceis de reverter | ADR aprovado | Tech Lead |
| Falta de rastreabilidade | Alta | Health metadata, plano de AuditEvent na 0.2 | Logs e eventos futuros | Tech Lead |
| Dado sensível sem classificação | Alta | Política de classificação de dados | Registro de classificação | Compliance |
| Dependência vulnerável | Média | Pinning progressivo e varredura de dependências | Relatório de varredura | Infra/DevOps |
| Funcionalidade fora de escopo | Alta | Checklist de novas funcionalidades | Checklist aprovado | PO/Compliance |
| Documentação dispersa | Média | Estrutura `docs/YYYY/MM`, `docs/adr`, `security`, `compliance` | Árvore documental | PO |

## Regra de manutenção

Todo risco novo deve ter owner, severidade, controle, evidência esperada e status de tratamento.
