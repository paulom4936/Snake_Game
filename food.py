import turtle
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = None
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("yellow")
        self.speed("fastest")
        self.new_food_loc()

    def new_food_loc(self):
        random_x = random.randint(-320, 320)
        random_y = random.randint(-320, 320)
        self.goto(random_x, random_y)
