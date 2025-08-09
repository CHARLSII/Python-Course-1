weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
lbs_kg = 0.45
kg_lbs = 2.2

if unit.upper() == 'L':
    print(f"Your weight in kilogram is {str(int(weight) * lbs_kg)}kg")
elif unit.upper() == 'K':
    print(f"Your weight in pounds is {str(int(weight) * kg_lbs)}lbs")
else:
    print("Please type correct unit")