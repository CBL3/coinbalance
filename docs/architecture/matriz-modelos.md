# Matriz de decisão: OpenSource vs Proprietário

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno de arquitetura e LLMOps

## Regra de decisão

Use o menor poder computacional capaz de entregar resposta correta, auditável e segura. Modelos maiores entram quando há ambiguidade real, alta consequência, necessidade de síntese complexa ou baixa confiança do caminho barato.

## Critérios

- Privacidade: dado sensível, regulado, estratégico ou de cliente.
- Materialidade: impacto financeiro, jurídico, operacional ou reputacional.
- Latência: necessidade de resposta síncrona ou assíncrona.
- Custo: orçamento por workflow e por tenant.
- Qualidade: taxa de erro aceitável, necessidade de explicação e validação externa.
- Portabilidade: risco de lock-in, exigência on-prem e fallback.

## Matriz

| Caso de uso | Requisito crítico | Recomendação | Justificativa | Ação |
| --- | --- | --- | --- | --- |
| Classificação simples de tickets/eventos | Custo e latência | Open source/local | Baixa materialidade e alta repetição | Usar modelo pequeno com threshold e fallback |
| Extração de campos de documentos padronizados | Precisão e auditoria | Híbrido | OCR/parsing determinístico com LLM só para exceções | Validar contra schema e regras |
| Análise de contrato piloto | Qualidade e risco jurídico | Proprietário ou modelo premium privado | Alta ambiguidade e impacto institucional | Exigir revisão humana e trilha de evidências |
| Onboarding de cliente | Privacidade e experiência | Híbrido | Pode combinar regras, RAG e modelo maior para exceções | Separar PII, usar redaction e consentimento |
| Reconciliação informacional | Materialidade | Determinístico + LLM assistivo | Comparação deve ser reprodutível; LLM não valida patrimônio nem saldo | LLM explica divergências, sistema registra evidências |
| Gêmeo Digital de processo | Estado e rastreabilidade | Híbrido | Simulação precisa de eventos e modelo de domínio | Event sourcing, snapshots e validação |
| Incidente de segurança | Tempo e contenção | Híbrido com runbooks | LLM auxilia triagem, mas política governa resposta | Bloquear ações destrutivas sem aprovação |
| Pacote on-prem | Privacidade e soberania | Open source/on-prem | Dados não podem sair do perímetro do cliente | Adaptador local e telemetria sanitizada |

## Política de escalonamento

1. Tente regra determinística, cache ou busca estruturada.
2. Use modelo pequeno para classificação, resumo curto ou roteamento.
3. Use modelo maior para síntese, planejamento, ambiguidade ou baixa confiança.
4. Acione humano quando houver ação irreversível, impacto financeiro relevante ou conflito de evidência.
5. Registre custo, latência, confiança e motivo de escalonamento.

## Guardrails de consumo consciente

- Limite de tokens por workflow e por tenant.
- Compactação de contexto antes de chamar modelo caro.
- Cache semântico para perguntas recorrentes.
- Batch assíncrono para tarefas não urgentes.
- Avaliações periódicas para rebaixar tarefas para modelos menores quando possível.
- Bloqueio de chamadas redundantes dentro do mesmo `trace_id`.
