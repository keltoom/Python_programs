from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.setposition(x, y)

    def up(self):
        new_y = self.paddle.ycor() + 30
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 30
        self.paddle.goto(self.paddle.xcor(), new_y)
