import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client socket criado com sucesso!')

host = 'localhost'
port = 5433
message = 'Olá, servidor, firmeza?'

try:
    print('Cliente: {}'.format(message))
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('O servidor respondeu: {}'.format(dados))
finally:
    print('Cliente: fechando a conexão')
    s.close()