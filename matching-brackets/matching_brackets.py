def is_paired(input_string):
    brackets = {"(": ")", "{": "}", "[": "]"}
    check = []
    input_string = list(input_string)
    
    for i in input_string:
        if i not in ("(", ")", "{", "}", "[", "]"):
            input_string.remove(i)

    if len(input_string) % 2 != 0:
        return False

    for i in input_string:
        if i in brackets:
            check.append(brackets[i])
        elif i in brackets.values():
            if check and check[-1] == i:
                check.pop()
            else:    
                return False
    return len(check) == 0