from pwn import *
import itertools
password_length = 30
correct_matches = 30  # Adjust this based on your program's output

charset=string.ascii_letters+string.digits+'_'
for password in itertools.product(charset,repeat=password_length):
    password = ''.join(password)
    p = process(['./notwordle'])
    p.sendline(password)
    output = p.recvall().decode().strip()
    if output == "Enter your password (30 characters long, all characters are alphanumeric or '_') : 29 / 30 characters match":
        print(f"Found password: {password}")
        break
    p.close()

