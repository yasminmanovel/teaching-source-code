

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
