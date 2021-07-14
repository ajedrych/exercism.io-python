def factors(value):
    divisors = []
    i = 2

    while value > 1:
        if value % i == 0:
            divisors.append(i)
            value = value / i
        else: i += 1
    return divisors
