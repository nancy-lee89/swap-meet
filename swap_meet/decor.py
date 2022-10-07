class Decor:
    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition == "poor":
            self.condition += 0
        if self.condition == "fair":
            self.condition += 1
        if self.condition == "good":
            self.condition += 2
        if self.condition == "excellent":
            self.condition += 3