from pwn import *
 #import numpy as np
import warnings
warnings.filterwarnings('ignore')
c=0
d=0
p=process('./ttt')

string_data = f"{c},{d}"
bytes_data=string_data.encode('utf-8')#default utf-8
out=p.recv()
print(out.decode('utf-8'))

p.sendline(string_data)
output=p.recv()

oi=output.decode()
print(oi)
oi=oi.strip().split(' ')
print(oi)
#minimax algo





#print(p.recvall().decode('utf-8'))
#for i in range(2):
 #ar=b'f"{c},{d}"'
 #p=process('./ttt') #processstarted
 #p.sendline(ar)
 #output=p.recvall()
 #out=output.decode('utf-8')
 #print(out)
 #c+=1
 #d+=1
#p.close()
