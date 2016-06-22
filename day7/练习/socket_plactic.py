import socket
ip_port = ('localhost',9090)
ss = socket.socket()
ss.bind(ip_port)
ss.listen(5)

while 1:
    print('waiting client request...')
    conn,addr  = ss.accept()
    while 1:
        try :
            reseved_mesg = conn.recv(1024)
            print(addr,'-client-request:',str(reseved_mesg,'utf8'))
            conn.send(reseved_mesg)
        except Exception as e:
            print('error：',e)
            break
conn.close()
def server1(conn,addr):
