# Relatório Sprint 5 - Information Gathering

## Membros

|                        Nome                        | Matrícula |
| :------------------------------------------------: | :-------: |
| [Felipe Direito](https://github.com/felipedireito) | 190086971 |
|    [Gabriel Campello](https://github.com/G16C)     | 211039439 |
|    [Gustavo Melo](https://github.com/gusrberto)    | 211039457 |
|  [Matheus Henrique](https://github.com/mathonaut)  | 211029666 |

---

# Web Crawling com Burp Suite Spider

## Sobre

Este relatório documenta o uso do Burp Suite Spider para realizar web crawling no site da aplicação testada (homolog.mepaenergia.org). O objetivo é mapear a estrutura do site, identificar conteúdo oculto e reunir informações relevantes para uma futura análise de segurança.

## O que é Web Crawling?

Web crawling é o processo automatizado de navegação por páginas da web para coleta de informações. Ele é amplamente utilizado para indexação de sites por motores de busca, análise de vulnerabilidades e coleta de dados estruturados. No contexto de segurança, web crawlers ajudam a identificar possíveis superfícies de ataque, endpoints ocultos e conteúdo sensível exposto.

## Exemplo de uso Web Crawling 

### Configuração

1. Abrir o Burp Suite e configurar o navegador para utilizar o Burp Proxy.

2. Acessar o site da aplicação testada homolog.mepaenergia.org para capturar as primeiras requisições HTTP.

3. Navegar até a aba Target > Site Map e adicionar o site ao escopo de análise.

4. Iniciar o Burp Suite Spider para explorar as URLs e coletar informações.

### Resultado 
A seguir na Imagem 1 podemos ver o uso da ferramenta burp para realizar o Web Crawling no site de homologação do MEPA.

###### Imagem 1
![Burp Web Crawling](./img/image.png)

A partir das informações obtidas com o processo de web Crawling é possível realizar ataques mais precisos em cima de possíveis fragilidades do site como mostro a seguir na Imagem 2 e 3.

###### Imagem 2 

![Repeater](./img/image2.png) 
Imagem com requisição padrão para o site: GET /?callbackUrl=https%3A%2F%2Fhomolog.mepaenergia.org 
Resposta dentro do esperado OK.

###### Imagem 3
![Repeater2](./img/image3.png)
Imagem com requisição para site falso do tipo: GET /?callbackUrl=https%3A%2F%2Fevilsite.com
Resposta obtida: OK.

O que indica que a depender da requisição feita para autenticação de login podemos acabar entrando em uma url falsa sem notar. 

### Conclusão
Com o Web Crawling fui capaz de identificar um erro que anteriormente não tinha sido capaz de confirmar, e usando as ferramentas adequadas consegui, isso indica que algém com mior treinamento na parte de invasões poderia acabar toamndo controle de uma requisição feita por um usuário sem que api notasse. 

# Fingerprinting

É uma técnica utilizada na identificação de sistemas, aplicações ou dispositivos, buscando características únicas do sistema que podem ser exploradas. Como cabeçalhos HTTP, respostas a tipos específicos de pacotes e até assinatura digitais. É usado principalmente para **auditoria de segurança**, realizando um mapeamento do sistema, identificando potenciais vulnerabilidades.

## Banner Grabbing

```c
$ curl -I https://homolog.mepaenergia.org/

HTTP/1.1 200 OK
Server: nginx
Date: Wed, 12 Feb 2025 23:49:37 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 37596
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: Next.js
ETag: "mvz808uaf2t0c"
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

A requisição acima mostrou a pilha tecnológica da aplicação (Nginx e Next.js) o que poderia auxiliar a ataques direcionados por parte de usuários maliciosos, mas que no caso do MEPA não é uma grande problema já que o projeto é Open-Source.
Quanto aos cabeçalhos de segurança é possível ver que a aplicação já protege contra diversos tipos de ataques, como possível melhoria só daria a sugestão de mais dois cabeçalhos:
* `Content-Security-Police (CSP)`: Auxilia mais ainda na proteção contra XSS e outros ataques colocando restrições no carregamento de scripts.
* `Referrer-Policy: no-referrer` ou `strict-origin-when-cross-origin`: Controlam o envio de informações de referenciador para evitar o vazamento de dados sensíveis.

## Wafw00f (Identificação de WAF)

![Teste Wafw00f](https://github.com/user-attachments/assets/4499c82d-e26d-41cc-bd82-23f8cf93a37a)

O teste mostrou nenhum Web Application Firewall (WAF) foi detectado, o que pode deixar a aplicação vulnerável a alguns tipos de ataques entre eles:

* Cross-Site Scripting (XSS)
* Remote Code Execution (RCE)
* Directory Traversal
* Ataques de Força Bruta

Um WAF adiciona uma camada extra de defesa que pode detectar e bloquear automaticamente várias dessas ameaças antes delas sequer chegarem ao sistema.

### Conclusão

A análise realizada mostrou que a aplicação já conta com boas práticas de segurança, mas pode ser fortalecida com a adição de cabeçalhos como CSP e Referrer-Policy. Além disso, a ausência de um Web Application Firewall (WAF) pode expor o sistema a ataques como XSS e RCE. Implementar um WAF ajudaria a mitigar essas ameaças, adicionando uma camada extra de proteção.

## Histórico de Versões

| Versão | Data       | Descrição                               | Autor(es)                                        |
| ------ | ---------- | --------------------------------------- | ------------------------------------------------ |
| `1.0`  | 10/02/2025 | Criação do documento.  | [Gabriel Campello](https://github.com/G16C)      |
| `1.1`  | 13/02/2025 | Adição de testes de Fingerpriting.  | [Gustavo Melo](https://github.com/gusrberto)      |