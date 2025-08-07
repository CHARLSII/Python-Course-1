guess_number = 7
chances = 0
limit = 3

while chances < limit:
    guess = input("Guess: ")
    
    if int(guess) == guess_number:
        print("You guessed the number!")
        break
    
    chances += 1
else:
    print("You failed")
    

     
    
    

