# $ -- Queen
# 0 -- path

import sys
def canPlace(board,n,current_col,current_row):
    for j in range(0,current_col): # block right , left
        if board[current_row][j] == '$':
            return False
    
    diagonal_i  = current_row
    diagonal_j  = current_col 
    
    while True: # block diagonal down
        if diagonal_i >= n or diagonal_j < 0:
            break
        if board[diagonal_i][diagonal_j] == '$':
            return False
        diagonal_i +=1
        diagonal_j -=1
    
    diagonal_i  = current_row - 1
    diagonal_j  = current_col - 1
    
    while True: # block diagonal up
        if diagonal_i < 0 or diagonal_j < 0:
            break
        if board[diagonal_i][diagonal_j] == '$':
            return False
        diagonal_i -=1
        diagonal_j -=1
    return True

def nQueen(board,n,current_col):
    placed=[-1 for i in range(n)]
    while n != current_col:
        flag = 0 
        for i in range(placed[current_col]+1,n):
            if canPlace(board,n,current_col,i):
                flag = 1
                placed[current_col] = i
                board[i][current_col] = '$'
                break
       
        if flag == 0:  # backtrack
            placed[current_col] = -1
            current_col -= 1
            if current_col<0:
                return False
            board[placed[current_col]][current_col] = '0'
        else:
            current_col +=1
    
    return True
    


def display(board,n):
    for i in range(0,n):
        for j in range(0,n):
            print(board[i][j],end="    ")
        print()

if __name__ == "__main__":
    n = int(input('N : '))
    board = [['0' for i in range(n)] for j in range(n)]
    if nQueen(board,n,0):
        display(board,n)
    else:
        print('Not Possible') 