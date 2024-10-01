import pwn
import string
import itertools
import re #regex module
exec='./notwordle'
pattern=re.compile(r'(\d+)\s*/\s*30')

ori=''
pasle=30
charset=string.ascii_letters+string.digits+'_'
#def list(ori,pasle):
for x in itertools.product(charset,repeat=pasle):
        x=''.join(x)
        password=ori+x
        p=pwn.process([exec])
        p.sendline(password)
        print(f"Trying password {password}")
        output=p.recvall().decode().strip()
        if output != "Enter your password (30 characters long, all characters are alphanumeric or '_') : 0 / 30 characters match":
             break
        match=pattern.search(output)
        #print(f"The match)
        print(f"output is {output}")
        if match:

            num=int(match.group(1))
            print(f"the match is {num}")
            if num==30:
                print(f"Password found and is {password}")
                break
            else:
                 pasle=30-num
                 ori=password[0:num-1]
        p.close()
