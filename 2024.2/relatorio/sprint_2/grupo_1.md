# Sprint 2 - Broken Authentication

## O que é Autenticação

A autenticação, é o processo de verificar se uma pessoa, sistema ou recurso realmente possui certas características ou atributos que ele afirma ter. Ou seja, quando você faz login em um site, o sistema verifica se a sua senha corresponde ao que ele tem registrado, para garantir que você é quem diz ser. A autenticação é a primeira linha de defesa contra acessos não autorizados em sistemas e aplicativos web. Ela pode ser realizada por diferentes métodos, como baseados em conhecimento (como senhas e PINs), baseados em posse (como cartões de identificação e dispositivos de autenticação) e baseados em características pessoais (como biometria, incluindo impressões digitais e reconhecimento facial). Além disso, a autenticação pode ser única, quando utiliza apenas um método, ou multifatorial (MFA), quando combina dois ou mais métodos para aumentar a segurança, como é o caso da autenticação de dois fatores (2FA).

## Ataques na Autenticação

### Ataques à Autenticação Baseada em Conhecimento

Esse método de autenticação depende de informações pessoais estáticas, que podem ser obtidas, adivinhadas ou forçadas.

### Ataques à Autenticação Baseada em Posse

Um benefício da autenticação baseada em posse é sua resistência a ameaças cibernéticas comuns. Métodos de autenticação que dependem de itens físicos, como tokens de hardware ou cartões inteligentes, são geralmente mais seguros, pois é mais difícil para os atacantes adquirir ou replicar objetos físicos do que obter informações por phishing ou vazamentos de dados.

### Ataques à Autenticação Baseada em Herança

A autenticação baseada em herança, como o uso de biometria, oferece conveniência e facilidade de uso, pois os usuários não precisam lembrar senhas complexas ou carregar tokens físicos. Os sistemas de autenticação baseados em herança devem lidar com preocupações sobre privacidade, segurança de dados e possíveis preconceitos nos algoritmos de reconhecimento biométrico para garantir a adoção e confiança generalizada.

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

# Vulnerabilidade encontrada

Foi identificado que é possível alterar a autorização de um usuário por meio de 
um acesso não autorizado. Por exemplo, um usuário com perfil operacional consegue 
alterar seu tipo para "gestor", o que não deveria ocorrer.

## Exemplo de Comportamento Inesperado

Ao acessar o perfil de um usuário operacional, recebemos a seguinte resposta do 
servidor. Podemos observar que, no campo `"type"`, o valor é `"university_user"`. 
Isso nos permite deduzir que o tipo `"university_admin"` possui mais privilégios.

```json
{
  "id": 2,
  "url": "http://localhost:8000/api/users/2/",
  "firstName": "João",
  "lastName": "da Silva",
  "universityName": "UFMG - Universidade Federal de Minas Gerais",
  "email": "admin@ufmg.br",
  "type": "university_user",
  "accountPasswordStatus": "OK",
  "haveResetPasswordTokenEnable": false,
  "createdOn": "2024-12-09T19:07:21.310022"
}
```

É possível alterar esse atributo do usuário, especificamente o campo "type", 
enviando uma requisição PATCH para a mesma URL que foi utilizada para o GET do 
usuário, com o corpo da requisição contendo o valor "type": "super_user".

## Exemplo de Requisição curl para Alteração:
```
curl --location --request PATCH 'http://localhost:8000/api/university-user/2/' \
--header 'Referer: http://localhost:3000/' \  
--header 'authorization: Token 634363bf594831b3f23e01da566436b13ddb5b8d' \  
--data '{
    "type":"university_admin"
}'  
``` 
Ao realizar essa requisição, recebemos o status HTTP 200 OK e, ao atualizar a 
página, o perfil do usuário é alterado para uma nova Role/autorização de "gestor".

### Resposta do Servidor:

```json
{
    "id": 2,
    "url": "http://localhost:8000/api/university-user/2/",
    "firstName": "João",
    "lastName": "da Silva",
    "email": "admin@ufmg.br",
    "type": "university_admin",
    "createdOn": "2024-12-09T19:07:21.310022",
    "university": 1
}
```
Agora, o usuário tem privilégios de gestão, podendo criar novos usuários com 
permissões de "gestor", gerenciar as pessoas da universidade e realizar todas 
as ações que um gestor pode executar no aplicativo, mesmo sem ter a autorização 
adequada. Esse comportamento ocorre porque a rota não verifica a autorização do 
usuário antes de permitir a alteração do valor do campo "type". Isso configura 
uma vulnerabilidade grave em qualquer sistema.

## Alteração para Super Usuário

Além disso, é possível alterar o tipo de usuário para "super_user", o que concede 
a capacidade de gerenciar pessoas de todas as instituições e 
até mesmo as próprias instituições.

### Exemplo de Requisição curl para Elevar para Super Usuário:
```
curl --location --request PATCH 'http://localhost:8000/api/university-user/2/' \
--header 'Referer: http://localhost:3000/' \
--header 'authorization: Token 8f533fa75dc1ab6af3dabf1fbdf166c28a38ba48' \
--header 'Content-Type: application/json' \
--data '{
    "type":"super_user"
}'
```
Essa vulnerabilidade é extremamente crítica, pois permite que usuários não 
autorizados assumam funções administrativas e ganhem controle sobre todos 
os dados e operações do sistema.
# Conclusão

A análise de vulnerabilidades de autenticação mostrou-se limitada devido a falhas 
no recebimento de e-mails cruciais para a execução de testes como brute-force e a 
análise de tokens. Além disso, o sistema em questão adota boas práticas de segurança, 
como o uso de tokens altamente aleatórios, o que torna ataques de manipulação e
brute-force ineficazes. Outro ponto importante foi a utilização de mensagens genéricas 
no caso de erro de autenticação, como "e-mail não cadastrado e/ou senha inválida".
Essa abordagem impede a enumeração de usuários e dificulta a aplicação de ataques 
de força bruta, já que não é possível distinguir se o erro ocorreu devido a um usuário 
inexistente ou uma senha incorreta. Essas medidas contribuem para a segurança geral do 
sistema, tornando-o mais resistente a tentativas de acesso não autorizado.

Entretanto, foi identificada uma vulnerabilidade grave relacionada à falta de verificação 
de autorização antes de alterar os privilégios de usuários. A manipulação do campo "type" 
permite que usuários não autorizados elevem seus próprios privilégios para "gestor" ou até 
"super usuário", o que pode comprometer o controle e a segurança do sistema. Essa falha expõe 
o sistema a um risco significativo, permitindo que qualquer usuário com acesso básico altere suas 
permissões, resultando em um controle indevido sobre as operações do sistema e afetando toda a gestão 
de usuários e dados sensíveis.

