# Relatório Sprint 3

## Arthur Grandão de Mello - 211039250

## IDOR (Insecure Direct Object References)

As vulnerabilidades IDOR ocorrem quando uma aplicação web expõe uma referência direta a um objeto, como um arquivo ou recurso de banco de dados, que o usuário final pode controlar diretamente para obter acesso a outros objetos semelhantes. Se um usuário puder acessar um recurso devido à falta de um sistema sólido de controle de acesso, o sistema será considerado vulnerável.

# Vulnerabilidades

## `/api/university-users/<pk>/`  &  `/api/users/<pk>/`

Nestas rotas, mesmo logado com um usuário padrão (university-user), é possível alterar as informações de qualquer outro usuário do sistema, incluindo você mesmo, ou até mesmo deletá-los.

**Exemplos:**

* **Escalar permissão do usuário**

Podemos alterar nosso tipo de permissão no sistema, o que nos dá acesso irrestrito ao mesmo.

<p align="left">
    <img src="img/escalar_comando.png" alt="Escalar Comando" width="49%" height="%49">
    <img src="img/escalar_comando_resultado.png" alt="Escalar Comando Resultado" width="49%">
</p>

* **Deletar outro usuário**

Podemos deletar outro usuário.

<p align="left">
    <img src="img/deletar_usuario.png" alt="Deletar Usuário" width="49%">
    <img src="img/deletar_usuario_resultado.png" alt="Deletar Usuário Resultado" width="49%">
</p>

* **Alterar senha de outros usuários**

Podemos remover o acesso de outra pessoa do sistema, ao menos temporariamente.

<p align="left">
    <img src="img/trocar_senha.png" alt="Trocar Senha" width="49%" height="%49">
    <img src="img/trocar_senha_resultado.png" alt="Trocar Senha Resultado" width="49%" height="49%">
</p>

# Outras rotas testadas

`/api/university-user/<pk>/favorite-consumer-units\.<format>/` <br>
`/api/university-user/change-university-user-type/` <br>
`/api/university-user/change-university-user-type\.<format>/` <br>
`/api/users/change-user-password/` <br>
`/api/users/change-user-password\.<format>/` <br>

As rotas acima não apresentaram nenhuma vulnerabilidade IDOR.

Também não observei nenhuma chamada AJAX ao utilizar o front-end da aplicação.
