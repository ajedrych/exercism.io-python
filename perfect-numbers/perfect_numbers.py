def classify(number):

    if number <= 0:
        raise ValueError("Invalid input")

    sum = 0
    for a in range(1, number):
        if number % a == 0:
            sum += a

    if sum < number:
        return f"deficient"
        
    if sum > number:
        return f"abundant"

    if sum == number:
        return f"perfect"
