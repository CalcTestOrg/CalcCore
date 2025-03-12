import socket
import pyodbc
import os
import subprocess

server_base = r'localhost\SQLEXPRESS'  
database = 'CalculatorDB'
username = ''
password = ''

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_base};DATABASE={database};Trusted_Connection=yes'


IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")

request = conn.recv(1024).decode()

try:
        expression = request
        result = eval(expression)  

        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()

        insert_query = "INSERT INTO Results (expression, result) VALUES (?, ?)"
        values = (expression, result)
        cursor.execute(insert_query, values)
        conn_db.commit()

        result_str = f"Результат: {result} успешно записан"
        conn.send(result_str.encode())

        cursor.close()
        conn_db.close()

except Exception as e:
        print(f"Ошибка: {e}")
        result_str = f"Ошибка: {e}"
        conn.send(result_str.encode())

conn.close()
server.close()
