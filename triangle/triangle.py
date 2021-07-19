def equilateral(sides):
    if 0 in sides:
        return False

    if sides[0] == sides[1] and sides[0] == sides[2]:
        return True
    else: return False


def isosceles(sides):
    if max(sides) > sum(sides) - max(sides) or 0 in sides:
        return False

    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    else: return False


def scalene(sides):
    if max(sides) > sum(sides) - max(sides) or 0 in sides:
        return False

    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    else: return False