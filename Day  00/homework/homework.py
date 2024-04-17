from turtle import *

#house
speed(30)
width(7)
      
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
color("yellow")
begin_fill()
forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window nomber 1
color("blue")
left(30)
forward(25)
left(90)
forward(70)
right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(66)

#window nomber 2
color("white")
forward(60)
 
color("blue")
left(90)
forward(38)
right(90)
forward(53)
right(90)
forward(38)
right(90)
forward(25)
right(90)
forward(38)
left(90)
forward(29)
left(90)
forward(38)
left(90)
forward(27)




exitonclick()

