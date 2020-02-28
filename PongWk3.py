from turtle import *

background = Screen()
background.setup(width=400, height=300)
background.bgcolor("green")
background.tracer(0)

# create dotted line
line = Turtle()
line.penup()
line.goto(0, 160)
line.right(90)
line.color("white")
for num in range(16):
  line.penup()
  line.forward(10)
  line.pendown()
  line.forward(10)
line.color("green")
line.forward(20)

# Set score at beginning of game
score_1 = 0
score_2 = 0

# Player 1
p1 = Turtle()
p1.speed(0)
p1.shape("square")
p1.color("blue")
# p1.turtlesize(stretch_wid=5,stretch_len=1)
p1.penup()
p1.goto(-350/2, 0)

# Player 2
p2 = Turtle()
p2.speed(0)
p2.shape("square")
p2.color("red")
# p2.resizemode("user")
# p2.shapesize(5,1)
p2.penup()
p2.goto(350/2, 0)

# Create ball
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = Turtle()
pen.speed(0)
pen.shape("square")

pen.penup()
pen.hideturtle()
pen.goto(0, 260/2)
pen.color("red")
pen.write("  Player 2: 0", align="left", font=("Courier", 12, "normal"))
pen.color("blue")
pen.write("Player 1: 0  ", align="right", font=("Courier", 12, "normal"))

# Functions
def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)

# Keyboard bindings
background.listen()
background.onkey(p1_up, "w")
background.onkey(p1_down, "s")
background.onkey(p2_up, "Up")
background.onkey(p2_down, "Down")

