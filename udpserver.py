import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))

mensagem = 'Servidor: Olá, cliente! Tudo bem?'

while 1:
    date, address = s.recvfrom(4096)

if dados:
    print('Servidor')