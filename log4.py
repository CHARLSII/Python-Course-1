# write a program to remove the duplicates in a list

"""
numbers = [1,5,7,5,1,9,3]
numbers_2 = []

print(numbers)

for x in numbers:
    if x not in numbers_2:
        numbers_2.append(x)
        
print(numbers_2)
"""

# tuple ()

""""
numbers = (1, 2, 3) # tuples can't be modified

print(numbers.count(1))
print(numbers.index(1))

"""

# unpacking

"""
numbers = (1, 2, 3)
x, y ,z = numbers

print(x, y, z)
"""

#dictionaries

""""
profile = {
    "name": "Charls Darren",
    "age" : 21,
    "birthday" : "April 1, 2004"
}
print(profile["name"])
print(profile.get("name"))

profile["sex"] = "Male"

print(profile["sex"])
"""

# create a program that will turn the phone numbers into its english equivalent
# my attempt
"""
phone_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

input_number = list(input("Phone: "))

output = ""
for x in input_number:
    output += phone_number[str(x)] + " "

print(output)

"""

# with the help of tutorial
""""
phone_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

input_number = input("Phone: ")

output = ""
for x in input_number:
    output += phone_number.get(x, "unrecognize") + " "

print(output)
"""
