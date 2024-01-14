import socket
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = "192.168.31.228"
port = 8888
addr = (ip, port)
socket_server.bind(addr)
print(ip)
#监听
socket_server.listen(8)
print("已设置好")

client_fd,client_ip = socket_server.accept()
print(client_fd)
print(client_ip)

#shuju
client_fd.sendall("nihao".encode("gbk"))
data = client_fd.recv(1024).decode("gbk")
print(data)
#关闭
client_fd.close()
socket_server.close()