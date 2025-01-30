# Relatório Sprint 4 - Cross-Site Scripting (XSS)

## Membros

| Nome | Matrícula |
| :--: | :-------: |
| [Mateus Fidelis](https://github.com/MatsFidelis) | 200073184 |
| [Pablo Guilherme](https://github.com/PabloGJBS) | 200025791 |
| [Pedro Lucas](https://github.com/AlefMemTav)     | 190115548 |
| [Rafael Bosi](https://github.com/strangeunit28) | 211029559 |

---

## Sobre 

Este relatório documenta os resultados alcançados durante a Sprint 3, com foco na vulnerabilidade conhecida como **Cross-Site Scripting (XSS)**. O objetivo foi explorar, identificar e compreender como essa vulnerabilidade pode comprometer sistemas reais, além de detalhar testes realizados na API do MEC Energia, os desafios enfrentados e os aprendizados adquiridos pela equipe.

---

## O que é Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) é uma vulnerabilidade de segurança que permite a injeção de scripts maliciosos em páginas da web visualizadas por outros usuários. O XSS pode ser explorado para roubo de informações, sequestro de sessões e manipulação da interface do usuário. Ele se divide em três principais categorias:

- **XSS Refletido:** O código malicioso é enviado ao servidor e retornado na resposta HTTP sem sanitização, afetando usuários que clicam em links maliciosos.

- **XSS Armazenado:** O código injetado é armazenado no banco de dados da aplicação e executado sempre que a página for carregada.

- **XSS baseado em DOM:** O ataque ocorre no lado do cliente, manipulando o DOM sem interagir diretamente com o servidor.

## Exemplo de Cross-Site Scripting (XSS)

Um exemplo simples de XSS Refletido em um formulário vulnerável seria:

```JavaScript
<input type="text" name="busca" value="<script>alert('XSS')</script>">
```
Se a aplicação não sanitizar corretamente a entrada do usuário, o código JavaScript será executado no navegador do usuário, permitindo ataques como roubo de cookies e modificação da interface da página.

## Teste de Cross-Site Scripting (XSS) no MEC Energia

### Metodologia

Para avaliar a segurança da API do MEC Energia, realizamos testes utilizando diferentes vetores de ataque XSS, incluindo:

- Envio de payloads maliciosos em campos de entrada.
- Análise da resposta do servidor para identificar vulnerabilidades.
- Testes de execução de scripts armazenados e refletidos.

### Testes de XSS - Pablo e Rafael Bosi

Todos os testes de XSS foram realizados no ambiente de homologação **<https://energia.lappis.rocks>**.

#### Testes Stored XSS

Realizamos tentativas de Stored XSS, que consistem na inserção de um código malicioso via campos de envio de respostas, como campos de edição de informações, conforme demonstrado a seguir:

![alt text](/docs/G3_RedTeam/sprint_4/imagesSprint4/TesteStoredEditarUnidade.png)

Ao realizar o envio desse e de outros códigos de teste para XSS, não obtivemos sucesso em alcançar essa vulnerabilidade. A aplicação funcionou normalmente, apenas editando o campo como deveria ser.

#### Testes Diretamente pela URL

Realizamos também testes diretamente por URLs, focando em URLs que aceitavam parâmetros, como esta: <https://energia.lappis.rocks/api/auth/signin?csrf=true>

Nesta URL, por exemplo, modificamos o parâmetro `csrf=true` para verificar se a aplicação refletia o valor do parâmetro na página ou no DOM.

Alguns dos Payloads XSS utilizados:

```markdown
> `https://energia.lappis.rocks/api/auth/signin?csrf=<script>alert('XSS')</script>`  

> `https://energia.lappis.rocks/api/auth/signin?csrf=%3Cscript%3Ealert('XSS')%3C%2Fscript%3E`

> `https://energia.lappis.rocks/api/auth/signin?csrf=%3Cimg%20src%3D%22x%22%20onerror%3D%22alert('XSS')%22%3E`
```

Após os envios, verificamos o código-fonte da página pela ferramenta de inspecionar elemento, mas o payload não foi refletido e nem processado.

#### Testes de XSS diretamente pelo inspecionar elementos

Foram realizados também testes dentro do inspecionar elementos. Na tentativa, buscamos por elementos que exibem conteúdo dinâmico, como por exemplo na imagem a seguir:

![alt text](/docs/G3_RedTeam/sprint_4/imagesSprint4/TesteXSSInspecionarElemento.png)

Mas, novamente, após testar em diversos locais, não obtivemos sucesso.

#### Teste com OWASP ZAP

Por fim, realizamos um teste utilizando a ferramenta OWASP ZAP na tentativa de identificar alguma vulnerabilidade de XSS. Porém, não encontramos. Em contrapartida, ao rodarmos uma análise completa no MEPA, encontramos o seguinte alerta:

![alt text](/docs/G3_RedTeam/sprint_4/imagesSprint4/vulnerabilidadeCritica.png)

A vulnerabilidade de risco apresentou uma possível brecha na versão 12.3.0 da lib Next.js.

## Referências

- OWASP. "Cross Site Scripting (XSS)." Disponível em: https://owasp.org/www-community/attacks/xss/

- Mozilla Developer Network. "XSS Attack Prevention." Disponível em: https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#Cross-site_scripting_(XSS)

- Hack The Box Academy. "Cross-Site Scripting (XSS)." Disponível em: https://academy.hackthebox.com/module/103/section/965

