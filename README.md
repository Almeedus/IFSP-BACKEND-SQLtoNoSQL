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

## Preparando o ambiente 1/2
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
## Preparando o ambiente 2/2
Instale o DUMP do banco de dados.
```
mysql -u root -p < dump.sql
```

## Inicie a aplicação
Inicie a aplicação pelo arquivo run.py
```
python run.py
```

## Testando a aplicação
Utilize de algum software de consumo de endpoint, extensão do vscode ou se preferir pelo comando cURL abaixo
```
curl http://127.0.0.1:5000/convert
```

Seguindo esses passos, você deve conseguir testar a API e verificar que a conversão de dados de MySQL para MongoDB está funcionando corretamente pelo retorno.
```
127.0.0.1 - - [07/Aug/2024 19:18:48] "GET /convert HTTP/1.1" 200 -
```
E pelo JSON.
```
{
  "message": "Dados convertidos com sucesso!"
}
```

# Dependência do Projeto
- Flask
- Pymongo
- Pymysql