import time
import os
import paramiko
from passwd import access_server_backup
from passwd import access_server_arhivs
import datetime


hostname_server_backup = access_server_arhivs['hostname']
user_server_backup = access_server_arhivs['user']
password_server_backup = access_server_arhivs['password']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname_server_backup, username=user_server_backup, password=password_server_backup)

current_dt = datetime.date.today()
current_date = current_dt.strftime("%d-%m-%Y")
print(f"Current date - {current_date}")

name_of_file = "02_02_2024_full_b1_s1_v1.tib"
less_name = name_of_file[:-18]
arhiv_name = less_name.replace('_', "-")
print(f"Arhiv date - {arhiv_name}")

if arhiv_name == current_date:
    print("Arhiv is find")
else:
    print("arhive is not exists")

'''
копирование файла
'''
# ssh = client.open_sftp()
# local_file_path = "readme.txt"
# remove_file_path = "/tmp/readme.txt"

# commands = [
#     "cd ..; cd ..; pwd",
# ]
#
# for i in commands:
#     stdin, stdout, stderr = client.exec_command(i)
#     print(stdout.read().decode())

'''
выполнение команд на удалённом сервере
'''
# stdin, stdout, stderr = client.exec_command("cd ..; cd ..; cd /data2; pwd")
# path_to_directory = stdout
# print(stdout.read().decode())


'''
закрытие соединения после копирования
'''
# ssh.put(local_file_path, remove_file_path)
# ssh.close()

client.close()