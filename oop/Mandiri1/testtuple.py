from turtle import *
speed(0)
i = 0
color('red')
def fun(n):
    global i
    forward(180)
    left(150)
    forward(200)
    left(100)
    i += 1
    if i<n:
        fun(n)

up()
goto(-80, -50)
down()
fun (50)
