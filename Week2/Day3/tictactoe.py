# Tic Tac Toe

# Step 1: Initializing Board 

def initialize_board():
    board = [([' ']*3) for num in range(3)]
    return board 

# Step 2: Displaying the Game Board

def display_board(board)->str:
    '''
    prints a 3x3 tic tac toe board 
    '''
    print(f"\n     |     |     ")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print(f"     |     |     ")
    print(f"-----|-----|-----")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")
    print(f"     |     |     \n")


# Step 3: Getting Player Input

def player_input(board, player)->int:
    '''
    Ask current player for their move 
    returns position 1-9 depending on empty tiles available on board 
    '''
    player_number = player

    position_map = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2)
    }

    print(f"Your turn player {player_number}")
    while True:

        try:
            position = int(input(f"Select your position (1 - 9)\n"))
            if position in range(1,10):
                row, column = position_map[position]
                if board[row][column] == ' ':
                    if player == 1:
                        board[row][column] = 'X'
                        break 
                    else:
                        board[row][column] = 'O'
                        break 
                else:
                    print('This position is already taken. Try again') 
            
            
            else: 
                print('You must enter a number between 1 and 9.')

        except ValueError:
            print('You must enter a valid number.')


# Step 4: Checking for a Winner

def check_win(board, player)->bool:
    '''
    Checks if the player won tic tac toe game
    based on board state and current player
    '''
    # Check Player Mark
    player_mark = ''
    if player == 1:
        player_mark = 'X'
    else:
        player_mark = 'O'

    # Check Horizontal Win
    for row in range(len(board)):
        if board[row][0] == player_mark and \
           board[row][1] == player_mark and \
           board[row][2] == player_mark:
            return True
    
    # Check Vertical Win
    for col in range(len(board[0])):
        if board[0][col] == player_mark and \
        board[1][col] == player_mark and \
        board[2][col] == player_mark:
            return True

    # Check Diagonal Win
    if  board[0][0] == player_mark and \
        board[1][1] == player_mark and \
        board[2][2] == player_mark:
         return True
    elif board[0][2] == player_mark and \
         board[1][1] == player_mark and \
         board[2][0] == player_mark:
         return True
    
    # No win
    return False 

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
            
    return True
            

# Step 6: The Main Game Loop

def play():
    '''
    Initializes a game of tic tac toe 
    '''
    board = initialize_board()
    player_number = 1
    print('Welcome to TIC TAC TOE! ❌⭕❌')
    display_board(board)

    while True: 
        player_input(board,player_number)
        display_board(board)
        if (check_win(board,player_number) == True):
            display_board(board)
            print(f'PLAYER {player_number} WON!\n')
            break 
        elif (check_tie(board) == True):
            display_board(board)
            print(f'IT\'S A TIE!')
            break
        else:
            if player_number == 1:
                player_number = 2
            else:
                player_number = 1


# Gameplay Tic Tac Toe    
play()