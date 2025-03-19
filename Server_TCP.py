import socket

HOST = '127.0.0.1'  # Endereço do servidor (localhost)
PORT = 65432        # Porta do servidor

question1 = "1️⃣O que faz a função socket.bind() em um servidor TCP?\na) Conecta o servidor a um cliente automaticamente.\nb) Define o endereço e a porta onde o servidor vai escutar conexões.\nc) Envia uma mensagem para um cliente conectado.\nd) Fecha o socket do servidor."
question2 = "2️⃣ Qual é a principal diferença entre TCP e UDP?\na) TCP é orientado a conexão e garante entrega, enquanto UDP é mais rápido, mas sem garantia de entrega.\nb) UDP sempre é mais seguro que TCP.\nc) TCP só pode ser usado para páginas web e UDP só para jogos.\nd) UDP não funciona em redes locais."
question3 = "3️⃣ O que significa a sigla API em tecnologia?\na) Aplicativo Para Internet\nb) Área de Programação Integrada\nc) Interface de Programação de Aplicações\nd) Arquitetura de Processamento Inteligente"
answer = ['b', 'a', 'c']

# Criando o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor aguardando conexão na porta {PORT}...")

# Aceita a conexão do cliente
connectionSocket, addr = server_socket.accept()
print(f"Conectado a {addr}")

# Envia as perguntas ao cliente
connectionSocket.sendall(question1.encode())
connectionSocket.sendall(question2.encode())
connectionSocket.sendall(question3.encode())
print("Questões enviadas ao cliente")

# Recebe a resposta do cliente
response1 = connectionSocket.recv(1024).decode()
response2 = connectionSocket.recv(1024).decode()
response3 = connectionSocket.recv(1024).decode()
print(f"Respostas: {response1, response2, response3}")

acertos = 0
erros = 0

# Realizando a correção das questões
if response1 == answer[0]:
    result1 = "Questão 1: Correta"
    acertos += 1
else:
    result1 = "Questão 1: Incorreta"
    erros += 1
    
if response2 == answer[1]:
    result2 = "Questão 2: Correta"
    acertos += 1
else:
    result2 = "Questão 2: Incorreta"
    erros += 1
    
if response3 == answer[2]:
    result3 = "Questão 3: Correta"
    acertos += 1
else:
    result3 = "Questão 3: Incorreta"
    erros += 1
   
# Retornando a correção
connectionSocket.sendall(result1.encode())
connectionSocket.sendall(result2.encode())
connectionSocket.sendall(result3.encode())
connectionSocket.sendall(acertos.encode())
connectionSocket.sendall(erros.encode())

# Fecha a conexão
connectionSocket.close()
server_socket.close()
