from turtle import Screen, Turtle

class Snake():
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

    def move_snake_up(self):
        """Moves the snake based up"""
        new_heading = self.snakes[0].heading() + 0
        self.snakes[0].setheading(new_heading)

    def move_snake_down(self):
        """Moves the snake based down"""
        new_heading = self.snakes[0].heading() + 180
        self.snakes[0].setheading(new_heading)

    def move_snake_left(self):
        """Moves the snake based left"""
        new_heading = self.snakes[0].heading() + 90
        self.snakes[0].setheading(new_heading)

    def move_snake_right(self):
        """Moves the snake based right"""
        new_heading = self.snakes[0].heading() + 270
        self.snakes[0].setheading(new_heading)
    

