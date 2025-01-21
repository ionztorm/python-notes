"""Snake for snake game."""

import turtle as t

SNAKE_STARTING_COORDINATES = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class."""

    def __init__(self)-> None:
        """Initialize the snake."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self) -> None:
        """Create a snake with 3segments."""
        for coordinate in SNAKE_STARTING_COORDINATES:
            self.add_segment(coordinate)

    def add_segment(self, position: tuple[int, int]) -> None:
        """Add a new segment to the snake."""
        snake = t.Turtle("square")
        snake.color("white")
        snake.speed("slowest")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)


    def extend(self) -> None:
        """Extend the length of the snake by adding a new segment to the snake."""
        self.add_segment(self.segments[-1].position())


    def move(self) -> None:
        """Move the snake."""
        # starting from the last segment, move each segment
        # to the position of the segment in front of it.
        # the make the first segment perform the next move
        for index in range(len(self.segments) -1, 0, -1):
            # get the coordinates of the next segment
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            # apply the coordinates to the current segment
            self.segments[index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        """Set snake to face upward."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Set snake to face downward."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Set snake to face leftward."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Set snake to face rightward."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self) -> None:
        """Reset the snake to the starting position."""
        for segment in self.segments:
            segment.goto(-1000,0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

