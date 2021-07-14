def steps(number):
    if number <= 0:
        raise ValueError("Invalid input")
    
    counter = 0
    while number > 1:
        if number % 2 != 0:
            number = number * 3 + 1
            counter += 1
        else:
            number =  number / 2
            counter += 1
    
    return counter