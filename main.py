from turtle import Screen

from snake import Snake
from food import Food
from scoring import Score

import time

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="s", fun=snake.move_down)
screen.onkey(key="d", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 18:
        snake.extend_snake()
        food.new_food_loc()
        score.scoring()

    # detect collision with wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < - 340:
        snake.reset()
        score.reset_snake()

    # detect with collision with own body
    for snake_body in snake.snake_body[1:]:
        if snake.head.distance(snake_body) < 10:
            snake.reset()
            score.reset_snake()

screen.exitonclick()
