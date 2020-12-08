import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print('A conexão falhou')
        print('Erro: {}'.format(error))
        sys.exit()

    print('Socket criado com sucesso!')

    target_host = input('Digite o host ou o ip a ser conectado: ')
    target_port = int(input('Digite a porta a ser conectada: '))

    try:
        s.connect((target_host, target_port))
        print('cliente tcp conectado com sucesso! no host {} e na porta {}'.format(target_host, target_port))
        s.shutdown(2)
    except socket.error as error:
        print('Não foi possível conectar no host')
        print('Erro: {}'.format(error))
        sys.exit()

if __name__ == "__main__":
    main()