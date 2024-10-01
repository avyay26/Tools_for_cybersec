from pwn import *
import warnings

p=process('./ttt')
gen = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
argarr = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]
def send_rec(a):
     
     warnings.filterwarnings('ignore')
     s=argarr[a]
     h=s.encode('utf-8')
     p.sendline(h)
     out=p.recv().decode('utf-8')
     print(out)
     out=out.split(' ')
     print(out)
     coun=0
     #update gen coun
     if out[0]=='Game' :
         fl=True


     if out[0]!='Game' :
      for i in out:
        if coun<9:
          if i=='\no' or i=='o':
                #oy[coun]=1
                gen[coun]='o'
          elif i=='\nx' or i=='x':
                #oy[coun]=0
                #xy[coun]=1
                gen[coun]='x'
          elif i=='\n_' or i=='_':
                #oy[coun]=0
                #xy[coun]=0
                gen[coun]='_'
          coun+=1
        else:
            break

def act():

    out=p.recv().decode('utf-8')
    print(out)
    send_rec(1)
    send_rec(0)
    send_rec(2)
    
act()




