from turtle import *

background = Screen()
background.setup(width=400, height=300)
background.bgcolor("green")
background.tracer(0)




# Player 1
p1 = Turtle()
p1.speed(0)
p1.shape("square")
p1.color("blue")
p1.penup()
p1.goto(-190, 0)
background.update()

# Player 2
p2 = Turtle()
p2.speed(0)
p2.shape("square")
p2.color("red")
p2.penup()
p2.goto(190, 0)
background.update()

# Create ball
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
background.update()
