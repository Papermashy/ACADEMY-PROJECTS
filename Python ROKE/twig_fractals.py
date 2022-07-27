from turtle import *
import random

def spiral(n):
    if n > 10:
        forward(n)
        left(50)
        spiral(n * 0.9)

def twig(n):
    pendown()
    pencolor("brown")

    if n > 10:
        width(n * 0.2)

        forward(n)
        left(30)
        twig(n * 0.5)
        right(60)
        twig(n * 0.5)
        left(30)
        back(n)
    else:
        r = random.randint(1, 5)
        if r != 1:
            pencolor("black")
            fillcolor("green")
            begin_fill()
            circle(random.randint(20, 50))
            end_fill()
            penup()
        else:
            pencolor("black")
            fillcolor("red")
            begin_fill()
            circle(random.randint(10, 30))
            end_fill()
            penup()


speed(0)
penup()
goto(0, -300)
left(90)
pendown()

#spiral(300)
twig(250)
exitonclick()



def mostbasicrecursivefunction(n):
    # we need to have some way of breaking out of the recursion to avoid a recursion error
    if n <= 990:
        print(f"Hello {n}")
        mostbasicrecursivefunction(n + 1)
    else:
        print("The end")


# 5! = 5 x 4 x 3 x 2 x 1   = 120
# 5! = 5 x 4!
# 4! = 4 x 3!
# 3! = 3 x 2!
# n! = n x (n - 1)!
def fctrl(n):
    if n > 1:
        return n * fctrl(n - 1)
    else:
        return n
# it would be simpler to do this with Python's maths library factorial function...

#print("Before")
#mostbasicrecursivefunction(1)
#print(fctrl(5))
#print("After")



def fn(n):
    if n > 0:
        print("*", end = "")
        fn(n - 1)

for i in range(3):
    fn(i)
else:
    fn(1)

# final output will be ****