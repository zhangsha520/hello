import gevent
import socket

p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# result = p.connect(('127.0.0.1', 1234))

try:
    with gevent.Timeout(5.0):
            p.connect(('127.0.0.1', 1234))
except gevent.timeout.Timeout:
    print("runtime connection timeout, please restart CNC")

except ConnectionRefusedError:
    print("runtime server refuse service, please restart CNC an runtime server")

print("socket connected")


while 1:

    msg = input('please input')

    # 防止输入空消息

    if not msg:

        continue

    p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码

    if msg == '1':

        break

p.close()
