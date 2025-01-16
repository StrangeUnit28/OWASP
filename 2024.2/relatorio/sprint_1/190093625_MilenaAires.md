# Relatório Sprint 1 - Trilha de Estudos Blue Team

## Introdução
Para a primeira Sprint foi definida uma trila de estudos para introduzir o conteúdo e capacitação do time para executar as tarefas. A plataforma utilizada foi o [TryHackMe](https://tryhackme.com/r/dashboard), uma plataforma direcionada para cibersegurança utilizando laboratórios e exercícios. 

## Introdução à Segurança Ofensiva

Introduzindo o Blue Team o primeiro curso foi voltado para mostrar ambos os lados e entender como funciona a cibersegurança. Dentro desse curso há uma interface completa onde há uma máquina onde é possível testar os conhecimentos aprendidos, como por exemplo o Gobuster.

O **Gobuster** é uma ferramenta de código aberto utilizada principalmente em testes de penetração e auditorias de segurança. Ela realiza ataques de força bruta para descobrir recursos ocultos em servidores web, como diretórios, arquivos, subdomínios e endpoints. Gobuster é rápido e eficiente porque trabalha diretamente com requisições HTTP, eliminando a necessidade de renderização de páginas.
```
gobuster -u http://fakebank.thm -w wordlist.txt dir
```
_No comando acima, -u é usado para indicar o site que estamos escaneando, -w pega uma lista de palavras para iterar e encontrar páginas ocultas._

Principais funcionalidades:
- Descoberta de diretórios e arquivos: Identifica pastas e arquivos que podem estar ocultos ou desprotegidos no servidor.
- Força bruta de subdomínios: Descobre subdomínios associados a um domínio específico.
- Pesquisa em buckets de S3: Encontra buckets públicos ou mal configurados na AWS.

É amplamente utilizado por profissionais de segurança para encontrar vulnerabilidades, verificar configurações inadequadas e explorar informações que podem ser usadas em ataques mais avançados.

## CI/CD and Build Security (Build Security)

CI/CD (Continuous Integration/Continuous Deployment) é uma prática essencial no desenvolvimento de software moderno. Ela automatiza a integração, teste, entrega e implantação de software, permitindo que equipes entreguem funcionalidades rapidamente e com qualidade. Porém, essas pipelines podem introduzir riscos de segurança se não forem configuradas adequadamente.

### 1. O que é CI/CD?

Continuous Integration (CI):
- Desenvolvedores integram alterações de código em um repositório central com frequência.
- O código é automaticamente verificado, testado e validado por meio de ferramentas.
- Reduz conflitos de integração e permite detectar problemas cedo.

Continuous Deployment (CD):
- Automatiza a implantação de alterações aprovadas diretamente em ambientes de produção.
- Minimiza a intervenção humana e acelera o ciclo de entrega.


### 2. Benefícios do CI/CD
- Redução de erros manuais no processo de integração e entrega.
- Entregas rápidas e consistentes de novas funcionalidades.
- Feedback rápido sobre a qualidade do código.
- Melhoria da colaboração entre equipes.
  
### 3. Segurança no Contexto de CI/CD
Build Security, ou segurança em builds, refere-se à proteção do pipeline de CI/CD e do código contra vulnerabilidades e ataques. A pipeline pode se tornar um vetor de ataque se:
- Configurações de segurança inadequadas forem utilizadas.
- Ferramentas ou dependências desatualizadas estiverem presentes.
- Secrets (segredos, como tokens e senhas) forem mal gerenciados.

### 4. Principais Riscos de Segurança na Pipeline CI/CD
Exposição de Secrets:
- Credenciais mal armazenadas nos repositórios ou nos pipelines.
- Vazamento de chaves de API ou tokens de acesso.

Ataques de Supply Chain:
- Dependências de terceiros comprometidas.
- Modificação maliciosa de bibliotecas externas.

Execução Não Autorizada:
- Scripts maliciosos ou não verificados sendo executados na pipeline.
- Injeção em Variáveis de Ambiente:
- Manipulação de variáveis que podem afetar a execução do código.

Artefatos Não Verificados:
- Deploy de builds sem validação ou com vulnerabilidades conhecidas.

### 5. Práticas de Segurança para CI/CD

#### 5.1. Segurança na Integração Contínua (CI):
- Análise Estática de Código (SAST): Use ferramentas como SonarQube, Semgrep ou Checkmarx para verificar vulnerabilidades no código.
- Análise de Dependências (SCA): Ferramentas como Snyk, Dependabot ou OWASP Dependency-Check ajudam a identificar pacotes vulneráveis.
- Revisão de Código Automatizada: Configure revisões obrigatórias e automáticas antes de aprovar alterações para a branch principal.

#### 5.2. Segurança na Entrega Contínua (CD):
- Verificação de Artefatos: Assegure que apenas builds assinados e verificados sejam promovidos entre ambientes. Use assinaturas digitais para autenticar artefatos.
- Ambientes Isolados: Configure ambientes segregados para desenvolvimento, teste e produção.
- Deploy Canary: Implante alterações para uma pequena parcela de usuários antes do rollout completo.

### 6. Protegendo a Infraestrutura do CI/CD
Controle de Acesso:
- Adote o princípio de privilégio mínimo (least privilege).
- Use autenticação multifator (MFA) para acessar os sistemas de CI/CD.

Segurança na Pipeline:
- Configure triggers e aprovações manuais para deploys críticos.
- Monitore o histórico de execuções e altere permissões regularmente.

Segurança dos Runners/Agentes:
- Use runners dedicados para builds críticos.
- Mantenha os agentes atualizados com os últimos patches de segurança.

Auditoria e Logs:
- Habilite auditorias completas e logging para detectar acessos não autorizados ou anomalias.
