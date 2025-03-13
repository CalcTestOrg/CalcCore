import tkinter as tk
import socket

IP = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))  

def send_to_server(expression):
    client.send(expression.encode())  
    response = client.recv(1024).decode()  
    result_var.set(response)  

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label1 = tk.Label(root, text="Первое число:")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Второе число:")
label2.grid(row=1, column=0)

result_var = tk.StringVar()
result_label = tk.Label(root, text="Результат:")
result_label.grid(row=2, column=0)

result_display = tk.Label(root, textvariable=result_var)
result_display.grid(row=2, column=1)

def add():
    send_to_server(f"{entry1.get()} + {entry2.get()}")

def subtract():
    send_to_server(f"{entry1.get()} - {entry2.get()}")

def multiply():
    send_to_server(f"{entry1.get()} * {entry2.get()}")

def divide():
    send_to_server(f"{entry1.get()} / {entry2.get()}")

add_button = tk.Button(root, text="Сложить", command=add)
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="Вычесть", command=subtract)
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="Умножить", command=multiply)
multiply_button.grid(row=3, column=2)

divide_button = tk.Button(root, text="Делить", command=divide)
divide_button.grid(row=4, column=0)

def on_closing():
    client.close()  
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
