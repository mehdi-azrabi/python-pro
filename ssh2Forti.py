import paramiko
import time
from getpass import getpass


ip = input("Please Enter Destination IP: ")
username = input("Please Enter User name: ")
password = input("Please Enter Password: ")

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip, port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'get system status\n')
time.sleep(2)
DEVICE_ACCESS.send(b'get router info bgp summary\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print(output.decode('ascii'))

SESSION.close()
