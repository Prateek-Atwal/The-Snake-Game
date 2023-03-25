from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc = Screen()
snake = Snake()
food = Food()
sb = Scoreboard()

sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("The Snake Game")
sc.tracer(0)
sc.listen()

sc.onkeypress(snake.up, "Up")
sc.onkeypress(snake.down, "Down")
sc.onkeypress(snake.left, "Left")
sc.onkeypress(snake.right, "Right")
snake_speed = 0.1
game_is_on = True
while game_is_on:
    sc.update()
    snake.move(20)
    time.sleep(snake_speed)
    if (snake.bit_itself() or snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280
            or snake.head.ycor() < -290):
        game_is_on = False
        sb.game_over()
        continue
    if snake.head.distance(food) < 15:
        print("Ate some!")
        sb.update_score()
        snake.extend()
        food.refresh()
        snake_speed *= 0.9

sc.exitonclick()
