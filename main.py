import paramiko
from passwd import access_server_arhivs
import datetime


hostname_server_backup = access_server_arhivs['hostname']
user_server_backup = access_server_arhivs['user']
password_server_backup = access_server_arhivs['password']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname_server_backup, username=user_server_backup, password=password_server_backup)



'''
выполнение команд на удалённом сервере
'''
not_exists_msg = "arhiv is not exists ... :-("
current_dt = datetime.date.today()
current_date = current_dt.strftime("%d-%m-%Y")
print(f"Current date - {current_date}")

stdin, stdout, stderr = client.exec_command("cd ..; cd ..; cd /data2;")
tmp_files = stdout.read().decode()
list_files = []
list_files = tmp_files.split()
# print(list_files)

for name_of_file in list_files:
    # print(name_of_file)
    short_name = name_of_file[:10]
    arhiv_name = short_name.replace('_', "-")

    if arhiv_name == current_date:
        ssh = client.open_sftp()
        local_file_path = short_name
        remove_file_path = f"/backups/{short_name}.tib"

        ssh.put(local_file_path, remove_file_path)

        print(f"Yes - {arhiv_name}")
        not_exists_msg = ""


if not_exists_msg != "":
    print(not_exists_msg)


'''
закрытие соединения после копирования
'''
# ssh.put(local_file_path, remove_file_path)
ssh.close()
client.close()