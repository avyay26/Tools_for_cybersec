import pwn
import math
import warnings
import time

# Initialize the process for the executable
def start_process():
    try:
        return pwn.process('./ttt')
    except Exception as e:
        print(f"Error starting process: {e}")
        return None

argarr = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]

gen = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
check = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def moves(gen):
    return '_' in gen

def che(gen):
    for i in check:
        if gen[i[0]] == gen[i[1]] == gen[i[2]] == 'o':
            return 10
        elif gen[i[0]] == gen[i[1]] == gen[i[2]] == 'x':
            return -10
    return 0

def minimax(gen, depth, is_max):
    score = che(gen)
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    if not moves(gen):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(9):
            if gen[i] == '_':
                gen[i] = 'o'
                best = max(best, minimax(gen, depth + 1, not is_max))
                gen[i] = '_'
        return best
    else:
        best = math.inf
        for i in range(9):
            if gen[i] == '_':
                gen[i] = 'x'
                best = min(best, minimax(gen, depth + 1, not is_max))
                gen[i] = '_'
        return best

def best_move(gen):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if gen[i] == '_':
            gen[i] = 'o'
            curr_val = minimax(gen, 0, False)
            gen[i] = '_'
            if curr_val > best_val:
                best_val = curr_val
                move = i
    return move

def send_rec(a, p):
    warnings.filterwarnings('ignore')
    try:
        s = argarr[a]
        s = s.encode('utf-8')
        p.sendline(s)
        time.sleep(1)  # Wait for the process to respond
        out = p.recv().decode()
        print(out)
        out = out.strip().split(' ')
        coun = 0
        fl = False
        
        if out[0] == 'Game':
            fl = True
        else:
            for i in out:
                if coun < 9:
                    if i == '\no' or i == 'o':
                        gen[coun] = 'o'
                    elif i == '\nx' or i == 'x':
                        gen[coun] = 'x'
                    elif i == '\n_' or i == '_':
                        gen[coun] = '_'
                    coun += 1
                else:
                    break
    except Exception as e:
        print(f"Error in send_rec: {e}")

def act():
    for _ in range(250):
        global gen
        gen = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        
        p = start_process()
        if not p:
            print("Process failed to start.")
            return
        
        send_rec(0, p)
        fl = False
        while not fl:
            m = best_move(gen)
            send_rec(m, p)

if __name__ == "__main__":
    act()

