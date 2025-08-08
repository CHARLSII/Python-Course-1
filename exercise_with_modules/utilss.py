def find_max(list_numbers):
    max = list_numbers[0]
    
    for number in list_numbers:
        if number > max:
            max = number
            
    return max
            
