from random import randrange

class MSDie:
    '''
        1. n면 주사위
            - 초기값은 1
        2. 주사위를 굴려 나오는 수
            - roll : 주사위를 굴려 나오는 수, 랜덤
            - setValue : user가 세팅할 수 있는 주사위 수 
    '''

    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = randrange(1, self.sides+1)
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

n7 = MSDie(7)
print(n7.value)
n7.roll()
print(n7.value)
n7.setValue(3)
print(n7.value)