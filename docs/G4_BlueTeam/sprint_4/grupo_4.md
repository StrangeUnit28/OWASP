# Relatório da Sprint 4 - Análise do Container Docker com Dockle

## Membros
|                        Nome                        | Matrícula |
| :------------------------------------------------: | :-------: |
| [Cainã Freitas](https://github.com/freitasc)       | 180014412 |

## **Introdução**
Neste relatório, detalhamos a experiência ao configurar e utilizar o **Dockle** como ferramenta de análise de segurança para garantir boas práticas e identificar vulnerabilidades em imagens Docker utilizadas pelo projeto **mec-energia-api**. O Dockle foi configurado para rodar manualmente, permitindo verificar a configuração e conformidade da imagem Docker antes de integrá-la ao pipeline.

---

## **Como o Dockle funciona**

O **Dockle** é uma ferramenta de segurança que realiza uma análise da conformidade de imagens Docker, verificando configurações inseguras, práticas de hardening recomendadas e potenciais vulnerabilidades. 

### **Principais Funcionalidades**
1. **Análise de Conformidade**: Verifica se a imagem Docker segue as boas práticas de segurança, como a minimização de privilégios e o uso de imagens base seguras.
2. **Hardening da Imagem Docker**: Detecta se a imagem Docker foi configurada adequadamente para reduzir a superfície de ataque.
3. **Verificação de Variáveis de Ambiente**: Inspeciona se variáveis sensíveis estão expostas nas configurações da imagem.
4. **Recomendações de Melhoria**: Gera relatórios com recomendações práticas de segurança para melhorar a configuração da imagem Docker.

### **Etapas de Funcionamento**
1. **Análise da Imagem Docker**:
   - Examina o Dockerfile e a imagem gerada para identificar falhas de configuração e práticas inseguras.
2. **Verificação contra Boas Práticas de Segurança**:
   - Compara as configurações da imagem com um conjunto de recomendações de hardening, como a definição de usuários não privilegiados e a remoção de ferramentas desnecessárias.
3. **Geração de Relatórios**:
   - Produz relatórios em formato de texto ou JSON, detalhando os problemas encontrados e sugerindo melhorias.

---

## **Execução Manual**

### Pré-requisitos
Certifique-se de que o Docker e o Dockle estão instalados no ambiente local:

```bash
curl -sSL https://github.com/goodwithtech/dockle/releases/download/v0.4.1/dockle-linux-amd64.tar.gz | tar xzv
sudo mv dockle /usr/local/bin/
```

### Comando para análise

- Para realizar uma análise da imagem Docker:

```bash
dockle -i mepa-api:latest-dev
```

### Exemplo de Saída

<p align="center">
  <img src=./G4_BlueTeam/sprint_4/imagens/example.png width="500"/>
</p>

---

## **Resultados Obtidos**

#### Resumo dos Achados:
| Nível de Criticalidade | Ocorrências | Categoria |
|------------------------|-------------|-----------|
| FATAL                  | 10          | **CIS-DI-0010**: Do not store credentials in environment variables/files |
| WARN                   | 1           | **CIS-DI-0001**: Create a user for the container |
| INFO                   | 6           | **CIS-DI-0005**: Enable Content trust for Docker, **CIS-DI-0006**: Add HEALTHCHECK instruction, **CIS-DI-0008**: Confirm safety of setuid/setgid files, **DKL-LI-0003**: Only put necessary files |

---

## **Vulnerabilidades Notáveis**

### **CIS-DI-0010: Do not store credentials in environment variables/files**
- **Descrição**: Foi identificado que múltiplos arquivos de configuração `settings.py` em diversos pacotes Python dentro do ambiente Docker contêm informações sensíveis, o que representa um risco de segurança, pois credenciais podem ser facilmente expostas.
- **Arquivos Suspeitos**:
  - `usr/local/lib/python3.11/site-packages/tutorial/settings.py`
  - `usr/local/lib/python3.11/site-packages/scipy/_lib/cobyqa/settings.py`
  - `usr/local/lib/python3.11/site-packages/djangorestframework_camel_case/settings.py`
  - `usr/local/lib/python3.11/site-packages/debug_toolbar/panels/settings.py`
  - `usr/local/lib/python3.11/site-packages/debug_toolbar/settings.py`
  - `usr/local/lib/python3.11/site-packages/easyaudit/settings.py`
  - `usr/local/lib/python3.11/site-packages/jedi/settings.py`
  - `usr/local/lib/python3.11/site-packages/django_extensions/settings.py`
  - `usr/local/lib/python3.11/site-packages/pytest_order/settings.py`
  - `usr/local/lib/python3.11/site-packages/rest_framework/settings.py`
- **Recomendação**: Evitar armazenar credenciais dentro de arquivos de configuração ou variáveis de ambiente. Usar soluções como **Docker Secrets**, **env vars**, ou **vaults** para gerenciar credenciais de forma segura.

---

### **CIS-DI-0001: Create a user for the container**
- **Descrição**: A configuração do container Docker está utilizando o usuário root, o que representa um risco de segurança.
- **Recomendação**: Criar um usuário não privilegiado para o container e configurar a execução dos processos com ele, reduzindo o risco de comprometimento da imagem.

---

### **CIS-DI-0005: Enable Content Trust for Docker**
- **Descrição**: Não foi ativado o **Content Trust** para as imagens Docker, o que pode permitir que imagens não verificadas ou comprometidas sejam baixadas.
- **Recomendação**: Ativar o `DOCKER_CONTENT_TRUST=1` antes de realizar operações de `docker pull` ou `docker build` para garantir que apenas imagens verificadas sejam utilizadas.

---

### **CIS-DI-0006: Add HEALTHCHECK instruction to the container image**
- **Descrição**: A imagem do Docker não inclui um comando de **HEALTHCHECK**, o que pode dificultar a monitoração da saúde do container em tempo de execução.
- **Recomendação**: Adicionar a instrução `HEALTHCHECK` no Dockerfile para garantir que a saúde do container seja monitorada e alertada quando necessário.

---

### **CIS-DI-0008: Confirm safety of setuid/setgid files**
- **Descrição**: Diversos arquivos setuid e setgid foram encontrados na imagem Docker, o que pode ser uma possível vulnerabilidade, já que esses arquivos podem ser usados para escalonamento de privilégios.
- **Arquivos setuid/setgid**:
  - Setuid: `usr/bin/passwd`, `usr/bin/chsh`, `usr/bin/chfn`, `usr/bin/gpasswd`, `usr/bin/umount`, `usr/bin/su`, `usr/bin/newgrp`, `usr/bin/mount`
  - Setgid: `usr/bin/chage`, `usr/bin/crontab`, `usr/sbin/unix_chkpwd`, `usr/bin/expiry`
- **Recomendação**: Rever e, se possível, remover arquivos setuid/setgid desnecessários ou potencialmente inseguros, garantindo que apenas arquivos essenciais para o funcionamento da aplicação permaneçam com essas permissões.

---

### **DKL-LI-0003: Only put necessary files**
- **Descrição**: Foi identificado que arquivos desnecessários foram incluídos no diretório do projeto, o que pode aumentar a superfície de ataque e deixar informações desnecessárias expostas.
- **Arquivos Desnecessários**:
  - `app/mepa-api/.DS_Store`
  - `app/mepa-api/scripts/.DS_Store`
- **Recomendação**: Remover arquivos desnecessários como `.DS_Store` antes de criar a imagem Docker ou incluí-los no controle de versão.

---

## **Conclusão**

- **Repensar a versão que a imagem usa de Base pelo Docker**: A imagem base utilizada é a `python:3.11.9-slim-bookworm`, que possui vulnerabilidades críticas herdados da imagem `debian:12-slim`. Recomenda-se pesquisa e escolha de uma imagem base mais segura. Na data atual as imagens com final `-slim-bookworm` estão na versão `3.14.0a4` e `3.14.0a5`, 3 updates minors a frente da versão utilizada e com correções de segurança para várias das vulnerabilidades encontradas.
- **Ações Imediatas**: Implementar as correções de **CIS-DI-0010** para evitar o armazenamento de credenciais inseguras e garantir a segurança do container com a criação de um usuário não root e o uso de **Content Trust**.
- **Melhorias Recomendadas**: Revisar a inclusão de arquivos setuid/setgid e desnecessários, além de adicionar a instrução `HEALTHCHECK` para melhorar a manutenção e operação do container em produção.
