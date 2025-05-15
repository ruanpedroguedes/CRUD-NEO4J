# 👥 NeoPeople - Sistema de Cadastro com Neo4j

Projeto simples de CRUD (Create, Read, Update, Delete) utilizando **Python** e **Neo4j**

---

## 🧠 Tecnologias Utilizadas

- 🐍 Python 3.10+
- 🧩 Neo4j 5.x
- 🔗 Driver oficial `neo4j` para Python

---

## 📁 Estrutura do Projeto

```

neopeople/
├── main.py              # Menu principal de interação
├── database.py          # Funções de conexão e CRUD
├── config.py            # Dados de acesso ao banco
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo

````

---

## ⚙️ Configuração

### 1. Instale o Python
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Instale o Neo4j Desktop
[https://neo4j.com/download/](https://neo4j.com/download/)

> ✅ Crie um banco local chamado `NeoPeopleDB`, configure o usuário como `admin_user` e a senha como `S3nh4F0rt3!`. Inicie o banco.

### 3. Clone ou baixe este repositório

```bash
git clone https://github.com/seu-usuario/neopeople.git
cd neopeople
````

### 4. Crie e ative o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # (Windows)
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do Banco (config.py)

```python
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "admin_user"
NEO4J_PASSWORD = "S3nh4F0rt3!"
```

---

## ▶️ Como executar

Com o ambiente virtual ativado, rode o sistema:

```bash
python main.py
```

Você verá o seguinte menu:

```
=== SISTEMA NEOPEOPLE ===
1 - Cadastrar pessoa
2 - Listar pessoas
3 - Atualizar nome
4 - Remover pessoa
0 - Sair
```

---

## 🧪 Exemplo de uso

1. Cadastrar: João - 25 anos
2. Atualizar: João → João da Silva
3. Remover: João da Silva
4. Listar: ver todos os registros no banco
