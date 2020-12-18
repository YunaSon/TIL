from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymin)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactive()

        if True:
            print(3)
    
    def clicked(self, p):
        if self.active == True:
            if ((self.xmin <= p.getX() <= self.xmax) 
                  and (self.ymin <= p.getY() <= self.ymax)):
                return True
        else:
            return False
    
    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        '''버튼을 활성 상태로 한다.'''
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactive(self):
        '''버튼을 비활성 상태로 한다.'''
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

a = Button(myWin, center, 200, 300, 'test')
