import random


choices = ['r', 'p', 's']

score_of_computer = 0
score_of_player = 0

while score_of_computer < 5 or score_of_player < 5:
    
    player_choice = str(input("Choose one of these r, p or s: ")).lower()
    if player_choice not in choices:
        print("Please, enter valid choice. s, p, r: ")
        continue
    
    random_choice = random.choice(choices)
    
    if score_of_player == random_choice:
        print("Draw")
        
    elif (player_choice == 'r' and random_choice == 's') or \
        (player_choice == 's' and random_choice == 'p') or \
            (player_choice == 'p' and random_choice == 'r'):
                score_of_player += 1
                print("You won this round.")
    else:
        score_of_computer += 1
        print("Computer won this round.")
    
    print(f"Computer {score_of_computer} : {score_of_player} You")
    
if score_of_player == 5:
    print("Congratulations, You won this game.")
else:
    print("Computer won this game. ")
    
    
        
        
        