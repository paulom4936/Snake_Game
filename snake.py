from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.last_heading = 0

    # create starting snake graphics
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_snake(pos)

    def add_snake(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snake_body.append(snake)

    def extend_snake(self):
        self.add_snake(self.snake_body[-1].position())

    def move_snake(self):
        for num_snake_body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[num_snake_body - 1].xcor()
            new_y = self.snake_body[num_snake_body - 1].ycor()
            self.snake_body[num_snake_body].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_heading = self.head.heading()

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for snake in self.snake_body:
            snake.goto(2000, 2000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
