import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for j in range(4):
    for i in range(4):
        t.fd(100)
        t.rt(90)
    t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(44)
for i in range(200):
    t.lt(1.8)
    t.fd(4.44)



turtle.done()