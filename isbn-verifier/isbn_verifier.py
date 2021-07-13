def is_valid(isbn):
    isbn = isbn.replace("-", "").upper()

    if len(isbn) != 10:
        return False
    
    if isbn[-1] == 'X':
        last = 10
    elif isbn[-1].isdigit():
        last = isbn[-1]
    else: return False

    for i in isbn[0:8]:
        if not i.isdigit():
            return False

    isbn_sum = int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + int(last)
    
    if (isbn_sum) % 11 == 0:
        return True
    else: return False
