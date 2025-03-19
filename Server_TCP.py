import socket
import json

HOST = 'localhost'
PORT = 3000

question1 = "1️⃣O que faz a função socket.bind() em um servidor TCP?\na) Conecta o servidor a um cliente automaticamente.\nb) Define o endereço e a porta onde o servidor vai escutar conexões.\nc) Envia uma mensagem para um cliente conectado.\nd) Fecha o socket do servidor."
question2 = "2️⃣ Qual é a principal diferença entre TCP e UDP?\na) TCP é orientado a conexão e garante entrega, enquanto UDP é mais rápido, mas sem garantia de entrega.\nb) UDP sempre é mais seguro que TCP.\nc) TCP só pode ser usado para páginas web e UDP só para jogos.\nd) UDP não funciona em redes locais."
question3 = "3️⃣ O que significa a sigla API em tecnologia?\na) Aplicativo Para Internet\nb) Área de Programação Integrada\nc) Interface de Programação de Aplicações\nd) Arquitetura de Processamento Inteligente"
answer = ['b', 'a', 'c']
number_of_questions = 3

# Criando o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))    #atribui um endereço/porta ao servidor
server_socket.listen(1)             #conecta a apenas um cliente por vez
print(f"Aguardando conexão na porta {PORT}...")

# Aceita conexão com o Client
connection_socket, addr_client = server_socket.accept()
print(f"Conexão estabelecida.\nCliente: {addr_client}")

# Envio das questões
connection_socket.send(str(number_of_questions).encode())
connection_socket.send(question1.encode())
connection_socket.send(question2.encode())
connection_socket.send(question3.encode())
print("Questões enviadas ao cliente.")

# Recebe as respostas do Client
response = list(connection_socket.recv(1024).decode())
print(f"Respostas recebidas.")

# Verifica as respostas
status = [False] * len(response)

for i in range(number_of_questions):
    if response[i] == answer[i]:
        status[i] = True
    else:
        status[i] = False

# Envia o resultado do questionário ao Client (Formato JSON)
connection_socket.send(json.dumps(status).encode())
print("Resultado do questionário enviado.")
