from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.update()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
 
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_body()  


    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        
        if snake.segments[0].distance(segment) < 10:
            is_game_on =False
            score.game_over()


screen.exitonclick()
