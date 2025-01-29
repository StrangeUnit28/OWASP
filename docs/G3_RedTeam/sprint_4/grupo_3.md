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

- Envio de payloads maliciosos em campos de entrada

- Análise da resposta do servidor para identificar vulnerabilidades

- Testes de execução de scripts armazenados e refletidos

### Resultados

## Referências

- OWASP. "Cross Site Scripting (XSS)." Disponível em: https://owasp.org/www-community/attacks/xss/

- Mozilla Developer Network. "XSS Attack Prevention." Disponível em: https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#Cross-site_scripting_(XSS)

- Hack The Box Academy. "Cross-Site Scripting (XSS)." Disponível em: https://academy.hackthebox.com/module/103/section/965

