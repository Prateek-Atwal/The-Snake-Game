from turtle import Turtle
FIRST_SEGMENT_START_X = -261
SEGMENT_SIZE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0  # reference being the turtle documentation for heading


class Snake:
    def __init__(self):
        self.tls = []
        self.create_snake()
        self.head = self.tls[0]

    def create_snake(self):
        for i in range(3):
            tl = Turtle("square")
            tl.color("white")
            tl.penup()
            if i > 0:
                tl.setposition(self.tls[i - 1].xcor() - SEGMENT_SIZE, self.tls[i - 1].ycor())
            else:
                tl.setx(FIRST_SEGMENT_START_X)
            self.tls.append(tl)

    def extend(self):
        tl = Turtle("square")
        tl.color("white")
        tl.penup()
        tl.setposition(self.tls[-1].xcor() - SEGMENT_SIZE, self.tls[-1].ycor())
        self.tls.append(tl)

    def move(self, dist):
        for i in range(len(self.tls) - 1, 0, -1):
            self.tls[i].setx(self.tls[i - 1].xcor())
            self.tls[i].sety(self.tls[i - 1].ycor())
        self.head.forward(dist)

    def realign(self):
        self.head.setx(FIRST_SEGMENT_START_X)
        for i in range(1, len(self.tls)):
            self.tls[i].setx(self.tls[i - 1].xcor() - SEGMENT_SIZE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.tls[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.tls[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.tls[0].setheading(DOWN)

    def bit_itself(self):
        for i in range(1, len(self.tls)):
            if self.head.distance(self.tls[i]) < 10:
                return True
        return False
