#Game Start

import turtle
t = turtle.Pen()

def MrSmilyPersonGuyThing():
    print ("You Win!")

print ("Hello there\n")

name = input("What is your name \n")

if name == "MrSmilyPersonGuyThing":
    MrSmilyPersonGuyThing()

print ("Alright %s... Let's start..." %(name))
print ("\n\n\n")

t.speed(0)
t.backward(150)
t.forward(300)
t.backward(160)
t.left(45)
t.forward(25)
t.right(90)
t.forward(25)
t.backward(25)
t.right(45)
t.backward(50)
t.left(90)
t.forward(25)
t.backward(50)
t.forward(25)
t.left(90)
t.forward(15)
t.right(90)
t.forward(12.5)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(12.5)

print ("What do you want to do?\n")
print ("A) Walk")
print ("B) Stand")
print ("C) Sleep")

choice = input()

#Ends
if choice == "A":
    print ("You walk forever and die")
    t.reset()
    t.speed(0)
    t.backward(150)
    t.forward(300)
    t.backward(160)
    t.left(90)
    t.left(45)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.backward(25)
    t.right(45)
    t.backward(50)
    t.left(90)
    t.forward(25)
    t.backward(50)
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(12.5)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(12.5)
    input()

#Ends
elif choice == "B":
    print ("You stand and get hit by a meteor and die.")

elif choice == "C":
    print ("You sleep and dream about...\n")
    print ("A) Unicorns")
    print ("B) Rainbows")
    print ("C) Death")

    choice1 = input()

    if choice == "A":
        print 
    























