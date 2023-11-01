from logic import check_winner

def get_empty_board():
    return[
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

def print_board(board):
    for row in board:
        print(row)

def get_player_input(current_player):
    """#equal to #(用于很多行的解释)
    input:
        row,col
    return:
        row:int-> the index of row
        col:int-> the index of column
    """
    prompt=f"player {current_player},please input your move, e.g. row,col\n"
    player_input=input(prompt)#this is a atr->"1,1"

    row_col_list=player_input.split(',')#["1","1"]
    #"1,1".split(',')->["1","1"]
    row_col_list=player_input.split(',')
    row,col=[int(x) for x in row_col_list]

    #[1,1]
    return row,col

def switch_player(current_player):
    if current_player=='X':
        return'O'
    return'X'

if __name__=='__main__':
    current_player='X'
    # get an empty board
    board = get_empty_board()
    #print the board
    winner=None
    #ask user input

    while winner is None:
        print_board(board)
        try:
            row,col=get_player_input(current_player)
        except ValueError:
            print("Invalid input,try again\n")
            continue

        row,col=get_player_input(current_player)
        if row is None:
            print("Invalid input,try again")
        

        board[row][col]=current_player
        winner = check_winner(board)#"O","X"->break out of the loop
        current_player=switch_player(current_player)
        #current_player="X"if current_player=="O"else"O"
    print_board(board)
    print(f"Winner is {current_player}!")

    
    #check for winner
    #check if game is draw
    #print the winner