import random 

ABILITIES = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')

def modifier(score):
    return (score - 10) // 2

class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)
    
    def ability(self):
        dices = sorted(random.randint(1,6) for i in range(4))
        return sum(dices[1:4])