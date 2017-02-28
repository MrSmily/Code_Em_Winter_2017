import turtle
t=turtle.Pen()
t.speed(9)

t.up()
t.backward(100)
t.down()
t.left(45)
t.forward(25)
t.backward(50)
t.forward(25)
t.right(90)

for i in range(181):
  t.forward(1)
  t.left(0.5)

t.left(90)
t.backward(25)
t.forward(50)

t.up()
t.right(45)
t.forward(50)
t.left(90)
t.forward(15)
t.down()

t.right(90)
t.forward(50)
t.left(90)
t.forward(5)
t.left(90)
t.forward(50)
t.left(90)
t.forward(5)

for i in range(25):
  t.left(90)
  t.forward(1)
  t.left(90)
  t.forward(5)
  t.right(90)
  t.forward(1)
  t.right(90)
  t.forward(5)

t.right(180)

t.up()
t.forward(87)
t.down()

t.left(90)
t.forward(50)
t.right(90)
t.forward(5)
t.right(90)
t.forward(50)
t.right(90)
t.forward(5)
t.right(90)
t.forward(50)
t.right(90)
t.forward(5)
t.left(90)

t.left(90)
t.forward(5)

for i in range(25):

  t.left(90)
  t.forward(1)
  t.left(90)
  t.forward(5)
  t.right(90)
  t.forward(1)
  t.right(90)
  t.forward(5)

t.up()

for i in range(25):

  t.forward(500)
  t.backward(5)
  t.forward(5)
  
t.down()
