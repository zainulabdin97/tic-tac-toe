player_1 = ""
player_2 = ""
all_rows = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def game_start():
    global player_1, player_2

    print('Tic Tak toe game')

    player_1 = input("Which symbol do you want to play with X or O: ").upper()

    # if invalid character
    while player_1 != "X" and player_1 != "O":
        player_1 = input("Not a valid character. Enter a valid character: ").upper()

    # assigning character to players
    if player_1 == "X":
        player_2 = "O"

    else:
        player_1 = "O"
        player_2 = "X"

    print(f"player 1 = {player_1}")
    print(f"player 2 = {player_2}\n\n")


def displaying_ui():
    
    global all_rows

    for i in range(len(all_rows)):

        for j in all_rows[i]:
            print(j + "     ", end=" ")
        print("\n")


def print_row_after_char(player, grid_number):
    global all_rows
    for i in range(len(all_rows)):
        all_rows[i] = [i.replace(grid_number, player) for i in all_rows[i]]

        print(f"{"     ".join(all_rows[i])}\n")


def win_logic(player_char):

    global all_rows
    # if characters match vertically
    for i in range(3):
        if all_rows[0][i] == player_char and all_rows[1][i] == player_char and all_rows[2][i] == player_char:
            return True

    # if characters match horizontally
    if all([j == player_char for j in all_rows[0]]) or all([j == player_char for j in all_rows[1]]) or all(
            [j == player_char for j in all_rows[2]]):
        return True

    # if characters match diagonally
    if all_rows[0][0] == player_char and all_rows[1][1] == player_char and all_rows[2][2] == player_char or all_rows[0][
        2] == player_char and \
            all_rows[1][1] == player_char and all_rows[2][0] == player_char:
        return True


def input_validation(player_num, player):
    grid_num_player = input(f"In which number do you wish to put your character player {player_num} ?: ")

    # checking if the user enters a position that is already filled by a character
    while grid_num_player not in all_rows[0] and grid_num_player not in all_rows[1] and grid_num_player not in all_rows[
        2]:
        grid_num_player = input("Not a valid position enter a valid position: ")

    print_row_after_char(player, grid_num_player)


# checking if the game is drawn
def game_drawn(i):
    if i == 9:
        print("Game draw")
        return True


game_start()

displaying_ui()




# displaying the chars on the grid
i = 0
while i < 9:

    input_validation(player_num=1, player=player_1)

    if win_logic(player_1):
        print("Player 1 win!")
        break

    i += 1

    # when game is drawed

    if game_drawn(i):
        break

    input_validation(player_num=2, player=player_2)

    if win_logic(player_2):
        print("Player 2 win!")
        break
    i += 1

    if game_drawn(i):
        break

# displaying_ui()
