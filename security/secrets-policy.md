# Política de Segredos

Data: 2026-05-20
Versão: 0.2.0-alpha
Status: Vigente  
Classificação: Documento interno de segurança

## Objetivo

Evitar exposição de credenciais, tokens, chaves privadas, senhas, strings de conexão e qualquer material equivalente.

## Regras

- Segredos não devem ser armazenados no repositório.
- `.env` e `.env.*` são ignorados por padrão.
- `.env.example` deve conter apenas nomes de variáveis e valores não sensíveis.
- Segredos de produção devem ficar em secret manager ou mecanismo equivalente.
- Rotação é obrigatória em caso de exposição real ou suspeita.

## Exemplos de segredos

- Chaves de API.
- Tokens OAuth.
- Senhas de banco.
- Certificados privados.
- Webhooks assinados.
- Credenciais de provedores de nuvem.

## Resposta a exposição

1. Revogar ou rotacionar o segredo.
2. Identificar impacto e janela de exposição.
3. Registrar incidente.
4. Remover o segredo do histórico quando aplicável.
5. Criar controle preventivo.
