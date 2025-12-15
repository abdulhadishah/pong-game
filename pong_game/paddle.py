from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("#00FFFF")
        self.penup()
        self.goto(position)
        self.speed(0)

    def move_up(self):
        y_goto = self.ycor() + 10
        self.goto(self.xcor(), y_goto)

    def move_down(self):
        y_goto = self.ycor() - 10
        self.goto(self.xcor(), y_goto)
