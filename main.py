#!/usr/bin/python

import datetime
import os.path
import paramiko
from passwd import access_server_arhivs


hostname_server_backup = access_server_arhivs['hostname']
user_server_backup = access_server_arhivs['user']
password_server_backup = access_server_arhivs['password']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname_server_backup, username=user_server_backup, password=password_server_backup)


'''
Определение текущей даты
'''
not_copied_msg = "file not copied ... :-("
current_dt = datetime.date.today()
current_date = current_dt.strftime("%d-%m-%Y")


'''
выполнение команд на удалённом сервере
'''
stdin, stdout, stderr = client.exec_command("cd ..; cd ..; cd /data2; ls")
tmp_files = stdout.read().decode()
list_files = []
list_files = tmp_files.split()

for name_of_file in list_files:
    short_name = name_of_file[:10]
    arhiv_name = short_name.replace('_', "-")

    if arhiv_name == current_date:
        ssh = client.open_sftp()
        remove_file_path = f"/data2/{arhiv_name}" + "_full_b1_s1_v1.txt"
        remove_file_path = remove_file_path.replace("-", "_")
        local_file_path = f"/backups/{arhiv_name}" + ".txt"
        folder_name = "backups"

        try:
            if os.path.exists(folder_name) != True:
                os.mkdir("/backups")
                print(f"Folder \"{folder_name}\" is created!")
        except BaseException:
            print("Folder is exists")


        try:
            ssh.get(remove_file_path, local_file_path)
            print("File is copied")
        except BaseException:
            print("Что то пошло не так...")
        finally:
            ssh.close()

        not_copied_msg = ""


if not_copied_msg != "":
    print(not_copied_msg)


'''
закрытие соединения после копирования
'''
client.close()
