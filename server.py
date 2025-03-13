import socket
import pyodbc

server_base = r'localhost\SQLEXPRESS'  
database = 'CalculatorDB'

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_base};DATABASE={database};Trusted_Connection=yes'

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")

while True:
    try:
        request = conn.recv(1024).decode().strip()
        if not request:
            break  

        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in request):
            result_str = "Ошибка: Некорректный ввод. Разрешены только числа и операторы +, -, *, /"
        else:
            expression = request
            result = eval(expression)  

            conn_db = pyodbc.connect(dsn)
            cursor = conn_db.cursor()

            insert_query = "INSERT INTO Results (expression, result) VALUES (?, ?)"
            values = (expression, result)
            cursor.execute(insert_query, values)
            conn_db.commit()

            result_str = f"Результат: {result} успешно записан"

            cursor.close()
            conn_db.close()

        conn.send(result_str.encode())

    except Exception as e:
        conn.send(f"Ошибка: {e}".encode())

print("Клиент отключился, сервер завершает работу.")
conn.close()
server.close()
