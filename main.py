import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# dispaly
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collution with food
    if snake.head.distance(food) < 15:
        food.refersh()
        snake.extend()
        scoreboard.increase_score()   # only increase_score (update is inside it)

    # detect collution with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):   # fixed last check
        scoreboard.reset()
        snake.reset()

    # detect collution with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
