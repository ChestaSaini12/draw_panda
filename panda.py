import turtle
p=turtle.Turtle()
wn=turtle.Screen()
p.speed(2)
p.pensize(3)
def sphere(col, rad):
    p.begin_fill()
    p.fillcolor(col)
    p.circle(rad)
    p.end_fill()
# first ear
p.up()
p.goto(-50, 100)
p.down()
sphere("black",30)
# second ear
p.up()
p.goto(50, 100)
p.down()
sphere("black",30)
# draw face
p.up()
p.setpos(0, 5)
p.down()
sphere("white", 65)
# left eye
p.up()
p.setpos(-35, 75)
p.down()
sphere("black", 15)

p.up()
p.goto(-35, 77)
p.down()
sphere("white",7)
# right eye
p.up()
p.setpos(35, 75)
p.down()
sphere("black", 15)

p.up()
p.goto(35, 77)
p.down()
sphere("white",7)
# nose and mouth
p.up()
p.goto(0,40)
p.down()
sphere("black",11)


p.up()
p.goto(0,40)
p.down()
p.right(90)
p.circle(10, 180)

p.up()
p.goto(0,40)
p.down()
p.left(360)
p.circle(10, -180)
p.hideturtle()