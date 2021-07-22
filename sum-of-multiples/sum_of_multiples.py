def sum_of_multiples(limit, multiples):
    
    numbers = []
    for i in range(1, limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                numbers.append(i)

    numbers = set(numbers)
    counter = 0
    for i in numbers:
        counter += i


    return counter
