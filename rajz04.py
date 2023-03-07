from turtle import *
from random import randint

scr = Screen()
scr.bgcolor('black')

szinek = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

turs:list[Turtle] = []
for x in range(6):
    turs.append(Turtle())
    turs[x].pencolor(szinek[x])
    turs[x].width(randint(1, 5))
    turs[x].speed(0)
    sz = randint(-scr.window_width()/2, scr.window_width()/2)
    ho = randint(-scr.window_height()/2, scr.window_height()/2)
    turs[x].penup()
    turs[x].goto(sz, ho)
    turs[x].pendown()

for x in range(100):
    for t in turs:
        t.forward(x)
        t.left(58)

done()