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

# Pen
pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 130)
pen.color("red")
pen.write("  Player 2: 0", align="left", font=("Courier", 12, "normal"))
pen.color("blue")
pen.write("Player 1: 0  ", align="right", font=("Courier", 12, "normal"))



background.update()
