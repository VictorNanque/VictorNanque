import socket
ports = [21,22,80,8080,8000,443,53]
host = str(input('Digite a url ou o ip:'))
for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(5)
    code = cliente.connect_ex((host,port))
    if code ==0:
        print('aberta',port)
    else:
        print('fechada',port)