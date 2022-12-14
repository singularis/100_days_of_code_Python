from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, snake_size):
        self.x = 0
        self.segments = []
        self.snake_size = snake_size
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.x = 0
        for segment in range(3):
            self.add_segment(segment)

    def add_segment(self, segment):
        snake_segment = Turtle()
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.shape("square")
        snake_segment.width(self.snake_size)
        snake_segment.setx(x=self.x)
        self.x -= self.snake_size
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
 
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(self.snake_size)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

