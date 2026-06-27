# TaskManager - Projeto em Python

Este projeto é um gerenciador simples de tarefas desenvolvido em Python. Ele permite criar e concluir tarefas, além de possuir testes automatizados para garantir o funcionamento correto das funcionalidades.

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


⚙️ Integração Contínua (GitHub Actions)

Este projeto utiliza GitHub Actions para rodar testes automaticamente a cada push.

O workflow executa:

Instalação de dependências
Execução dos testes com pytest

---

## 📁 Estrutura do Projeto


src/
│
├── init.py
└── tasks.py

tests/
└── test_tasks.py

.github/
└── workflows/
└── python.yml


---
## 🧠 Tecnologias utilizadas
Python 3
Pytest
GitHub Actions
📌 Autor Vinicius de Souza 


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

Se não houver requirements.txt, instalar manualmente:

pip install pytest
---

