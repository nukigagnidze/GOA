from turtle import *

bgcolor("white")
# Create a turtle for drawing

# Draw castle base
penup()
goto(-150, -150)
pendown()
begin_fill()
color("gray")

# Draw rectangle for castle base
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)

end_fill()

# Draw left tower
penup()
goto(-150, 50)
pendown()
begin_fill()
color("darkgray")

# Draw rectangle for left tower
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)

end_fill()

# Draw middle tower
penup()
goto(0, 50)
pendown()
begin_fill()
color("darkgray")

# Draw rectangle for middle tower
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)

end_fill()

# Draw right tower
penup()
goto(150, 50)
pendown()
begin_fill()
color("darkgray")

# Draw rectangle for right tower
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)

end_fill()

# Draw roof
penup()
goto(-150, 50)
pendown()
begin_fill()
color("darkred")

# Draw triangle for roof
goto(0, 150)
goto(150, 50)
goto(-150, 50)

end_fill()

# Draw the king
penup()
goto(-100, -150)
pendown()
begin_fill()
color("blue")

# Draw circle for king
circle(30)

end_fill()

# Draw the king's crown
penup()
goto(-120, -120)
pendown()
begin_fill()
color("gold")

# Draw triangle for king's crown
goto(-80, -120)
goto(-100, -90)
goto(-120, -120)

end_fill()

# Draw the queen
penup()
goto(100, -150)
pendown()
begin_fill()
color("pink")

# Draw circle for queen
circle(30)

end_fill()

# Draw the queen's crown
penup()
goto(80, -120)
pendown()
begin_fill()
color("gold")

# Draw triangle for queen's crown
goto(120, -120)
goto(100, -90)
goto(80, -120)

end_fill()

# Draw flagpole
penup()
goto(150, 150)
pendown()
color("black")
pensize(3)

# Draw flagpole line
goto(150, 250)

# Draw flag
begin_fill()
goto(200, 250)
goto(200, 225)
goto(150, 225)
goto(150, 250)
end_fill()
right(90)
forward(10)  # draw bottom part of 'G'
backward(10)
left(90)
forward(10)
right(90)
forward(10)
right(90)
forward(5)
right(90)
forward(5)

# Draw 'O'
penup()
goto(170, 230)
pendown()
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)

# Draw 'A'
penup()
goto(185, 230)
pendown()
right(60)
forward(10)
right(120)
forward(10)
backward(5)
right(120)
forward(5)

exitonclick()