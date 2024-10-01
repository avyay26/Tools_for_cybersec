import pwn
import math
import warnings

# Initialize the process for the executable
p = pwn.process('./ttt')

# Array of possible moves in Tic-Tac-Toe
argarr = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]

# Initial state of the board
gen = ['_','_','_','_','_','_','_','_','_']

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

def send_rec(a):
    """Send the move to the process and receive the board state."""
    warnings.filterwarnings('ignore')
    s = argarr[a]
    s = s.encode('utf-8')
    p.sendline(s)
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
                    gen[coun]= 'o'
                elif i == '\nx' or i == 'x':
                    gen[coun]= 'x'
                elif i == '\n_' or i == '_':
                    gen[coun]= '_'
                coun += 1
            else:
                break



def clear(gen):
  for i in range(9):
    gen[i] = '_'

def act():
        
        clear(gen)
                
        send_rec(0)
        print(gen)
        
        while True:
            m = best_move(gen)
            print(gen)
            print(m)
            send_rec(m)

act()

