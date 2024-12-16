from turtle import Screen
from snake import Snake
from snake_food import Food
from scoreboard import ScoreBoard
import time


class SnakeGame:
    def __init__(self):
        pass

    def start_game(self):
        """Creates a window to show the playground and the snake"""
        my_screen = Screen()
        my_screen.setup(width=600,height=600)
        my_screen.bgcolor("black")
        my_screen.title("Snake Game")

        my_screen.listen()
        game_is_on = True

        my_screen.tracer(0) #turns off the animation
        snake = Snake()
        snake.draw_snake()
        food = Food()
        score = ScoreBoard()

        my_screen.onkey(key="Up",fun=snake.move_snake_up)
        my_screen.onkey(key="Down",fun=snake.move_snake_down)
        my_screen.onkey(key="Left",fun=snake.move_snake_left)
        my_screen.onkey(key="Right",fun=snake.move_snake_right)

        while game_is_on:
            my_screen.update() #displays the current frame of the ongoing animation, valid when trace if off
            time.sleep(0.1)
 
            for snake_num in range(snake.snake_size-1,0,-1):
                new_x = snake.snake_segment[snake_num-1].xcor()
                new_y = snake.snake_segment[snake_num-1].ycor()
                snake.snake_segment[snake_num].goto(new_x,new_y)
            snake.snake_segment[0].forward(20)

            #Detect collision with the food
            if snake.snake_segment[0].distance(food) < 15:
                score.update_score()
                food.refresh()
                snake.increase_snake()

        my_screen.exitonclick()

if __name__ == "__main__":
    play = SnakeGame()
    play.start_game()