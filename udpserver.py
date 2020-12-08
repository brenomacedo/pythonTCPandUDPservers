import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('socket criado com sucesso!')

host = 'localhost'
port = 5555

s.bind((host, port))

message = 'Servidor: Olá, cliente! Tudo bem?'

while 1:
    data, address = s.recvfrom(4096)

    if data:
        print('Servidor enviando mensagem...')
        s.sendto(data + (message.encode()), address)
