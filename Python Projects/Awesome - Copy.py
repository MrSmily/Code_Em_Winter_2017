#Start
def MrSmilyPersonGuyThing():
    print ("You Win")
    input()

import turtle
t = turtle.Pen()

print ("Input: Super Mini Internet, Tic-Tac-Toe, Drawing, Adventure Story, or Calculator.\n")

COMMAND42 = "MrSmilyPersonGuyThing"
COMMAND101 = "Super Mini Internet"
COMMAND102 = "Tic-Tac-Toe"
COMMAND103 = "Drawing"
COMMAND104 = "Adventure Story"
COMMAND105 = "Calculator"

def handle_command(command):

    response = ""

    #Awesome
    if command.find(COMMAND42) >= 0:
        MrSmilyPersonGuyThing()

    #Super Mini Internet
    elif command.find(COMMAND101) >= 0:
        
        COMMAND11 = "What is water?" 
        COMMAND21 = "Pi."
        COMMAND31 = "Speak computer."
        COMMAND41 = "How old are you?"
        COMMAND101101001 = "ERROR..."

        def handle_command(command):

            if command.find(COMMAND11) >= 0:
                response = "H20"

            elif command.find(COMMAND21) >= 0:
                response = "3.141592653589793238462643383...etc."

            elif command.find(COMMAND31) >= 0:
                response = "00000000000000000100000000000000000000111100000000000000000001011000000000000011010011111100000000000011000000"

            elif command.find(COMMAND41) >= 0:
                response = "I am 4,967,435,537.98 years old."

            elif command.find(COMMAND101101001) >= 0:
                for i in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
                    print ("ERROR...")

                response = "Shut Down..."
                

            return response

        while True:
            command = input('Super Mini Internet: -->')
            response = handle_command(command)
            print(response)
            print

    #Needs a CPU
    #Tic-Tac-Toe
    elif command.find(COMMAND102) >= 0:

        print ("Player 1: Please input x and then a number between 1 and 9.")
        print ("Player 2: Please input o and then a number between 1 and 9.\n")
        
        t.reset()
        
        t.speed(0)

        t.up()
        t.right(90)
        t.forward(50)
        t.left(90)
        t.backward(150)
        t.down()

        t.forward(300)

        t.up()
        t.left(90)
        t.forward(100)
        t.right(90)
        t.backward(300)
        t.down()

        t.forward(300)

        t.up()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.down()

        t.forward(300)

        t.up()
        t.right(90)
        t.forward(100)
        t.right(90)
        t.down()

        t.forward(300)

        t.up()
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(150)
        t.down()

        COMMAND1 = "1x" 
        COMMAND2 = "2x"
        COMMAND3 = "3x"
        COMMAND4 = "4x"
        COMMAND5 = "5x"
        COMMAND6 = "6x"
        COMMAND7 = "7x"
        COMMAND8 = "8x"
        COMMAND9 = "9x"
        COMMAND10 = "1o"
        COMMAND11 = "2o"
        COMMAND12 = "3o"
        COMMAND13 = "4o"
        COMMAND14 = "5o"
        COMMAND15 = "6o"
        COMMAND16 = "7o"
        COMMAND17 = "8o"
        COMMAND18 = "9o"

        def handle_command(command):
    
            response = ""

            if command.find(COMMAND1) >= 0:
                t.up()
                t.right(135)
                t.forward(100)
                t.down()
                t.forward(90)
                t.backward(45)
                t.left(90)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.right(90)
                t.up()
                t.backward(145)
                t.right(225)
                t.down()
                
                response = ""

            elif command.find(COMMAND2) >= 0:
                t.right(180)
        
                t.up()
                t.forward(100)
                t.down()
                t.right(45)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.left(90)
                t.forward(45)
                t.backward(90)
                t.up()
                t.forward(45)
                t.right(225)
                t.forward(100)
                t.down()
        
                response = ""
        
        

            elif command.find(COMMAND3) >= 0:
                t.left(135)
                t.up()
                t.forward(100)
                t.down()
                t.forward(90)
                t.backward(45)
                t.left(90)
                t.forward(45)
                t.backward(90)
                t.up()
                t.forward(45)
                t.right(90)
                t.backward(145)
                t.right(135)
                t.down()
                
                response = ""
        
        
        

            elif command.find(COMMAND4) >= 0:
                t.right(90)
                t.up()
                t.forward(100)
                t.down()
                t.right(45)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.left(90)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.up()
                t.right(45)
                t.backward(100)
                t.left(90)
                t.down()
                
                response = ""
        
        

            elif command.find(COMMAND5) >= 0:
                t.right(45)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.left(90)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.right(45)
                
                response = ""
        
            elif command.find(COMMAND6) >= 0:
                t.left(90)
                t.up()
                t.forward(100)
                t.down()
                t.left(45)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.right(90)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.up()
                t.left(45)
                t.backward(100)
                t.right(90)
                
                response = ""
        
            elif command.find(COMMAND7) >= 0:
                t.right(45)
                t.up()
                t.forward(100)
                t.down()
                t.forward(90)
                t.backward(45)
                t.right(90)
                t.forward(45)
                t.backward(90)
                t.up()
                t.forward(45)
                t.left(90)
                t.backward(145)
                t.left(135)
                t.right(90)
                t.down()
                response = ""
        
            elif command.find(COMMAND8) >= 0:
                t.up()
                t.forward(100)
                t.down()
                t.left(45)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.right(90)
                t.forward(45)
                t.backward(90)
                t.up()
                t.forward(45)
                t.left(225)
                t.forward(100)
                t.right(180)
                t.down()
                response = ""
        
            elif command.find(COMMAND9) >= 0:
                t.up()
                t.left(45)
                t.forward(100)
                t.down()
                t.forward(90)
                t.backward(45)
                t.right(90)
                t.forward(45)
                t.backward(90)
                t.forward(45)
                t.left(90)
                t.up()
                t.backward(145)
                t.right(45)
                t.down()
                
                response = ""

            elif command.find(COMMAND10) >= 0:
                t.up()
                t.right(135)
                t.forward(105)
                t.left(45)
                t.forward(25)
                t.down()
                for i in range(180):
                    t.right(2)
                    t.forward(1)

                t.up()
                t.backward(25)
                t.right(45)
                t.backward(105)
                t.right(225)
                t.down()

                response = ""

            elif command.find(COMMAND11) >= 0:
                t.right(180)
        
                t.up()
                t.forward(75)
                t.left(90)
                t.down()
                for i in range(180):
                    t.right(2)
                    t.forward(1)

                t.left(90)
                t.up()
                t.forward(75)
                t.down()
                
                response = ""

            elif command.find(COMMAND12) >= 0:
                t.left(135)
                t.up()
                t.forward(105)
                t.right(45)
                t.forward(25)
                t.down()
                for i in range(180):
                    t.left(2)
                    t.forward(1)
                t.up()
                t.backward(25)
                t.left(45)
                t.backward(105)
                t.right(135)
                t.down()
                response = ""
            
            elif command.find(COMMAND13) >= 0:
                t.up()
                t.right(90)
                t.forward(75)
                t.right(90)
                t.down()
                for i in range(180):
                    t.left(2)
                    t.forward(1)
                t.up()
                t.left(90)
                t.backward(75)
                t.left(90)
                t.down()
                response = ""

            elif command.find(COMMAND14) >= 0:
                t.up()
                t.backward(30)
                t.right(90)
                t.down()
                for i in range(180):
                    t.left(2)
                    t.forward(1)
                t.up()
                t.left(90)
                t.forward(30)
                t.down()
                response = ""

            elif command.find(COMMAND15) >= 0:
                t.up()
                t.left(90)
                t.forward(75)
                t.left(90)
                t.down()
                for i in range(180):
                    t.right(2)
                    t.forward(1)
                t.up()
                t.right(90)
                t.backward(75)
                t.right(90)
                t.down()

            elif command.find(COMMAND16) >= 0:
                t.up()
                t.right(45)
                t.forward(105)
                t.right(45)
                t.forward(25)
                t.down()
                for i in range(180):
                    t.left(2)
                    t.forward(1)

                t.up()
                t.backward(25)
                t.left(45)
                t.backward(105)
                t.left(225)
                t.right(180)
                t.down()

                response = ""

            elif command.find(COMMAND17) >= 0:      
                t.up()
                t.forward(75)
                t.right(90)
                t.down()
                for i in range(180):
                    t.left(2)
                    t.forward(1)

                t.right(90)
                t.up()
                t.forward(75)
                t.down()
                
                response = ""

            elif command.find(COMMAND18) >= 0:
                t.up()
                t.left(45)
                t.forward(105)
                t.left(45)
                t.forward(25)
                t.down()
                for i in range(180):
                    t.right(2)
                    t.forward(1)

                t.up()
                t.backward(25)
                t.right(45)
                t.backward(105)
                t.left(225)
                t.left(90)
                t.down()

                response = ""

            return response

        while True:
            command = input('Your Turn...')
            response = handle_command(command)
            print(response)
            print

    #Drawing
    elif command.find(COMMAND103) >= 0:

        t.reset()

        t.color('black', 'sienna')

        print ("Drawing...")
        
        t.up()
        t.backward(250)
        t.right(90)
        t.forward(100)
        t.down()

        t.begin_fill()

        t.right(180)
        t.forward(250)
        t.right(45)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(45)
        t.forward(250)
        t.right(90)
        t.forward(140)

        t.end_fill()

        t.color('black', 'saddlebrown')

        t.begin_fill()

        t.right(35)
        t.forward(20)
        t.right(55)
        t.forward(250)
        t.right(90)
        t.right(35)
        t.forward(20)
        t.backward(20)
        t.left(35)
        t.left(45)
        t.forward(100)
        t.right(80)
        t.forward(20)
        t.right(100)
        t.forward(100)
        t.left(45)
        t.forward(250)
        t.right(90)

        t.right(35)
        t.forward(20)
        t.right(55)
        t.forward(250)
        t.right(90)
        t.right(35)
        t.forward(20)
        t.backward(20)
        t.left(35)
        t.left(45)
        t.forward(100)
        t.right(80)
        t.forward(20)
        t.right(100)
        t.forward(100)

        t.end_fill()

        print ("Drawing...")

        t.backward(100)
        t.left(80)

        t.up()
        t.right(35)
        t.forward(50)
        t.left(55)
        t.forward(45)
        t.down()

        t.speed(0)

        t.color('black', 'white')
        t.begin_fill()

        for i in range(360):
            t.right(1)
            t.forward(1)

        t.end_fill()

        t.color('black')

        t.up()
        t.right(55)
        t.forward(45)
        t.right(90)
        t.down()
        
        t.forward(35)
        t.right(90)
        t.forward(45)

        t.up()
        t.backward(200)
        t.down()

        t.up()
        t.forward(50)
        t.down()

        t.color('black')
        t.begin_fill()
        
        t.right(90)
        t.forward(35)
        t.backward(70)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(50)

        t.end_fill()

        t.color('black', 'saddlebrown')

        t.begin_fill()

        t.right(50)
        t.forward(35)
        t.right(40)
        t.right(90)
        t.forward(95)
        t.right(90)
        t.right(40)
        t.forward(35)

        t.end_fill()

        t.up()
        t.left(40)
        t.forward(70)
        t.down()

        t.begin_fill()

        t.left(40)
        t.forward(35)
        t.right(40)
        t.right(90)
        t.forward(95)
        t.right(90)
        t.right(40)
        t.forward(35)

        t.end_fill()

        t.color('silver')

        t.up()
        t.right(50)
        t.forward(50)
        t.left(90)
        t.forward(35)
        t.right(90)
        t.down()

        t.width(5)
        
        t.left(70)
        t.forward(250)
        t.left(20)

        t.begin_fill()
        
        t.forward(50)
        t.backward(100)
        t.right(35)
        t.forward(100)
        t.left(35)
        t.forward(100)
        t.left(145)
        t.forward(100)

        t.end_fill()

        t.color('black')

        t.up()
        t.backward(50)
        t.left(35)
        t.forward(25)
        t.right(45)
        t.down()
        
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.backward(20)
        t.left(45)
        t.backward(40)
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.backward(20)
        t.left(45)
        t.backward(20)
        t.forward(20)
        t.right(135)
        t.forward(10)
        t.right(90)

        print ("Drawing...")

        for i in range(150):
            t.left(5)
            t.forward(1)

        print ("Done...")

        t.up()

        for i in range(100):
            t.forward(500000000000)
            t.backward(50)


        response = "Hope you like them. :)\n\n\n"
        
    #Adventure Story
    elif command.find(COMMAND104) >= 0:

        t.reset()

        print ("Hello there!\n")
        print ("Welcome to my Adventure!\n")

        #Name Select
        name = input("What is your name?\n")
        if name == "Person":
            Person()
        print ("Alright %s, let's start our Adventure!!!\n" %(name))
        print ("\n\n\n")

        #Adventure Starts
        print ("You find yourself lost in the Jungle... \n")

        print ("You see a small path to your right.\n")

        print ("What do you do?")
        print ("A) Start walking")
        print ("B) Wait for help")

        choice = input()

        if choice == "A":
            t.speed(0)
            t.up()
            t.right(90)
            t.forward(100)
            t.left(90)
            t.down()

            t.left(90)
            t.forward(200)
            t.right(45)
            t.forward(100)
            t.backward(100)
            t.left(45)
            t.forward(100)
            t.backward(100)
            t.left(45)
            t.forward(100)
            t.backward(100)
            t.right(45)
            t.backward(175)
            t.right(90)
            t.forward(5)

            for i in range(4):
                t.right(90)
                t.forward(10)
            
            print ("You start walking and come to a fork in the path. Which way do you go?")
            print ("A) go right")
            print ("B) Go Strait")
            print ("C) Go left")

            choice2 = input()

            if choice2 == "A":
                
                t.reset()
                t.up()
                t.right(90)
                t.forward(50)
                t.down()
                t.left(90)
                t.forward(25)
                t.right(90)
                t.forward(50)
                t.backward(50)
                t.left(90)
                t.backward(125)
                t.forward(90)
                t.left(60)
                t.forward(25)
                t.right(130)
                t.forward(25)
                t.backward(25)
                t.left(160)
                t.forward(50)
                t.right(90)
                t.forward(25)
                t.backward(25)
                t.left(90)
                t.forward(25)
                t.right(90)
                t.forward(25)
                t.right(90)
                t.forward(25)
                t.right(90)
                t.forward(25)
                t.left(45)
                t.forward(25)
                
                
                print ("You reach a large hole, what do you do?")
                print ("A) Jump")
                print ("B) Go around")

                choice8 = input()

                if choice8 == "A":
                    t.reset()
                    t.speed(0)
                    t.up()
                    t.backward(50)
                    t.down()
                    t.backward(75)
                    t.forward(75)
                    t.right(90)
                    t.forward(50)
                    t.backward(50)
                    t.up()
                    t.left(90)
                    t.forward(25)
                    t.down()
                    t.left(45)
                    t.forward(25)
                    t.right(90)
                    t.forward(25)
                    t.backward(25)
                    t.left(135)
                    t.forward(50)
                    t.right(90)
                    t.forward(25)
                    t.backward(50)
                    t.forward(25)
                    t.left(90)
                    t.forward(10)
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

                    t.reset()
                    t.forward(200)
                    t.backward(400)
                    t.forward(350)
                    t.left(90)
                    t.left(45)
                    t.forward(25)
                    t.right(90)
                    t.forward(25)
                    t.backward(25)
                    t.left(135)
                    t.forward(50)
                    t.right(90)
                    t.forward(25)
                    t.backward(50)
                    t.forward(25)
                    t.left(90)
                    t.forward(10)
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
                    
                    print ("You miss by a mile and break your right leg. What do you do?")
                    print ("A) wait")
                    print ("B) Scream")
                    print ("C) Try to get out")

                    choice10 = input()

                    if choice10 == "A":
                        print ("You get an idea. What is it?")
                        print ("A) Dig")
                        print ("B) Make fire")

                        choice12 = input()

                        if choice12 == "A":
                            print ("You start digging and find 3 thin objects and a match. One is an emergency flare, and the other two are sticks of TNT. Which do you lite?")
                            print ("A) Object 1")
                            print ("B) object 2")
                            print ("C) Object 3")
                
                            choice13 = input()

                            #Ends
                            if choice13 == "A":
                                print ("You lite TNT and blow up. The End.")
                                input()

                            elif choice13 == "B":
                                print ("You lite the emergency flare and 5 hours later people come and try to rescue you but somehow fail. What should you do?")
                                print ("A) Continue to beleive")
                                print ("B) Die")

                                choice16 = input()

                                #Ends
                                if choice16 == "A":
                                    print ("You die a beleiver")
                                    input()
                            
                                #Ends
                                elif choice16 == "B":
                                    print ("You die")
                                    input()

                            #Ends
                            elif choice13 == "C":
                                print ("You lite TNT and blow up. The End.")
                                input()
                        #Ends
                        elif choice12 == "B":
                            print ("You have nothing to make a fire out of, you perish. The End.")
                            input()
 
                    #Ends
                    elif choice10 == "B":
                            print ("You scream forever and die")
                            input()

                    #Ends
                    elif choice10 == "C":
                            print ("You can't get out and die... yeah sorry.")
                            input()

                elif choice8 == "B":
                    print ("You successfully bypass the hole... Now what?")
                    print
        
           #Ends   
            elif choice2 == "B":
                print ("You fall in a trap that was built 100,000 years ago. You slowly parish")
                input()
        
            elif choice2 == "C":
                print ("You get lost in a thicker part of the jungle, you start to panic.")
                print ("A) Stay")
                print ("B) Turn back")

                choice9 = input()

                #Ends
                if choice9 == "A":
                    print ("you stay, die and is never found")
                    input()

                #Ends
                elif choice9 == "B":
                    print ("You get lost again and die a lonely death")
                    input()

        if choice =="B":
            print ("How would you wait?")
            print ("A) Yell")
            print ("B) Make camp there")

            choice3 = input()

            #Ends
            if choice3 == "A":
                print ("No one hears you, you slowly DIE. The End")
                input()
        
            elif choice3 == "B":
                print ("You wonder where to make your camp.")
                print ("A) Climb a tree")
                print ("B) Try to make a fire")
                print ("C) Dig a hole")

                choice4 = input()
        
                if choice4 == "A":
                    print ("You climb half way up a tall tree, what do want to do?")
                    print ("A) Keep climbing")
                    print ("B) Start setting up camp")

                    choice7 = input()

                    if choice7 == "A":
                        print ("You reach the top and you see a stream of smoke in the distance. What do you do?")
                        print ("A) Follow")
                        print ("B) Make camp")

                    #Ends   
                    elif choice7 == "B":
                        print ("You slip and fall from the tree and break your ribs...AKA you die.")
                        input()
            
            elif choice4 == "B":
                print ("What should you do?")
                print ("A) Make fire with what you have")
                print ("B) Find wood")

                choice6 = input()

                if choice6 == "A":
                    print ("You successfully make a fire, but you see a storm coming, what should you do?")
                    print ("A) Try to create a roof over yourself and fire")
                    print ("B) Find shelter")

                elif choice6 == "B":
                    print ("By the time you get back it starts to rain, now what?")
                    print ("A) Give up")
                    print ("B) Try to sleep")

            elif choice4 == "C":
                print ("Ummmm... ok now what?")
                print ("A) Continue to dig")
                print ("B) Stop digging")
                print ("C) Do nothing")

                choice5 = input()

                if choice5 == "A":
                    print ("You fall into a deep cave system, now what?")
                    print ("A) Explore")
                    print ("B) Curl up into a ball and cry")

                    choice11 = input()

                    if choice11 == "A":
                        print ("You stumble around in the dark and come across an old skeleton and feel two things that could be sourses of light and a match around it.")
                        print ("Which do you lite?")
                        print ("A) Thin and tall item")
                        print ("B) wide and short item")

                        choice14 = input()

                        if choice14 == "A":
                            print ("You try to light a stick and fail. Now what.")
                            print ("A) Give up and die")
                            print ("B) Sleep and die")
                            print ("C) Join the skeleton")

                            choice15 = input()
                        
                            #Ends
                            if choice15 == "A":
                                print ("YOU...ARE...DEAD!")
                                input()
                            
                            #Ends
                            if choice15 == "B":
                                print ("YOU...ARE...DEAD!")
                                input()

                            #Ends
                            if choice15 == "C":
                                print ("YOU...ARE...DEAD!")
                                input()
                            
                        #To Be Continued
                        elif choice14 == "B":
                            print ("You lite a lantern and can now explore more.\n")
                            print ("To Be Continued...")
                            input()
                        
                    #Ends
                    elif choice11 == "B":
                        print ("Ok... you die... quitter.")
                        input()
                
                #Ends
                elif choice5 == "B":
                    print ("OK. %s dies. With luck someone will find your remains in a few million years" %(name))
                    input()
                
                #Ends
                elif choice5 == "C":
                    print ("('Speaking in a Russin accent')You are dead... no big surprise.")
                    input()
        
        response = "The End"

    #Calculator
    if command.find(COMMAND105) >= 0:
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return x / y

        print ("Select operation.")
        print ("1.Add")
        print ("2.Subtract")
        print ("3.Multiply")
        print ("4.Divide\n")

        choice = input("Enter choice(1/2/3/4):")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print ("\n")

        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))

        else:
            print("Invalid input")

        response = "Done\n"

    return response

while True:
    command = input('Input:')
    response = handle_command(command)
    print(response)
    print

#Awesome End... Wait,... It Never Ends.













        
