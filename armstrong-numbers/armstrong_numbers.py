def is_armstrong_number(number):

    #convert int to list
    number_converted = list(map(int, str(number)))
    sum = 0

    for x in number_converted:
        sum += x**len(number_converted)
    
    if sum == number:
        return True
    else: return False