import turtle

colors = ["red", "blue","white" ,"yellow" ,"pink","green"]
turtle.bgcolor("black")
t = turtle
for x in range(360):

    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(66)
