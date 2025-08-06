

#name = input("Your name: ")
#color = input("Your favorite color: ")

#print(name, "likes", color)

#birth_year = input("Birth year: ")
#age = 2025 - int(birth_year)

#print (age, "years old")

#weight = input("Weight(lbs): ")
#print('Your weight in kg is', str(int(weight) * 0.45) + "kg")

#sentence = "This is a sentence"

#print(sentence[-1])
#print(sentence[0:4])

#last_name = "Marfil"
#first_name = "Charls"
#sentence = f"{first_name} {last_name} is studying python"

#print(sentence)

#print(sentence.replace("python", "java"))

# operators 
# add(+), sub(-), multiply(*), divide(/), remainder(%), exponent(**)

#print(math.factorial(4))
#print(math.gcd(346, 471))
#print(math.cbrt(45))

#is_good = False
#is_bad = False

#if is_good:
#    print("It's a good day")
#    print("Enjoy your day!")
#elif is_bad:
#    print("It's a bad day")
#    print("Cheer up!")
#else:
#    print("It's a lovely day!")

#house_price = 1000000
#is_good_credit = False
#down_payment = 0

#if is_good_credit:
#    down_payment = house_price * 0.1
#else:
#    down_payment = house_price * 0.2
    
#print(f"Your down payment is Php{int(down_payment)}")

name = input("Type your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks good!")
    