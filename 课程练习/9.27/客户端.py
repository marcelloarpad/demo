import socket

#1.创建一哥socket对象
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.连接到服务器
host = "www.baidu.com"
port = 80

server_add = socket.gethostbyname(host)
server = (server_add,port)
socket_client.connect(server)
#3.惊醒数据交换
socket_client.sendall('GET / HTTP/1.1\r\n\r\n'.encode())
message = socket_client.recv(4096).decode()
print(message)
#关闭连接

