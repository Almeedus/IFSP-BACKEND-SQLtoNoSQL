from flask import Blueprint, jsonify
import pymysql
from pymongo import MongoClient

bp = Blueprint('main', __name__)

@bp.route('/convert', methods=['GET'])
def convert():
    # Conectar ao MySQL
    mysql_conn = pymysql.connect(
        host='localhost',
        user='root',
        password='senha',
        db='minha_base'
    )
    cursor = mysql_conn.cursor(pymysql.cursors.DictCursor)
    
    # Conectar ao MongoDB
    mongo_client = MongoClient('mongodb://localhost:27017/')
    mongo_db = mongo_client['minha_base_nosql']
    
    # Converter dados de usuários
    cursor.execute('SELECT * FROM usuario')
    usuarios = cursor.fetchall()
    mongo_db['usuario'].insert_many(usuarios)
    
    # Converter dados de endereços
    cursor.execute('SELECT * FROM endereco')
    enderecos = cursor.fetchall()
    mongo_db['endereco'].insert_many(enderecos)
    
    # Converter dados de telefones
    cursor.execute('SELECT * FROM telefone')
    telefones = cursor.fetchall()
    mongo_db['telefone'].insert_many(telefones)
    
    # Fechar conexões
    cursor.close()
    mysql_conn.close()
    mongo_client.close()
    
    return jsonify(message='Dados convertidos com sucesso!'), 200

def init_app(app):
    app.register_blueprint(bp)
