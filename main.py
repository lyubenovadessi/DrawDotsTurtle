import turtle as t
import random

t.colormode(255)
dess = t.Turtle()

color_list = [(208, 173, 62), (28, 102, 153), (240, 227, 44), (167, 46, 92), (222, 58, 97), (136, 62, 52), (238, 77, 33), (191, 126, 168), (11, 96, 80), (240, 161, 196), (250, 220, 1), (115, 174, 215), (142, 220, 180), (9, 179, 214), (10, 191, 145), (140, 106, 186), (60, 47, 64), (144, 204, 118), (26, 118, 94), (70, 54, 111), (82, 58, 53), (82, 52, 101), (230, 173, 165), (235, 174, 13), (145, 211, 224), (12, 79, 110), (182, 185, 214), (44, 58, 75), (70, 55, 52), (22, 72, 62)]

dess.shape("turtle")
dess.color("black")
dess.speed(0)
dess.penup()
dess.hideturtle()
dess.setheading(225)
dess.forward(300)
dess.setheading(0)
num_dots = 100
for dot_count in range(1, num_dots + 1):
    dess.dot(20, random.choice(color_list))
    dess.penup()
    dess.forward(50)
    if dot_count % 10 == 0:
        dess.setheading(90)
        dess.forward(50)
        dess.setheading(180)
        dess.forward(500)
        dess.setheading(0)

my_screen = t.Screen()
my_screen.exitonclick()