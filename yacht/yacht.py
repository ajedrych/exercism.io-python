"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = lambda cards: 50 if len(set(cards)) == 1 else 0
ONES = lambda cards: sum(x for x in cards if x == 1)
TWOS = lambda cards: sum(x for x in cards if x == 2)
THREES = lambda cards: sum(x for x in cards if x == 3)
FOURS = lambda cards: sum(x for x in cards if x == 4)
FIVES = lambda cards: sum(x for x in cards if x == 5)
SIXES = lambda cards: sum(x for x in cards if x == 6)
FULL_HOUSE = lambda cards: sum(cards) if len(set(cards)) == 2 and any(cards.count(x) == 3 for x in set(cards)) else 0
FOUR_OF_A_KIND = lambda cards: sum(x * 4 for x in set(cards) if cards.count(x) >= 4)
LITTLE_STRAIGHT = lambda cards: 30 if sum(cards) == (1 + 2 + 3 + 4 + 5) else 0
BIG_STRAIGHT = lambda cards: 30 if sum(cards) ==  (2 + 3+ 4 + 5 + 6) else 0
CHOICE = lambda cards: sum(cards)


def score(dice, category):
    if (x > 0 and x < 7 for x in dice):
        return category(dice)
    pass
