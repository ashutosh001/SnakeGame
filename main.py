from turtle import Screen, Turtle
import time

class SnakeGame():
    def __init__(self):
        self.snake_size = 3
        self.snakes = list()

    def draw_snake(self):
        """Creates the initial snake using turtle"""
        starting_position = [0,-20,-40]
        for x in range(self.snake_size):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.up()
            snake.goto(starting_position[x],0)
            self.snakes.append(snake)

    def move_snake_left(self):
        """Moves the snake based left"""
        new_heading = self.snakes[0].heading() + 90
        self.snakes[0].setheading(new_heading)

    def move_snake_right(self):
        """Moves the snake based right"""
        new_heading = self.snakes[0].heading() + 270
        self.snakes[0].setheading(new_heading)
    
    def start_game(self):
        """Creates a window to show the playground and the snake"""
        my_screen = Screen()
        my_screen.setup(width=600,height=600)
        my_screen.bgcolor("black")
        my_screen.title("Snake Game")

        my_screen.listen()
        game_is_on = True

        my_screen.tracer(0) #turns off the animation
        self.draw_snake()

        while game_is_on:
            my_screen.update() #displays the current frame of the ongoing animation, valid when trace if off
            time.sleep(0.1)

            for snake_num in range(self.snake_size-1,0,-1):
                new_x = self.snakes[snake_num-1].xcor()
                new_y = self.snakes[snake_num-1].ycor()
                self.snakes[snake_num].goto(new_x,new_y)
            self.snakes[0].forward(20)

            my_screen.onkey(key='a',fun=self.move_snake_left)
            my_screen.onkey(key='d',fun=self.move_snake_right)

        my_screen.exitonclick()

if __name__ == "__main__":
    play = SnakeGame()
    play.start_game()