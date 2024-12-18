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

            snake_head = snake.snake_segment[0]
 
            for snake_num in range(snake.snake_size-1,0,-1):
                #each snake segment takes the last position of the previous segment
                new_x = snake.snake_segment[snake_num-1].xcor()
                new_y = snake.snake_segment[snake_num-1].ycor()
                snake.snake_segment[snake_num].goto(new_x,new_y)
            snake_head.forward(20)

            #Detect collision with the food
            if snake_head.distance(food) < 15:
                score.increase_score()
                food.refresh()
                snake.increase_snake()
            
            #Detect collision with wall
            left_wall = snake_head.xcor() > 280
            right_wall = snake_head.xcor() < -300
            upper_wall = snake_head.ycor() > 280
            bottom_wall = snake_head.ycor() < -290
            if left_wall or right_wall or upper_wall or bottom_wall:
                score.reset_scoreboard()
                snake.reset_snake()

            #Detect collision with tail or any othe part of the body
            for x in range(1,snake.snake_size):
                segment = snake.snake_segment[x]
                if snake_head.distance(segment) < 10:
                    score.reset_scoreboard()
                    snake.reset_snake()              

        my_screen.exitonclick()

if __name__ == "__main__":
    play = SnakeGame()
    play.start_game()