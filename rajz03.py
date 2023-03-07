from turtle import *
from random import randint

scr = Screen()
scr.bgcolor('black')

tur = Turtle()
tur.width(2)
tur.shape('turtle')
tur.speed('fastest')

szinek = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

tur.pencolor(szinek[1])

tur.circle(100, 180)
tur.left(90)
tur.forward(400)

done()