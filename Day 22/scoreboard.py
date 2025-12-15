from turtle import Turtle

FONT = ("Arial", 60, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#EAEAEA")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

class BoundaryLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#00bcd4")
        self.pensize(4)
        self.penup()
        self.goto(0, 280)
        self.setheading(270)
        self.draw_center_line()

    def draw_center_line(self):
        for _ in range(30):
            while self.ycor() > - 280:
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)