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
