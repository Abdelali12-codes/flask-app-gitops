from flask import Flask, url_for, template_rendered, request, jsonify
import os
from mysql.connector import Error
import mysql.connector

db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_database = os.getenv('DB_DATABASE', 'demo')
db_user = os.getenv('DB_USERNAME', '')
db_password = os.getenv('DB_PASSWORD', '')

app = Flask(__name__)

try:
    connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database
    )
    if connection.is_connected():
        print('Connected to MySQL database!')
except Error as e:
    print('Failed to connect to MySQL database:', e)
    raise e

@app.route('/')
def home():
    return 'up', 200
    
@app.route('/app')
def application():
    return jsonify({'name': 'flaskapp'})




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')