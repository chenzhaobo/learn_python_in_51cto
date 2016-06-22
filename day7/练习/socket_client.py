import socket
sk = socket.socket()
ip_port = ('localhost',9090)
sk.connect(ip_port)
while 1:
    user_input = input('>>:')
    sk.send(bytes(user_input,'utf8'))
    conn = sk.recv(1024)
    print('server respone:',str(conn,'utf8'))
conn.colse()