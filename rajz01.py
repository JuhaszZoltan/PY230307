from turtle import *
from random import randint

scr = Screen()
scr.bgcolor('black')

tur = Turtle()
# tur.pencolor('white')
tur.width(2)
tur.shape('turtle')
tur.speed('fastest')

#           0       1        2        3         4         5
szinek = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

for x in range(256):
    r = f'{randint(0, 255):02X}'
    g = f'{randint(0, 255):02X}'
    b = f'{randint(0, 255):02X}'
    tur.pencolor(f'#{r}{g}{b}')
    tur.forward(x)
    tur.right(56)

done()