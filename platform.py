from turtle import *
from time import sleep

print("Як буде виглядати Україна 2100 році? Напевно задумувся кожен")
sleep(5)
# Створення екземпляру черепашки
t1 = Turtle()
def draw_flag(color, x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color(color)
    t1.begin_fill()
    for x in range(2):
        t1.forward(340/2)
        t1.right(90)
        t1.forward(60/2)
        t1.right(90)
    t1.end_fill()
draw_flag('blue', -150, 30)
draw_flag('yellow', -150, 0)

t1.left(90)
t1.penup()
t1.forward(200/2)
t1.pendown()
t1.color('black')
t1.forward(20/2)
t1.right(90)
t1.forward(50/2)
t1.right(90)
t1.forward(70/2)
t1.right(90)
def num_second(lenght_1):
    for m in range(1,5):
        t1.forward(lenght_1)
        t1.left(90)
        t1.forward(lenght_1)
        t1.right(90)
num_second(10/2)
def num_first(moove,left_moove):
    t1.left(left_moove)
    t1.forward(30/2)
    t1.left(left_moove)
    t1.forward(moove)
    t1.penup()
    t1.forward(moove)
    t1.left(left_moove)
    t1.pendown()
    t1.forward(150/2)
    t1.left(135)
    t1.forward(moove)
    t1.backward(moove)
    t1.right(225)
    t1.penup()
    t1.forward(moove)
    t1.pendown()
num_first(50/2,90)
def num_zero(degrees,lenght_2,lenght_3):
    for m in range(1, 3):
        t1.forward(lenght_2)
        t1.right(degrees)
        t1.forward(lenght_3)
        t1.right(degrees)
        t1.forward(lenght_2)
        t1.right(degrees)
        t1.forward(lenght_3)
        t1.right(degrees)
        t1.penup()
        t1.forward(110/2)
        t1.pendown()
num_zero(90,60/2,150/2)
t1.reset()
print("На мою думку у 2100 буде Виглядати так:")
sleep(5)
t2 = Turtle()
t2.penup()
t2.forward(50/3)
t2.left(90)
t2.pendown()
t2.color('grey')
t2.forward(300/3)
t2.right(90)
t2.forward(200/3)
t2.right(90)


def windows_1(lr,fd):
    for x in range(1, 8):
        t2.forward(fd)
        t2.right(lr)
        t2.color('blue')
        t2.begin_fill()
        t2.forward(170/3)
        t2.left(lr)
        t2.forward(fd)
        t2.left(lr)
        t2.forward(170/3)
        t2.right(lr)
        t2.backward(fd)
        t2.end_fill()
        t2.color('grey')
        t2.forward(fd)
windows_1(90, 20/3)
t2.forward(20/3)
t2.right(90)
t2.forward(200/3)
t2.left(90)
t2.penup()
t2.forward(1)
t2.pendown()
t2.right(90)
t2.color('green')
t2.begin_fill()
t2.forward(810/3)
t2.left(90)
t2.forward(350/3)
t2.left(90)
t2.forward(810)
t2.left(90)
t2.forward(350/3)
t2.end_fill()
t2.penup()
t2.color('grey')
t2.right(90)
t2.forward(30/3)
t2.left(90)
t2.pendown()
t2.begin_fill()
t2.forward(300/5)
t2.left(90)
t2.forward(30/3)
t2.left(90)
t2.forward(300/5)
t2.end_fill()
t2.left(90)
t2.forward(300/5)
t2.left(90)
t2.forward(300/5)
t2.right(90)
t2.forward(200/4)
t2.right(90)
def windows_2(lr,fd):
    for x in range(1, 8):
        t2.forward(fd)
        t2.right(lr)
        t2.color('blue')
        t2.begin_fill()
        t2.forward(170/3)
        t2.left(lr)
        t2.forward(fd)
        t2.left(lr)
        t2.forward(170/3)
        t2.right(lr)
        t2.backward(fd)
        t2.end_fill()
        t2.color('grey')
        t2.forward(fd)
windows_2(90, 20/3)
t2.forward(20/3)
t2.right(90)
t2.forward(170/3)
t2.right(90)
t2.begin_fill()
t2.forward(300/3)
t2.left(90)
t2.forward(30/3)
t2.left(90)
t2.forward(300/3)
t2.left(90)
t2.forward(30/3)
t2.end_fill()
t2.right(180)
t2.penup()
t2.forward(75/3)
t2.right(90)
t2.forward(29)
t2.pendown()
t2.color('yellow')
t2.begin_fill()
t2.circle(25/2)
t2.end_fill()
t1.color('green')
t1.penup()
t1.right(90)
t1.forward(1)
t1.left(90)
t1.pendown()
t1.begin_fill()
t1.forward(755/4)
t1.right(90)
t1.forward(350/4)
t1.right(90)
t1.forward(755/4)
t1.right(90)
t1.forward(350/4)
t1.end_fill()
exitonclick()
