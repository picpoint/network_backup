import paramiko
import datetime
from passwd import access_server_arhivs


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

stdin, stdout, stderr = client.exec_command("cd ..; cd ..; cd /data2; ls")
tmp_files = stdout.read().decode()
list_files = []
list_files = tmp_files.split()

for name_of_file in list_files:
    short_name = name_of_file[:10]
    arhiv_name = short_name.replace('_', "-")

    if arhiv_name == current_date:
        ssh = client.open_sftp()
        remove_file_path = f"/data2/{arhiv_name}" + "_full_b1_s1_v1.tib"
        remove_file_path = remove_file_path.replace("-", "_")
        print(remove_file_path)

        local_file_path = f"{arhiv_name}" + ".tib"
        ssh.get(remove_file_path, local_file_path)

        print(f"Yes - {arhiv_name}")
        not_exists_msg = ""


if not_exists_msg != "":
    print(not_exists_msg)


'''
закрытие соединения после копирования
'''
ssh.close()
client.close()