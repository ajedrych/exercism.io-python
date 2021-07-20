def primes(limit):
    numbers = []
    final = []
    for i in range(2, limit + 1):
        if i not in numbers:
            final.append(i)
            for j in range (i*i, limit + 1, i):
                numbers.append(j)
    
    return final