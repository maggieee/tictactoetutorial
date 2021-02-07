# winning:

def win(current_game):

    # find out if there's a diagonal winner:
    if current_game[0][0] == current_game[1][1] == current_game[2][2] or current_game[0][2] == current_game[1][1] == current_game[2][0] and current_game[1][1] != '☐':
        print(f'{current_game[1][1]} is the winner!')
        return True

    # find out if there's a vertical winner:
    vertical_lst = []
    for row in current_game:
        vertical_lst.append(row[0])

    if vertical_lst[0] == vertical_lst[1] == vertical_lst[2] and vertical_lst[0] != '☐': #don't win if board in starting position
        print(f'{vertical_lst[0]} is the winner!')
        return True

    # find out if there's a horizontal winner:
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '☐': #don't win if board in starting position
            print(f'{row[0]} is the winner!')
            return True

    return False



def render_board(player="☐", row=0, column=0, just_display=False):
    try:
        if board[row][column] != '☐':
            print("Someone's already played here -- please pick another space.")
            return False

        print("    0    1    2")
        if not just_display:
            board[row][column] = player
        for count, row in enumerate(board):
            print(count, row)
    
    except IndexError as e:
        print("Error: Make sure you input row/column as 0 1 or 2 -->", e)
        # return False

    except Exception as e:
        print("Something went very wrong! -->", e)
        # return False

# render_board(just_display=True)

# render_board(player="X", row=2, column=2)

play = True
players = ["X", "O"]
while play:
    board = [['☐', '☐', '☐'],
            ['☐', '☐', '☐'],
            ['☐', '☐', '☐']]

    game_won = False
    render_board(just_display=True)
    current_player = players[0]
    while not game_won:
        print(f'Your turn, Player {current_player}')
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        render_board(current_player, row_choice, column_choice)
        if current_player == players[0]:
            current_player = players[1]
        elif current_player == players[1]:
            current_player = players[0]
        
        if win(board):
            game_won = True
            again = input("The game is over. Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeeeeeee")
                play = False
            else:
                print("Not a valid answer; playing again")
    