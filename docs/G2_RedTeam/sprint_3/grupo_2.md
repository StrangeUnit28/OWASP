# Relatório Sprint 3 - Insecure Direct Object References

## Membros

|                        Nome                        | Matrícula |
| :------------------------------------------------: | :-------: |
| [Felipe Direito](https://github.com/felipedireito) | 190086971 |
|    [Gabriel Campello](https://github.com/G16C)     | 211039439 |
|    [Gustavo Melo](https://github.com/gusrberto)    | 211039457 |
|  [Matheus Henrique](https://github.com/mathonaut)  | 211029666 |

---

## 1. Teste de IDOR para alteração de dados de outro usuário

### Objetivos

O objetivo desse teste foi verificar se um usuário cadastrado na plataforma é capaz de alterar informações de outro usuário, que podem levar à tomada da conta por um usuário qualquer.

O teste foi realizado no ambiente de [homologação](https://energia.lappis.rocks/) do MEPA.

Para realização do teste foi utilizado a ferramenta de interceptação de requisições do _Burp Suite_, que age como um proxy sobre as requisições HTTP.

### Passo-a-passo

**1**. Os primeiros passos foram se autenticar na plataforma como um usuário de baixo privilégio (nesse caso `José` com cargo `Operacional`).

<center>

Figura 1.1 - Tela de Login.

![Logando na plataforma](./img/burp-idor-passo1.png)

</center>

**2**. Com o proxy do _Burp Suite_ ativado, vou interceptar a requisição de acesso ao perfil do `José`.

<center>

Figura 1.2 - Autenticado como José.

![Tela Home José](./img/burp-idor-passo2.png)

</center>

**3**. Como o parâmetro identificador de usuários é um simples ID sequencial, posso trocar o ID da requisição `GET` de 3 para 2.

<center>

Figura 1.3 - Requisição Original com ID `3`.

![Requisição Original](./img/burp-idor-passo3.png)

</center>

<center>

Figura 1.4 - Requisição Modificada com ID `2`.

![Requisição Modificada](./img/burp-idor-passo4.png)

</center>

**4**. Agora estou visualizando a página como o usuário de ID `2` que neste caso é o `João` que possui privilégios de `Gestão` (acima de José).

<center>

Figura 1.5 - Tela de Perfil pela visão do usuário `João`.

![Perfil João](./img/burp-idor-passo5.png)

</center>

**5**. Com isso é possível acessar a página de Editar Pessoa como `João` e assim alterar suas informações (em especial seu email).

<center>

Figura 1.6 - Tela de Editar Pessoa pela visão do usuário `João`.

![Editar Perfil do João](./img/burp-idor-passo6.png)

</center>

<center>

Figura 1.7 - Alterando as informações do usuário `João`.

![Alterando informações do João](./img/burp-idor-passo7.png)

</center>

**6**. Como o token de sessão não verifica se o usuário tem permissão de realizar essa operação, a requisição retorna com um status `200` e as informações realmente foram alteradas.

<center>

Figura 1.8 - Resposta da requisição no _Burp Suite_.

![Resposta da Requisição](./img/burp-idor-passo8.png)

</center>

<center>

Figura 1.9 - Mensagem de sucesso mostrando que a pessoa foi editada.

![Mensagem de sucesso](./img/burp-idor-passo9.png)

</center>

**7**. Por fim se utilizarmos novamente do método do Passo 2, veremos que de fato as informações do usuário `João` foram alteradas.

<center>

Figura 1.10 - Novo usuário com informações alteradas.

![Novo Usuário](./img/burp-idor-passo10.png)

</center>

Agora após esses passos o usuário `José` poderia pedir uma Redefinição de Senha para esta conta (que agora ele possui o email), e após a redefinição ele teria acesso total à uma conta de outro usuário, que ainda por cima possui privilégios superiores a sua conta original.

### Conclusão

O teste concluiu que existe uma **ALTA** vulnerabilidade na aplicação à ataques IDOR. Algumas possíveis melhorias seriam a implementação de uma política de controle de acesso no Back-End da aplicação, controle esse que utilizaria o token de sessão que a aplicação já possui para validar e verificar todas as requisições. Garantindo que um usuário no sistema possui permissão de realizar uma determinada ação.

Também recomendaria a utilização de IDs mais aleatórios e não-previsíveis que dificultaria o acesso à informações não autorizadas.

---

## Relatório de Testes de Insecure Direct Object References (IDOR) - Matheus

**Objetivo:**

O objetivo deste teste foi verificar a existência de vulnerabilidades nas rotas da API fornecida, analisando possíveis falhas de Insecure Direct Object References (IDOR).

### 1. **Teste de Injeção de Código Malicioso**

A primeira etapa envolveu testar algumas rotas da API para verificar se seria possível a injeção de códigos que exporiam diretórios da aplicação.

**Método:**

- Foi enviada uma requisição para cada rota testada com um token de autenticação e as flags contendo os códigos maliciosos.
- As rotas testadas foram: `/api/consumer-units/` e `/api/tariffs/`, e outras sub-rotas.

**Resultado Esperado:**

- A resposta esperada era um código de status indicando que a injeção não estava sendo permitida.

**Resultado Obtido:**

- A aplicação gerou o código `412` e não permitiu a alteração na página. Os resultados podem ser vistos nas figuras 2.1 a 2.3.

<center>

Figura 2.1 - Resposta da requisição na rota `consumer-units`.

![Resposta da requisição na rota consumer-units](./img/math-idor-1.png)

</center>

<center>

Figura 2.2 - Resposta da requisição na rota `tariffs`.

![Resposta da requisição na rota tariffs](./img/math-idor-2.png)

</center>

<center>

Figura 2.3 - Resposta da segunda tentativa de requisição na rota `consumer-units`.

![Resposta da requisição na rota consumer-units](./img/math-idor-3.png)

</center>

### 2. **Teste de Acesso a diretorios**

Essa etapa envolveu testar algumas rotas da API para verificar se seria possível o acesso através da mudança dos parâmetros de acesso na rota.

**Método:**

- Foi enviada uma requisição para cada rota testada com um token de autenticação e o código para o caminho desejado.
- As rotas testadas foram as proposta para o [sub-grupo 2](../../../2024.2/url_mec_energia.txt).

**Resultado Esperado:**

- A resposta esperada era acesso aos diretórios que contém informações sobre usuários ou como ele são manipulados pela aplicação.

**Resultado Obtido:**

- A aplicação gerou os códigos `301` e `404` não permitindo o acesso às páginas. O resultado para a rota consumer-units pode ser visto na figura 2.4.

<center>

Figura 2.4 - Resposta da tentativa de requisição na rota `consumer-units`.

![Resposta da tentativa de requisição na rota consumer-units](./img/math-idor-4.png)

</center>

- Foi realizado o teste com a codificação da url. A aplicação retornou o código `404`. A resultado para o teste da rota `api/consumer-units/edit_consumer_unit_and_contract` pode ser vista na figura 2.5.

<center>

Figura 2.5 - Resposta da tentativa de requisição na rota `api/consumer-units/edit_consumer_unit_and_contract`.

![Resposta da tentativa de requisição na rota api/consumer-units/edit_consumer_unit_and_contract](./img/math-idor-5.png)

</center>

### 3. **Teste de inclusao de arquivos malicionsos**

Essa etapa envolveu testar a rota de upload da API para verificar se seria possível o enviar arquivos maliciosos ou fora do padrão esperado.

**Método:**

- Foi realizado o envio através do front com um arquivo de formato diferente do esperado.
- Foi enviada uma requisição para cada rota testada com um token de autenticação e do arquivo malicioso.
- A rota testada foi a `api/energy-bills/upload/`.

**Resultado Esperado:**

- A resposta esperada era o envio do arquivo com sucesso.

**Resultado Obtido:**

- Primeiramente, foi realizada a tentativa mal-sucedida pelo front. O resultado pode ser visto na figura 2.6.

<center>

Figura 2.6 - Resposta da tentativa de envio do arquivo malicioso.

![Resposta da tentativa de envio do arquivo malicioso.](./img/math-idor-6.png)

</center>

- Após, foi feita a tentativa com cURL. A aplicação gerou o código `412`. O resultado pode ser visto na figura 2.7.

<center>

Figura 2.7 - Resposta da tentativa de envio do arquivo malicioso com cURL.

![Resposta da tentativa de envio do arquivo malicioso com cURL](./img/math-idor-7.png)

</center>

---

## Histórico de Versões

| Versão | Data       | Descrição                               | Autor(es)                                        |
| ------ | ---------- | --------------------------------------- | ------------------------------------------------ |
| `1.0`  | 16/01/2025 | Adiciona relatório inicial da sprint 3. | [Gustavo Melo](https://github.com/gusrberto)     |
| `1.1`  | 16/01/2025 | Adiciona relatório da sprint 3.         | [Matheus Henrique](https://github.com/mathonaut) |
