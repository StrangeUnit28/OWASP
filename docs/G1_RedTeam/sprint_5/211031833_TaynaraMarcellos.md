# Relatório sobre Session Fixation

## 1. Introdução
Session Fixation é um tipo de ataque onde um invasor consegue fixar um identificador de sessão válido e, em seguida, engana a vítima para que esta utilize essa sessão ao fazer login. Isso permite ao atacante assumir a sessão da vítima, levando a um ataque de sequestro de sessão.

## 2. Mecanismo do Ataque
O ataque de Session Fixation ocorre em três estágios:

**Estágio 1: Obtenção de um Identificador de Sessão Válido**

Um atacante pode simplesmente acessar a aplicação para obter um identificador de sessão sem precisar autenticar-se.

Alternativamente, o invasor pode criar uma conta na aplicação para obter um identificador de sessão válido.

**Estágio 2: Fixação do Identificador de Sessão**

O ataque ocorre quando o identificador de sessão permanece o mesmo antes e depois do login.

Aplicações vulneráveis aceitam identificadores de sessão a partir de strings de consulta de URL (Query Strings) ou Post Data.

Se um parâmetro de sessão na URL for aceito e convertido em um identificador de sessão válido, o atacante pode fixar esse valor.

**Estágio 3: Engano da Vítima para Utilizar a Sessão Comprometida**

O atacante cria um link contendo o identificador de sessão fixado e convence a vítima a acessá-lo.

Ao acessar o link, a vítima assume a sessão controlada pelo atacante.


## 4. Medidas de Prevenção

Regenerar o identificador de sessão após o login.

Não aceitar identificadores de sessão em URL Query Strings ou Post Data.

Utilizar cookies com atributos seguros (HttpOnly, Secure, SameSite).

Definir um tempo de expiração curto para sessões inativas.

Implementar autenticação multifator (MFA) para dificultar a exploração de sessões comprometidas.

## 5. Conclusão
Session Fixation é uma vulnerabilidade perigosa que pode comprometer a segurança de usuários em aplicações web. Implementar boas práticas de segurança e evitar o uso inadequado de identificadores de sessão é essencial para mitigar esse tipo de ataque.