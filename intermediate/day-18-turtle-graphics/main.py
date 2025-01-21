from turtle import Turtle, Screen, colormode
import random


ttl = Turtle()
ttl.shape("turtle")
ttl.color("chartreuse3")

# Challenge 1 - draw a square

# for _ in range(0, 4):
#     ttl.forward(100)
#     ttl.left(90)

# Challenge 2 - Draw a dotted line
# for i in range(15):
#     ttl.forward(10)
#     ttl.penup()
#     ttl.forward(10)
#     ttl.pendown()

# Challenge 3 - Draw a Triangle, Square, Pentagon, Hexagon, Heptagon
# Octagon, nonagon, and decagon. Make each shape a random color

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


#
#
# def draw_shape(num_sides):
#     angles = 360 / num_sides
#     ttl.pencolor(random_color())
#     for _ in range(num_sides):
#         ttl.forward(100)
#         ttl.right(angles)
#
#
# for i in range(3, 11):
#     draw_shape(i)

# Challenge 4 - Random Walk

# ttl.pensize(10)
# turns = [ttl.right, ttl.left]
# ttl.speed("fastest")
#
#
# def random_walk(num_movements, move_distance):
#     for _ in range(num_movements):
#         ttl.pencolor(random_color())
#         ttl.forward(move_distance)
#         random.choice(turns)(90)
#
#
# random_walk(200, 30)

# Challenge 5 - draw a spirograph

ttl.speed("fastest")


# def turtle_spyrograph(circle_size, turn_angle):
#     repetitions = 360 / turn_angle
#     for _ in range(int(repetitions)):
#         ttl.pencolor(random_color())
#         ttl.circle(circle_size)
#         ttl.right(turn_angle)
def turtle_spyrograph(circle_size, heading_change):
    for _ in range(int(360 / heading_change)):
        ttl.pencolor(random_color())
        ttl.circle(circle_size)
        ttl.setheading(ttl.heading() + heading_change)


turtle_spyrograph(100, 5)

# keep this at the end of the file
screen = Screen()
screen.exitonclick()  # without this line, the window will close immediately after opening
