from turtle import Screen, Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_size = 3
        self.snake_segment = list() #This lists contains all the segments of the snake, initially 3 segments

    def draw_snake(self):
        """Creates the initial snake using turtle"""
        starting_position = [0,-20,-40]
        for x in range(self.snake_size):
            snake_segment = Turtle()
            snake_segment.speed("slowest")
            snake_segment.shape("square")
            snake_segment.color("white")
            snake_segment.up()
            snake_segment.goto(starting_position[x],0)
            self.snake_segment.append(snake_segment)

    def increase_snake(self):
        """Makes the snake longer once the snake eats food"""
        new_snake_segment = Turtle()
        new_snake_segment.speed("slowest")
        new_snake_segment.shape("square")
        new_snake_segment.color("white")
        new_snake_segment.up()
        x_axis = self.snake_segment[self.snake_size-1].xcor()
        y_axis = self.snake_segment[self.snake_size-1].ycor()
        new_snake_segment.goto(x_axis,y_axis)
        self.snake_segment.append(new_snake_segment)
        self.snake_size += 1


    def move_snake_up(self):
        """Moves the snake head up"""
        if self.snake_segment[0].heading() != DOWN: #to prevent snake backward movement
            self.snake_segment[0].setheading(UP) #only changing the head segment

    def move_snake_down(self):
        """Moves the snake head down"""
        if self.snake_segment[0].heading() != UP:
            self.snake_segment[0].setheading(DOWN)

    def move_snake_left(self):
        """Moves the snake head left"""
        if self.snake_segment[0].heading() != RIGHT:
            self.snake_segment[0].setheading(LEFT)

    def move_snake_right(self):
        """Moves the snake head right"""
        if self.snake_segment[0].heading() != LEFT:
            self.snake_segment[0].setheading(RIGHT)
    

