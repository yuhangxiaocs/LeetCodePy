from turtle import *
import random
import math

# 设置色彩模式是RGB:
colormode(255)

width(1)

speed("fastest")


def draw_random(times):
    ran = 300
    for i in range(times):
        penup()
        x, y = random.randint(-ran, ran), random.randint(-ran, ran)
        goto(x, y)

        pendown()
        r, g, b = random.randint(150, 200), random.randint(150, 200), random.randint(150, 200)
        color(r, g, b)
        rad = random.randint(5, 50)
        steps = random.randint(3, 100)
        begin_fill()
        pencolor(r, g, b)

        circle(rad, steps=steps)
        end_fill()

        penup()

        r = r + 1
        g = g + 2
        b = b + 3
        pencolor(r % 200, g % 200, b % 200)


#
# draw_random(500)
def logo():
    color(50, 50, 50)
    begin_fill()

    for i in range(100):
        circle(100, steps=i + 3)
    end_fill()
    penup()

    done()


def sun():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        speed(10)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


# sun()


def z_scan():
    hideturtle()
    x = 10
    color('red')
    # begin_fill()
    while x < 200:
        forward(1)
        right(145)
        forward((int)(math.sqrt(2) * x))
        left(45)
        forward(1)
        left(45)
        forward((int)(math.sqrt(2) * (x + 1)))
        right(45)
        x += 1
    # end_fill()

    done()


z_scan()
