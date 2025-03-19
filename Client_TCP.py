import socket
import json

HOST = 'localhost'
PORT = 3000

# Criando o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Conexão com o servidor estabelecida.")

# Recebe o numero de questões a ser recebidas do servidor
number_of_questions = int(client_socket.recv(1024).decode())

question = []
# Recebe as questões do servidor
for i in range(number_of_questions):
    question.append(client_socket.recv(1024).decode())

# Imprime as informações recebidas
for i in range(number_of_questions):
    print(question[i])

# Solicita as respostas para cada questão
response = []
print("\nInsira abaixo as respostas das quetões: ")
for i in range(number_of_questions):
    response.append(input(f"Questão {i}: "))

# Envia as respostas ao servidor
client_socket.send(''.join(response).encode())
print("\nRespostas enviadas ao servidor.")

# Recebe o resultado do questionário
result = json.loads(client_socket.recv(1024).decode())
print(f"Resultado recebido.")

#Imprimindo o resultado do questionário

correct = 0
wrong = 0

print("\nResultado do Questionário:")
for i in range(number_of_questions):
    if result[i] == True:
        print(f"Questão {i+1}: Correta ")
        correct += 1
    else:
        print(f"Questão {i+1}: Incorreta ")
        wrong += 1

print(f"\nAcertos: {correct}")
print(f"Erros: {wrong}")

nota = (correct / len(result)) * 100
print("Nota: ", round(nota, 2))
