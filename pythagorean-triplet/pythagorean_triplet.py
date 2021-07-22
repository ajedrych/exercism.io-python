def triplets_with_sum(number):
    import math

    result = []
    for b in range(1, number):
        for a in range(1, b):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0 and a + b + c == number:
                result.append([a, b, int(c)])

    return result
