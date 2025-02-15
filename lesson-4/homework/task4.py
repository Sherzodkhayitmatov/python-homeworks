import random

while True:
    num = random.randint(1,100)
    print("I have chosen the number. Try to find the number!")
    number_of_guesses = 0
    
    
    while number_of_guesses < 10:
        guessed_num = int(input("Guess the number: "))
        
        if num == guessed_num:
            print("Well done, you found it.")
            break
        
        
        elif num < guessed_num:
            print("It is too high.")                      
        
        elif num > guessed_num:
            print("It is too low.") 
            
        number_of_guesses += 1
        
        if number_of_guesses == 10:
            again = input("You lost, Want to play again? ").strip().lower()
            if again not in ['y', 'yes', 'ok']:
                break
