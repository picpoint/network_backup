import paramiko
from passwd import access


hostname = access['hostname']
user = access['user']
password = access['password']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=user, password=password)

ssh = client.open_sftp()
local_file_path = "readme.txt"
remove_file_path = "/tmp/readme.txt"

ssh.put(local_file_path, remove_file_path)
ssh.close()
client.close()