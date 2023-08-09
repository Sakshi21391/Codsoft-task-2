import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth
    if check_winner(board, 'O'):
        return 10 - depth
    if check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score

def get_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while not check_winner(board, 'X') and not check_winner(board, 'O') and not check_draw(board):
        row, col = get_best_move(board)
        board[row][col] = 'O'
        print("\nAI's move:")
        print_board(board)
        
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        
        if check_draw(board):
            print("It's a draw!")
            break
        
        player_row = int(input("Enter row (0-2) for your move: "))
        player_col = int(input("Enter column (0-2) for your move: "))
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
            print_board(board)
            
            if check_winner(board, 'X'):
                print("You win!")
                break
        else:
            print("Cell already taken. Try again.")
    
    print("Game over!")

if __name__ == "__main__":
    main()
