from socket import *
from feistel_cipher import feistel_cipher

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

key = [3, 2, 0, 1]

while 1:
  #Cria um socket para tratar a conexao do cliente
  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024)

  decoded_sentence = feistel_cipher(sentence, key)
  capitalizedSentence = decoded_sentence.upper()
  
  print('Mensagem recebida pelo servidor:', sentence)
  print('Mensagem decriptografada pelo servidor:', capitalizedSentence)
  
  encoded_sentence = feistel_cipher(decoded_sentence, key)

  print('Mensagem criptografada pelo servidor:', encoded_sentence)

  connectionSocket.send(encoded_sentence)
  connectionSocket.close()