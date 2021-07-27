def commands(number):
    number = bin(number)
    number = number.replace("b", "0")
    
    result = []
    if number[-1] == "1":
        result.append("wink")
    if number[-2] == "1":
        result.append("double blink")
    if len(number) > 3 and number[-3] == "1":
        result.append("close your eyes")
    if len(number) > 4 and number[-4] == "1":
        result.append("jump")
    if len(number) > 5 and number[-5] == "1":
        result.reverse()
    return result

