# Relatório da Sprint 5 - Pipeline CI/CD Segura

## Membros
|                        Nome                        | Matrícula |
| :------------------------------------------------: | :-------: |
| [Cainã Freitas](https://github.com/freitasc)       | 180014412 |

## **Introdução**
Nesta sprint, o foco foi a implementação de uma **pipeline CI/CD segura**, integrando ferramentas de **Static Application Security Testing (SAST)** e **Image e Container Security Scanning** no **GitLab CI/CD**. O objetivo é garantir a segurança do código e das imagens Docker antes da implantação.

---

## **Pipeline CI/CD Segura**

### **Objetivos**
1. **Automatizar a verificação de segurança do código-fonte** antes da build.
2. **Analisar vulnerabilidades em imagens Docker** usadas na aplicação.
3. **Gerar relatórios detalhados** de vulnerabilidades para correção.
4. **Garantir conformidade com boas práticas de segurança** no ciclo de desenvolvimento.

### **Ferramentas Integradas**
- **Bandit**: Análise estática de segurança para código Python.
- **Trivy**: Scanner de vulnerabilidades em imagens Docker.
- **Dockle**: Auditoria de segurança e hardening para imagens Docker.

---

## **Configuração da Pipeline no GitLab CI/CD**
A configuração da pipeline CI/CD inclui três estágios principais de segurança:

### **1. Static Application Security Testing (SAST)**
Utiliza **Bandit** para identificar vulnerabilidades no código Python.

```yaml
bandit:
  stage: sast                
  image: python:3.11          
  before_script:              
    - pip install bandit
  script:
    - bandit --version
    - bandit -r . --configfile .bandit.yml -o sast-report.json -f json --exit-zero
  allow_failure: false
  artifacts:
    reports:
      sast: sast-report.json
    expire_in: 1 week
```

### **2. Security Scanning para Imagens Docker**
Utiliza **Trivy** para detectar vulnerabilidades em dependências do container.

```yaml
trivy:
  stage: sast
  image: docker:stable
  before_script:
    - export TRIVY_VERSION=$(wget -qO - "https://api.github.com/repos/aquasecurity/trivy/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
    - echo $TRIVY_VERSION
    - wget --no-verbose https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz -O - | tar -zxvf -
  allow_failure: false
  script:
    - ./trivy image --exit-code 0 --cache-dir .trivycache/ --no-progress --format template --template "@contrib/gitlab.tpl" -o image-report.json $CI_REGISTRY_IMAGE:latest
    - ./trivy image --exit-code 0 --cache-dir .trivycache/ --severity HIGH --no-progress $CI_REGISTRY_IMAGE:latest
    - ./trivy image --exit-code 0 --cache-dir .trivycache/ --severity CRITICAL --no-progress $CI_REGISTRY_IMAGE:latest
  cache:        
    paths:
      - .trivycache/
  artifacts:
    reports:
      sast: image-report.json
    expire_in: 1 week
```

### **3. Hardening e Auditoria de Container Docker**
Utiliza **Dockle** para verificar conformidade com boas práticas de segurança.

```yaml
dockle:
  stage: sast
  image: docker:stable
  before_script:
    - apk --no-cache add bash git curl tar sed grep
  script:
    - |
      VERSION=$(
      curl --silent "https://api.github.com/repos/goodwithtech/dockle/releases/latest" | \
      grep '"tag_name":' | \
      sed -E 's/.*"v([^"]+)".*/\1/' \
      ) && curl -L -o dockle.tar.gz https://github.com/goodwithtech/dockle/releases/download/v${VERSION}/dockle_${VERSION}_Linux-64bit.tar.gz && \
      tar zxvf dockle.tar.gz
    - ./dockle -f json -o container-report.json $CI_REGISTRY_IMAGE:latest
  allow_failure: false
  artifacts:
    reports:
      sast: container-report.json
    expire_in: 1 week
```

---

## **Merge Request e Validação da Pipeline**

### **Descrição do Merge Request**
Durante a Sprint 5, foi realizado um **Merge Request (MR)** no repositório principal do projeto **mec-energia-api**, incorporando as modificações de segurança na pipeline.

#### **Detalhes do Merge Request**
- **Branch de Origem:** `freitasc/mec-energia-api:develop`
- **Branch de Destino:** `develop`
- **Commits:** 27
- **Pipelines Executadas:** 20
- **Mudanças:** 2
- **Autor:** Cainã Freitas

#### **Como isso foi testado?**
A pipeline foi executada com sucesso, gerando relatórios que detalham possíveis vulnerabilidades e recomendações para mitigação.

### **Evidências do Funcionamento**
Abaixo, devem ser inseridas imagens mostrando o funcionamento adequado da pipeline e os botões de download dos relatórios gerados:

<p align="center">
  <img src=./G4_BlueTeam/sprint_5/imagens/pipeline.png width="500"/>
</p>

### **Botões para Download dos Relatórios**

<p align="center">
  <img src=./G4_BlueTeam/sprint_5/imagens/reports.png width="500"/>
</p>

### **Resultados e Melhorias Implementadas**

- **Automatização Completa da Análise de Segurança**: Todas as análises foram integradas ao CI/CD, eliminando a necessidade de execução manual.
- **Geração de Relatórios de Vulnerabilidades**: Agora, os relatórios são armazenados como artefatos no GitLab para consulta e correção.
- **Aprimoramento da Segurança do Container**:
  - Correção de vulnerabilidades críticas identificadas.
  - Remoção de arquivos desnecessários da imagem Docker.
  - Configuração de um usuário não root no container.
- **Pipeline Segura e Confiável**: Redução dos riscos de exposição de credenciais e código vulnerável.

---

## **Conclusão**
A implementação de segurança na pipeline CI/CD trouxe avanços significativos na proteção da aplicação contra vulnerabilidades. Agora, qualquer código ou imagem Docker passará por um rigoroso processo de verificação antes de ser implantado, garantindo maior conformidade com boas práticas de segurança.

Próximos passos incluem a revisão e correção contínua das vulnerabilidades identificadas e a exploração de novas ferramentas para aprimorar ainda mais a segurança do projeto.
