# Relatório Sprint 2 - Broken Authentication

|                            Nome                             | Matrícula |
| :---------------------------------------------------------: | :-------: |
| [Arthur Grandão de Mello](https://github.com/arthurgrandao) | 211039250 |

## Broken Authentication

### Enumeração de Usuários

A aplicação do Mec-Energia não possibilita a enumeração de usuários, visto que não é possível concluir a partir da resposta fornecida pelo sistema, se o usuário existe ou não.

### Força Bruta em senhas

Rodei o [ffuf](https://github.com/ffuf/ffuf) para tentar a força bruta no usuário admin padrão, contudo sem sucesso.

```
ffuf -u http://localhost:8000/api-auth/login/ -X POST -d "csrfmiddlewaretoken=oFy2gLkZ1Q6n09Hli7rtYd2KOTFnYUViuhZvKoiS4V0NF7t3l7ZbiLdi2lAX0jrJ&next=%2Fapi%2F&username=admin%40admin.com&password=FUZZ&submit=Log+in" -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: csrftoken=gMBDEN83df4AP8WSdaISuIlIoC5KczGB" -w /usr/share/wordlists/rockyou.txt -b "next-auth.callback-url=http://localhost:3000" -fc 200

admin                   [Status: 403, Size: 16380, Words: 2868, Lines: 642, Duration: 958ms]
```

\*\*admin é a senha correta

### Autenticação por acesso direto

O sistema está protegido de acessos por usuários não identificados que tentam acessar diretamente rotas reservadas.

### Tokens de sessão

Os tokens de sessão são muito robustos, portanto não podem ser simplesmente decifrados por força bruta.

Exemplo:

```
sessionid=by5pdv967opzdglkafxh6j66jdj5fvjf
```

Além disso, cada token gerado é suficientemente diferente do outro,
o que não nos oferece um padrão para diminuir o escopo da força bruta.

Exemplos:

```
sid1=022rzya5dlvgqyawmoj3f70gtwfjayb2
sid2=xosjdsr5g6r5rpti3443427ldkyyrrhw0
```

### Tokens de troca de senha

Ao solicitar a troca de senhas, ele envia esses links para que possamos trocar a senha.

Similarmente aos tokens de sessão, esses tokens são robustos e não podem ser facilmente burlados.

```
http://localhost:3000/definir-senha/?nome=José&token=ci5ek3-0d3d497f6dfd0d7eb1754ba731ce7866

http://localhost:3000/definir-senha/?nome=José&token=ci5eol-b25bdb817b8edf4964115bb1ab5b92ae

http://localhost:3000/definir-senha/?nome=José&token=ci5eqt-a80b4b37bb5687bb72f249ea92a12b36
```

### Fixação de sessão

Não encontrei uma maneira de alterar o cookie da sessão de forma viável para um ataque, no contexto dessa aplicação.

### Timeouts de sessão impróprios

Os cookies de sessão tem vida limitada e são devidamente excluídos após o fim da sessão.

## Dificuldades encontradas

Tive dificuldades em aplicar os conceitos aprendidos no curso na plataforma do Mec-Energia. E tive dificuldades em configurar o serviço de e-mails da plataforma, para que eu
pudesse testar as funcionalidades que dependem de recebimento de e-mails, como a troca de senha.

## Referências

Módulo "[Broken Authentication](https://academy.hackthebox.com/module/details/80)" [HTB Academy](https://academy.hackthebox.com/)
