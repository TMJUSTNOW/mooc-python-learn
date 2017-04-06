#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle, time

## 绘制一个正方形
def DrawSquare():
    screen = turtle.Screen()
    screen.setup(500, 500, 0, 0)
    screen.title("Turtle Games.")
    screen.bgcolor('white')

    # Draw a square
    square = turtle.Turtle()
    square.pensize(3)
    square.up();
    square.goto(-50, 0)
    square.down()
    square.color("hotpink", '')
    for i in range(4):
        square.forward(100)
        square.left(90)
    # square.exitonclick()

    smallSquare = turtle.Turtle()
    smallSquare.pensize(3)
    smallSquare.up()
    smallSquare.goto(-50, 50)
    smallSquare.down()
    smallSquare.color("hotpink")

    smallSquare.seth(45)
    smallSquare.fd(70)
    smallSquare.seth(-45)
    smallSquare.fd(70)

    smallSquare.seth(0)
    smallSquare.fd(-100)

    smallSquare.seth(-45)
    smallSquare.fd(70)
    smallSquare.seth(45)
    smallSquare.fd(70)


## 绘制一个三角形
def DrawTriangle():
    triangle = turtle.Turtle()
    triangle.up();
    triangle.goto(-50, 0)
    triangle.down()
    triangle.color("hotpink", '')
    triangle.pensize(3)
    for i in range(3):
        triangle.seth(i* 120)
        triangle.fd(108)

def main():
    DrawSquare()
    # DrawTriangle()
    time.sleep(60)

if __name__ == '__main__':
    main()