# TaskManager - Projeto em Python

Este projeto é um gerenciador simples de tarefas desenvolvido em Python. Ele permite criar e concluir tarefas, além de possuir testes automatizados para garantir o funcionamento correto das funcionalidades.

## 🔄 Gestão de Mudanças

Durante o desenvolvimento do projeto, não houve alteração significativa no escopo funcional inicialmente proposto. No entanto, ocorreram ajustes e melhorias na implementação para garantir melhor organização, compatibilidade e boas práticas de desenvolvimento.

Entre as principais adaptações realizadas estão:

- Organização do projeto no padrão `src/` para melhorar estrutura e compatibilidade com testes
- Ajustes nos imports e configuração do ambiente para funcionamento correto com pytest
- Refinamento do workflow de integração contínua no GitHub Actions
- Pequenas melhorias na estrutura da classe TaskManager para maior clareza

Essas mudanças foram realizadas com o objetivo de melhorar a qualidade técnica e a manutenção do projeto.
---

## 📌 Funcionalidades

- Criar tarefas
- Listar tarefas armazenadas
- Marcar tarefas como concluídas
- Estrutura simples e modular
- Testes automatizados com pytest

---
## 🧪 Como executar o projeto

Execute o comando:

pytest

Ou, se necessário:

python -m pytest

---
##⚙️ Integração Contínua (GitHub Actions)

Este projeto utiliza GitHub Actions para rodar testes automaticamente a cada push.

O workflow executa:

Instalação de dependências
Execução dos testes com pytest

---

## 🧠 Tecnologias utilizadas
Python 3

Pytest

GitHub Actions

Autor Vinicius de Souza 

---


## 🚀 Como executar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/vinisilva910/trabalho_techflow_solutions
cd trabalho_techflow_solutions
2. Criar ambiente virtual (opcional, recomendado)
python -m venv venv

Ativar o ambiente:

Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt


pip install pytest
---

