class Allergies:

    ingredients = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16,
        "chocolate": 32, "pollen": 64, "cats": 128}

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        self.item = item
        return bool(self.score & Allergies.ingredients[item])

    @property
    def lst(self):
        list = []
        for allergy in Allergies.ingredients:
            if self.allergic_to(allergy):
                list.append(allergy)
        return list