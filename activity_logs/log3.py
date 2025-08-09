import random

#while loops
""""
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
"""
#for loops
"""""
for x in range(5):
    for y in range(5):
        print(f"{x}, {y}")
"""
""""
numbers = [5,2,5,2,2]

for x in numbers:
    output = ""
    for y in range(x):
        output += "x"
    print(output)
"""

#list
#write a program to find the largest number in a list

numbers = [0] * 10

for x in range(10):
    numbers[x] = random.randrange(0,20)
print(numbers)

largest = numbers[0]

for y in range(len(numbers)):
    if largest < numbers[y]:
        largest = numbers[y]
print(f"Largest number is: {largest}")
    


    
    
     
    
    

