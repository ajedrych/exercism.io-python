def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Invalid input")

    numbers = []
    for i in range(len(series) - length + 1):
        if i < i + length:
            numbers.append(series[i:i+length])
    return numbers