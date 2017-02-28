#Introduction
def Person():
    print ("Wow, you input the correct answer! You have survived! YOU... ARE... THE... BEST!")
    input()

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
    print ("You start walking and come to a fork in the path. Which way do you go?")
    print ("A) go right")
    print ("B) Go Strait")
    print ("C) Go left")

    choice2 = input()

    if choice2 == "A":
        print ("You reach a large hole, what do you do?")
        print ("A) Jump")
        print ("B) Go around")

        choice8 = input()

        if choice8 == "A":
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
                print ("(Speaking in a Russin accent)You are dead... no big surprise.")
                input()









        














               
    













    
    
