from turtle import *
from random import randint

scr = Screen()
scr.bgcolor('black')

tur = Turtle()
tur.width(2)
tur.shape('turtle')
tur.speed('fastest')

szinek = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

for x in range(256):
    tur.pencolor(szinek[x%6])
    tur.penup()
    tur.forward(x*3)
    tur.right(58)
    tur.pendown()
    tur.write("cica", font=('Arial', int((x / 4) + 1)))

done()