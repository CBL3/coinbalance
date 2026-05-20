# Classificação de Dados

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno de compliance

## Classes

| Classe | Descrição | Exemplo | Controle |
| --- | --- | --- | --- |
| Público | Informação divulgável | README | Revisão simples |
| Interno | Informação operacional não sensível | Roadmap interno | Acesso interno |
| Confidencial | Estratégia, arquitetura ou cliente | Matriz de riscos | Acesso restrito |
| Sensível | PII, credenciais, contratos, dados regulados | Documento de cliente | Criptografia, minimização e logs restritos |
| Restrito | Segredos, chaves, tokens, dados críticos | API key | Secret manager e rotação |

## Regras

- Dados devem ser classificados antes de persistência ou envio a terceiros.
- Logs não devem conter segredos.
- Dados sensíveis devem ser minimizados.
- Evidências devem possuir origem, hash, metadados e retenção.
- Dados de cliente não devem ser usados para treinamento sem autorização explícita.
