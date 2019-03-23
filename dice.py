import  random

class Dice:
    def roll(self):
        self.x=random.randint(1,6)
        self.y=random.randint(1,6)
        print(f'({self.x},{self.y})')


dice=Dice()
dice.roll()