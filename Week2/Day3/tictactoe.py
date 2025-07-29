# Tic Tac Toe

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# Step 2: Displaying the Game Board

def display_board()->str:
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

def player_input(player)->int:
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

    print(f"Your turn {player_number}")
    while True:

        try:
            position = int(input(f"Select your position (1 - 9)\n"))
            if position in range(1,10):
                row, column = position_map[position]
                if board[row][column] == ' ':
                    if player == 1:
                        board[row][column] = 'X'
                    else:
                        board[row][column] = 'O'
                else:
                    print('This position is already taken. Try again')

                break 
            
            
            else: 
                print('You must enter a number between 1 and 9.')

        except ValueError:
            print('You must enter a valid number.')

    display_board()


player_input(1)



