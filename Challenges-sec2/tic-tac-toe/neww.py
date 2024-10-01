from pwn import *
import warnings 



p=process('./ttt')
argarr=["0,0","0,1","0,2","1,0","1,1","1,2","2,0","2,1","2,2"]
#oy=[0,0,0,0,0,0,0,0,0]
#xy=[0,0,0,0,0,0,0,0,0]
gen=['_','_','_','_','_','_','_','_','_']
check=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def moves(gen):
    
    return '_' in gen    
    
def che(gen):
    for i in check:
        #for j in i:
       #gen[i[0]]==gen[i[1]]==gen[i[2]]=='o':
        if gen[i[0]]==gen[i[1]]==gen[i[2]]=='o':
            return 10
        elif gen[i[0]]==gen[i[1]]==gen[i[2]]=='x':
            return -10
    return 0    
  
def minimax(gen,depth,is_max):
    score=che(gen)
    
    
    if score==10:
        return score - depth
    elif score==-10:
        return score + depth    
    if moves(gen)==False:
        return 0
    if is_max==True:
      best=-100000000000
      for i in range(9):
          if gen[i]=='_':
              gen[i]='o'
              best=max(best,minimax(gen,depth+1,not is_max))
              gen[i]='_'
      return best
    elif is_max==False:
        best=100000000 
        for i in range(9):
          if gen[i]=='_':
              gen[i]='x'
              best=min(best,minimax(gen,depth+1,not is_max))
              gen[i]='_'
        return best
def best_move(gen):
    be=-10000000
    mov=-1
    for i in range(9):
        if gen[i] == '_':
           gen[i] = 'o'
           curr_val = minimax(gen,0,False)
           gen[i] = '_'
           if curr_val>be:
               be=curr_val
               mov=i
    return mov
    
       
    

       



fl=True

def send_rec(a):
      warnings.filterwarnings('ignore')
      s=argarr[a]
      h=s.encode('utf-8')
      p.sendline(h)
      out=p.recvuntil(b'0,2\n').decode()
      print(out)
      out=out.split(' ')
      #print(p.recv().decode())
      #print(out)
      coun=0
     #update gen coun
     #if out[0]=='Game' :
         #fl=True
         
      if out[0]=='Game':
          fl=False
          clear(gen) 
          return
      elif out[0]=='o':
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
      elif out[0] !='Game' and out[0] !='o':
         print(p.recv().decode())

def clear(gen):
    for i in range(9):
        gen[i]='_'
def act():
    out=p.recv().decode()
    print(out)
   #for i in range(250):
    #gen=['_','_','_','_','_','_','_','_','_']
    
    send_rec(0)
   
    
    m=best_move(gen)
    print(m)
      
    send_rec(m)
    print(gen)
  
ou=p.recv().decode()
print(ou)
for k in range(251):
  print(k)
  #print(ou)
  fl=True
  send_rec(0)
  while fl==True:
      
      m=best_move(gen)
      send_rec(m)
             
     
#gen=['o','_','_','_','_','_','_','x','_'] 
#print(best_move(gen))
   #send_rec(0)
void cellVoltageLoop (unsigned long timeBuffer)
{
  	byte  error = 0;
    error |= LTC2949_ADxx(
		/*byte md = MD_NORMAL     : */MD_FAST,
		/*byte ch = CELL_CH_ALL   : */CELL_CH_ALL,
		/*byte dcp = DCP_DISABLED : */DCP_DISABLED,
		/*uint8_t pollTimeout = 0 : */LTCDEF_POLL_EOC ? LTC2949_68XX_GETADCVTIMEOUT16US(LTC2949_68XX_T6C_27KHZ	);
     #print(best_move(gen))
 #   print(m)
  #send_rec(m)
  #print(gen)
 #m=best_move(gen)
  #print(m)
 #send_rec(m)
 #print(gen)
#print(best_move(gen))
            

