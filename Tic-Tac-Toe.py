import random 

# Dictionary for storing the current state of each square ('X', 'O', or # for unmarked) and a list of currently marked squares
spaces_dict = { 1: str(1), 2: str(2), 3: str(3), 4: str(4), 5: str(5), 6: str(6), 7: str(7), 8: str(8), 9: str(9)}
marked_spaces = []

# This fuction setups the tic-tac-toe board that is presented at the beginning of the game. 
def tic_tac_toe():
    print("    |    |   ")
    print("  1 |  2 |  3")
    print("    |    |   ")
    print("--------------")
    print("    |    |   ")
    print("  4 |  5 |  6")
    print("    |    |   ")
    print("--------------")
    print("    |    |   ")
    print("  7 |  8 |  9")
    print("    |    |   ")

# This function sets all the boxes to the keys representing the current state of the board.
def move():
    print("    |    |   ")
    print("  " + spaces_dict[1] + " |  " + spaces_dict[2] + " |  " + spaces_dict[3])
    print("    |    |   ")
    print("--------------")
    print("    |    |   ")
    print("  " + spaces_dict[4] + " |  " + spaces_dict[5] + " |  " + spaces_dict[6])
    print("    |    |   ")
    print("--------------")
    print("    |    |   ")
    print("  " + spaces_dict[7] + " |  " + spaces_dict[8] + " |  " + spaces_dict[9])
    print("    |    |   ")

# This function gives the computer a 50/50 chance of moving to a randomly selcted box on the board that isn't already selected by the player.
def computer_move():
    print("Now it's the computer's turn.")
    random_num = random.randint(1,10)    
    if random_num <= 5:
         unused_spaces = [x for x in spaces_dict.keys() if x not in marked_spaces]
         choosen_unused_space = unused_spaces[random.randint(0,len(unused_spaces)-1)]
         spaces_dict[choosen_unused_space] = "X"
         marked_spaces.append(choosen_unused_space)
    else:
         print("Computer missed question, now your turn.")
    move()

# This function checks all the combinations for the computer or player to win the game. 
def win(player_symbol):

    return (spaces_dict[1] is player_symbol and spaces_dict[2] is player_symbol and spaces_dict[3] is player_symbol) or \
    (spaces_dict[4] is player_symbol and spaces_dict[5] is player_symbol and spaces_dict[6] is player_symbol) or \
    (spaces_dict[7] is player_symbol and spaces_dict[8] is player_symbol and spaces_dict[9] is player_symbol) or \
    (spaces_dict[1] is player_symbol and spaces_dict[4] is player_symbol and spaces_dict[7] is player_symbol) or \
    (spaces_dict[2] is player_symbol and spaces_dict[5] is player_symbol and spaces_dict[8] is player_symbol) or \
    (spaces_dict[3] is player_symbol and spaces_dict[6] is player_symbol and spaces_dict[9] is player_symbol) or \
    (spaces_dict[1] is player_symbol and spaces_dict[5] is player_symbol and spaces_dict[9] is player_symbol) or \
    (spaces_dict[3] is player_symbol and spaces_dict[5] is player_symbol and spaces_dict[7] is player_symbol)

# This function checks the possibility for a tie where no one has gotten 3 symbols in a row. 
def tie():
    unused_spaces = [x for x in spaces_dict.keys() if x not in marked_spaces]
    if len(unused_spaces) == 0:
        print("You have drawn with the computer")
        return True 
    else:
         return False 
    

# This function creates the addition equation given to the player to answer based on the box he or she has selected and makes the move if the player answers correctly. 
def addition_equ(numb):
    random_num = random.randint(0,10)
    print(str(random_num) + "+" + str(random_num)) 
    ans_1 = random_num + random_num
    ans_2 = int(input("What is the answer?"))
    if ans_2 == ans_1:
        print("You are correct!")
        spaces_dict[numb] = "O"
        marked_spaces.append(numb)
    else:
        print("You are wrong.")
    computer_move()
        

number_list = [x for x in range(1,10)]


# The code displayed below first introduces the game. Then, it asks the player to choose a box which then leads to an equation to pop up. 
# The equation then needs to be answered. Once answered either right or wrong, it is the computer's turn which moves randomly and doesn't always answer correctly. 
# This continues until the while statement is false. This means that someone has won or the game is a tie. 
print("Welcome to tic-tac-toe Land!")
tic_tac_toe()
print("")
while not win('X') and not win('O') and not tie():
    while True:
        value = int(input("Pick a square between 1 and 9."))
        if value not in number_list:
                print("You put a invalid value.")
        else:
            break
    addition_equ(value)

if win("X"):
     print("Computer won! :(")
elif win("O"):
     print("Player won! Yay! :)")


