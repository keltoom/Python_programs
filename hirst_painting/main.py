# import colorgram
# rgb_colors=[]
# colors = colorgram.extract('image.jpg', 25)
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

kelly = t.Turtle()
kelly.penup()
kelly.hideturtle()
y = 0
for _ in range(10):
    kelly.setposition(-250, -230 + y)
    for _ in range(10):
        kelly.dot(20, random.choice(color_list))
        kelly.penup()
        kelly.forward(50)
        y += 5

screen = t.Screen()
screen.exitonclick()
