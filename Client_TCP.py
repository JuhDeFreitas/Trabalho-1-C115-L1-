import socket

HOST = '127.0.0.1'  # Endereço do servidor (localhost)
PORT = 65432        # Porta do servidor

# Criando o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recebe as perguntas do servidor
question1 = client_socket.recv(1024).decode()
question2 = client_socket.recv(1024).decode()
question3 = client_socket.recv(1024).decode()
print(question1)
print(question2)
print(question3)

# Envia as respostas ao servidor
answer1 = 'b'  # Resposta para a pergunta
answer2 = "a"  # Resposta para a pergunta
answer3 = "a"  # Resposta para a pergunta
client_socket.sendall(answer1.encode())
client_socket.sendall(answer2.encode())
client_socket.sendall(answer3.encode())

# Rececbendo os resultados do servidor
result1 = client_socket.recv(1024).decode()
result2 = client_socket.recv(1024).decode()
result3 = client_socket.recv(1024).decode()

# Mostrando os resultados do questionário
print(result1)
print(result2)
print(result3)

# Fecha a conexão
client_socket.close()
