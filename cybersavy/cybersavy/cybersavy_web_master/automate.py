import paramiko
host = "192.168.1.101"
port = 22
username = "root"
password = "userone"

command = "getent passwd"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

for i in lines:
    if "home" in i:
        print(i.split(":"))