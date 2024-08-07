# IFSP-BACKEND-SQLtoNoSQL

Este projeto consiste em uma API Flask que realiza a conversão de uma base de dados relacional (Banco utilizado: MySQL) para uma base de dados não relacional (Banco utilizado: MongoDB).

## Estrutura do Projeto
```
IFSP-BACKEND-SQLToNoSQL/
│
├── flask_api/
│ ├── app/
│ │ ├── __init__.py
│ │ └── routes.py
│ └── run.py
├── dump.sql
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

```

## Como rodar este projeto?
Para definirmos um escopo, vamos configurar um ambiente virtual com as libs que precisamos.
```
python3 -m venv venv
```
Ativar seu ambiente virtual.
- Linux:
```
source venv/bin/activate
```
- Windows
```
venv/Scripts/activate
```

Instalar as dependências.
```
pip install flask pymysql pymongo
```
