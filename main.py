import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("pink")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)
pen.color("red")
pen.fillcolor("red")
pen.penup()

pen.goto(0, -50)
pen.pendown()
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

pen.penup()
pen.goto(0, -150)
pen.color("black")
pen.write("Você não é um eletrocardiograma, mas fez meu coração dar uma arritmada de tanto amor", align="center", font=("Arial", 18, "bold"))
pen.hideturtle()

pen.showturtle()

turtle.done()
