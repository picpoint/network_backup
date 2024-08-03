import paramiko
from copy_files_module import copy_files

FOLDER_SRC = "src"
FOLDER_DST = "dst"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.10.100', username='admin', password='00000')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())

ssh.close()



# copy_files(FOLDER_SRC, FOLDER_DST)