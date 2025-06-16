import turtle
n=200
te = turtle.Turtle()
te.shape("turtle")
te.color("orange")
# 위,왼,아래, 오른 
te.left(90)
te.forward(n)
te.left(90)
te.forward(n)
te.left(90)
te.forward(n)
te.left(90)
te.forward(n)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
# 삼각형 그리기
t.forward(n)
t.right(120)
t.forward(n)
t.right(120)
t.forward(n)

t2=turtle.Turtle()
t2.shape("turtle")
t2.color("black")
t2.forward(70)
t2.right(120)
t2.forward(70)
t2.right(120)
t2.forward(70)


turtle.done()
