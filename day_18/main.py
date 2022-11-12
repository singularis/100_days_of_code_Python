from turtle import Turtle, Screen
import random
import colorgram

painter = Turtle()
screen = Screen()
screen.colormode(255)
painter.speed(0)
painter.hideturtle()

paint_size = 10
dot_size = 10
distance_between_dots = 30


def colors_extractor():
    colors = colorgram.extract('collors.webp', 50)
    colors_for_use = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        full_rgb = (r, g, b)
        colors_for_use.append(full_rgb)
    return colors_for_use


def picture_printer(colors_list):
    x_center = ((paint_size + distance_between_dots) * paint_size) / 2
    painter.up()
    painter.setpos(-x_center, -x_center)
    for _ in range(paint_size):
        for _ in range(paint_size):
            rand_color = random.choice(colors_list)
            painter.color(rand_color)
            painter.dot(dot_size)
            painter.up()
            painter.forward(distance_between_dots)
        current_position = painter.pos()
        painter.setpos(-x_center, current_position[1] + distance_between_dots)


picture_printer(colors_extractor())

screen.exitonclick()
