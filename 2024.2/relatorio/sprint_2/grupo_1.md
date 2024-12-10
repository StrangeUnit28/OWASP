# Sprint 2 - Broken Authentication

## Relatório de Estudo - Módulo: Vulnerabilidades de Autenticação em Aplicações Web

Neste módulo, o foco principal foi entender as vulnerabilidades e configurações incorretas relacionadas à autenticação em aplicativos web, que podem ser exploradas para obter acesso não autorizado. Durante o curso, foram abordados diversos métodos de autenticação, técnicas de ataque e falhas no gerenciamento de sessões. As principais áreas de estudo incluem:

## 1. Visão Geral dos Métodos de Autenticação e Ataques
Estudamos os diferentes métodos usados para autenticação em sistemas web, como senhas, tokens e autenticação multifatorial. Também foram apresentados ataques comuns que visam comprometer esses métodos, como ataques de força bruta e outros tipos de vulnerabilidades.

## 2. Ataques de Força Bruta à Autenticação
Exploração de técnicas que permitem a automação de tentativas de senha, visando quebrar credenciais de usuários por tentativa e erro.

## 3. Ataques à Autenticação Baseada em Senha
Fomos introduzidos aos riscos associados à autenticação baseada em senha, como o uso de senhas fracas ou a exposição de senhas em texto claro.

## 4. Bypass de Autenticação
Estudamos técnicas que permitem contornar os mecanismos de autenticação de um sistema, acessando recursos sem a devida autorização.

## 5. Ataques ao Tratamento Impróprio de Sessões
Analisamos como falhas no gerenciamento de sessões podem ser exploradas para manter sessões ativas indevidamente ou roubar sessões de outros usuários.

O módulo foi composto por sessões teóricas seguidas de exercícios práticos, proporcionando uma compreensão mais profunda das táticas e técnicas mencionadas. Os exercícios práticos foram realizados no ambiente de laboratório fornecido, o PwnBox, ou em uma máquina virtual pessoal, com comandos de exemplo e saídas para reforçar o aprendizado.

Ao final, o módulo incluiu uma avaliação prática, que testou as habilidades adquiridas ao longo do curso. Concluímos que a prática contínua e a execução dos exemplos apresentados são essenciais para consolidar os conceitos e estratégias de mitigação das vulnerabilidades de autenticação.

# Aplicação no MEPA

## Enumeração de Usuários

## Resumo sobre a Impossibilidade de Aplicar Enumeração de Usuários

Não foi possível aplicar a técnica de enumeração de usuários, pois o sistema utiliza **email** como identificador para o login. Além disso, a mensagem de erro retornada para credenciais incorretas não diferencia se o usuário não existe ou se apenas a senha está errada. A mensagem apresentada é genérica: "**e-mail não cadastrado e/ou senha inválida**", o que impede a exploração da vulnerabilidade.

## Senhas por força bruta
### Desafios Enfrentados na Execução do Teste

No projeto em questão, a intenção era criar um usuário para entender o padrão de criação de credenciais e reduzir a amostra de senhas possíveis para otimizar o brute-force. No entanto, os passos e padrões de criação das credenciais foram enviados por e-mail, mas eu não consegui receber esse e-mail. Sem essas informações, a redução da amostra de senhas tornou o ataque muito mais desafiador.
Conclusão

O ataque de brute-force seria eficaz apenas se fosse possível determinar um usuário válido, com a credencial sendo a única variável desconhecida. Sem conhecer o padrão de criação das senhas, o ataque se torna difícil, pois a amostra de senhas a ser testada permanece ampla. Para um ataque bem-sucedido, é necessário entender os padrões de senha para otimizar o processo e aumentar as chances de sucesso.

## Tokens de redefinição de senha por força bruta

A etapa de identificação do token de reset de senha depende do envio de um e-mail contendo o token necessário para validar a solicitação de recuperação de senha. No entanto, devido à impossibilidade de receber o e-mail, não foi possível acessar o token e, portanto, não foi viável realizar a análise ou aplicar o teste relacionado à validação do token.

### Códigos 2FA de força bruta
Sem o acesso ao e-mail com o token, não pude verificar como o sistema lida com o processo de recuperação de senha nem analisar seus padrões de criação ou de validade. Isso impediu a execução da etapa de teste, uma vez que o fluxo de reset de senha não pôde ser completamente analisado.
Conclusão

A realização do teste dependia do recebimento do e-mail com o token de reset de senha. Sem esse e-mail, não foi possível aplicar a análise ou as técnicas de interceptação, resultando na impossibilidade de testar o processo de recuperação de senha.

### Ataques a Tokens de Sessão 

Os ataques a tokens de sessão descritos, como brute-force e a manipulação de tokens previsíveis, não são aplicáveis ao projeto, pois o sistema em questão utiliza tokens altamente aleatórios e seguros, gerados com o algoritmos criptográficos Devido à aleatoriedade desses tokens e à natureza do algoritmo utilizado, não é viável adivinhar ou manipular os tokens para obter acesso não autorizado.

Além disso, o projeto não emprega tokens de sessão codificados ou manipuláveis, o que torna os ataques descritos, como a alteração de cookies ou a exploração de tokens previsíveis, inviáveis no contexto do projeto. Dessa forma, tais vulnerabilidades não são relevantes para o cenário analisado.

Exemplo: 

1 - 3916d80000febe4db35759bd0f89010ca3dda193  
2 - 75d97f9d0471367134110e380b4ad1fdd6b71f17  
3 - b857b771e690b73f2d96f6c2042a29ba004ed201

# Conclusão

A análise de vulnerabilidades de autenticação mostrou-se limitada devido a falhas no recebimento de e-mails cruciais para a execução de testes como brute-force e a análise de tokens. Além disso, o sistema em questão adota boas práticas de segurança, como o uso de tokens altamente aleatórios, o que torna ataques de manipulação e brute-force ineficazes. Outro ponto importante foi a utilização de mensagens genéricas no caso de erro de autenticação, como "e-mail não cadastrado e/ou senha inválida". Essa abordagem impede a enumeração de usuários e dificulta a aplicação de ataques de força bruta, já que não é possível distinguir se o erro ocorreu devido a um usuário inexistente ou uma senha incorreta. Essas medidas contribuem para a segurança geral do sistema, tornando-o mais resistente a tentativas de acesso não autorizado.