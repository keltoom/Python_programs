from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finished_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def move_back(self):
        self.goto(STARTING_POSITION)
