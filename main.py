import turtle

# Configurar a tela
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("pink")

# Criar a tartaruga
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)
pen.color("red")
pen.fillcolor("red")
pen.penup()

# Desenhar o coração
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

# Esconder a tartaruga temporariamente
pen.penup()
pen.goto(0, -150)
pen.color("black")
pen.write("I love you", align="center", font=("Arial", 18, "bold"))
pen.hideturtle()

# Mostrar a tartaruga novamente
pen.showturtle()

# Manter a janela aberta
turtle.done()
