from graphics import *

### 그래픽 창을 띄운다.
win = GraphWin()

### 좌표 (100, 100)에 반지름이 30인 원에 색을 빨간색으로 칠한다.
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

### Text객체를 이용해여 좌표 (100, 100)에 "Red Circle"이라는 레이블을 단다.
label = Text(center, "Red Circle")
label.draw(win)

### Rectangle객체를 이용하여 정사각형을 그린다.
rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win)

oval = Oval(Point(20, 120), Point(180, 199))
oval.draw(win)
