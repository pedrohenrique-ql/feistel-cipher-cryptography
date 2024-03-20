from socket import *
from feistel_cipher import feistel_cipher

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

key = b"mysecretk"

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))

#Recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')
encoded_message = feistel_cipher(bytes(message, 'utf-8'), key)

print('Mensagem do usuário:', message)
print('Mensagem do usuário criptografada:', encoded_message)

clientSocket.send(encoded_message)

#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
decoded_server_message = feistel_cipher(modifiedMessage, key)

print('Mensagem recebida pelo servidor:', modifiedMessage)
print('Mensagem do servidor decriptografada:', decoded_server_message)

clientSocket.close()