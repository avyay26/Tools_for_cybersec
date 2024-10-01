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

# Array of possible moves in Tic-Tac-Toe
argarr = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]

# Winning combinations
check = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def moves(gen):
    """Check if there are moves left."""
    return '_' in gen

def che(gen):
    """Evaluate the board state and return the score."""
    for i in check:
        if gen[i[0]] == gen[i[1]] == gen[i[2]] == 'o':
            return 10
        elif gen[i[0]] == gen[i[1]] == gen[i[2]] == 'x':
            return -10
    return 0

def minimax(gen, depth, is_max):
    """Minimax algorithm to find the optimal move."""
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
    """Find the best move for the 'o' player."""
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
fl=False

global gen 
def send_rec(a, p):
    """Send the move to the process and receive the board state."""
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
        
        
        if out[0] == 'Game':
            fl = True
        else :
            for i in out:
                if coun < 9:
                    if i == 'o' or i == '\no':
                        gen[coun] = 'o'
                    elif i == 'x' or i == '\nx':
                        gen[coun] = 'x'
                    elif i == '_' or i == '\n_':
                        gen[coun] = '_'
                    coun += 1
                else:
                    break
    except Exception as e:
        print(f"Error in send_rec: {e}")

def act():
        """Main function to play the game multiple times."""
    #for _ in range(250):
        global gen
        gen=['_','_','_','_','_','_','_','_','_']
        
        p = start_process()
        if not p:
            print("Process failed to start.")
            return
        
        send_rec(0, p)  # Initial move by 'o'
        
        while not fl:
            m = best_move(gen)
            print(gen)
            print(m)
            send_rec(m, p)

if __name__ == "__main__":
    act()
