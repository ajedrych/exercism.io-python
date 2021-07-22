def recite(start, take=1):
    text = []
    for i in range(start, start - take, -1):
        if i > 2:
            text += [f"{i} bottles of beer on the wall, {i} bottles of beer.",
                f"Take one down and pass it around, {i - 1} bottles of beer on the wall."]
        if i == 2:
            text += [f"{i} bottles of beer on the wall, {i} bottles of beer.",
                f"Take one down and pass it around, {i - 1} bottle of beer on the wall."]
        if i == 1:
            text += [f"1 bottle of beer on the wall, 1 bottle of beer.",
                f"Take it down and pass it around, no more bottles of beer on the wall."]
        if i == 0: 
            text += [f"No more bottles of beer on the wall, no more bottles of beer.",
                f"Go to the store and buy some more, 99 bottles of beer on the wall."]
        if i - 1 > start-take:
            text += [""]
    return text