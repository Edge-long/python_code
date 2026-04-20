from random import randint

class Die:
    def __init__(self,sider=6):
        self.sider = sider
        self.amount = 1
    def roll_die(self):
        while self.amount <= 1:
            print(f"{randint(1,self.sider)}")
            self.amount += 1

award = Die()
award.roll_die()