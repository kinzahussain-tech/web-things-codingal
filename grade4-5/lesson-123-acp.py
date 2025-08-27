import turtle

# Create turtle object
t = turtle.Turtle()

# Draw a Triangle
t.color("blue")
t.begin_fill()
for _ in range(3):
    t.forward(100)   # Move forward
    t.left(120)      # Turn left 120 degrees
t.end_fill()

# Move to another position
t.penup()
t.goto(150, 0)   # Shift right
t.pendown()

# Draw a Rectangle
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(120)   # Length
    t.left(90)
    t.forward(60)    # Width
    t.left(90)
t.end_fill()

# Keep the window open
turtle.done()
