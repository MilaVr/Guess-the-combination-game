import random
from copy import deepcopy

# Creating an empty board
guess = ["____"]*10
score = ["____"]*10

def board(guess, score):
    print(guess[0], "   ", score[0])
    print(guess[1], "   ", score[1])
    print(guess[2], "   ", score[2])
    print(guess[3], "   ", score[3])
    print(guess[4], "   ", score[4])
    print(guess[5], "   ", score[5])
    print(guess[6], "   ", score[6])
    print(guess[7], "   ", score[7])
    print(guess[8], "   ", score[8])
    print(guess[9], "   ", score[9])

def check_entry(player_entry):
    for char in player_entry:
        if char.isdigit() and (0 < int(char) <= 6):
            continue
        else:
            return False
    return True

# Generating random four-digit combination, digits (1-5)
combination = []
for x in range(4):
    combination.append(str(random.randint(1,6)))

# Scoring – character in place is marked X
#         – character in wrong place is marked O 

k=0
while k < 10:
    combo = deepcopy(combination)    
    while True:
        player_combination = input("Your combination: ")

        if len(player_combination) != 4:
            print("Invalid entry, combination must include four digits (1-5)!")
        elif not check_entry(player_combination):
            print("Invalid entry, combination must include only digits (1-5)!")
        else:
            break   
    print()

    player_combo = [x for x in player_combination]
    combo_marked = list(enumerate(combo))
    player_combo_marked = list(enumerate(player_combo))

# Marking the players combination to the board
    guess[k] = player_combination
  
    X = 0
    O = 0

# Checking for the characters in place (X)
    for x in player_combo_marked:
        if x in combo_marked:
            X += 1
            combo_marked.remove(x)
            combo.remove(x[1])
            player_combo.remove(x[1])

# Checking for the characters off place (O)
    for x in player_combo:
        if x in combo:
            O += 1
            combo.remove(x)

# Marking the score to the board
    score[k] = X*"X" + O*"O"

# Checking for win 
    if score[k] == "XXXX":
        print(f"Congratulations, You Win! {player_combination} is the correct combination")
        break
    else:
        board(guess,score)
        print()
    
    k+=1
            
        

