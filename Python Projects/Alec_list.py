

print("give a food item")
food = input()
foodp = float(input("enter food price: "))


print("give a drink item")
drink = input()
drinkp = float (input("enter drink price: "))

print ("give a dessert item")
dessert = input()
dessertp = float(input("enter food price: "))


my_grocery_list =[food, drink, dessert]
my_price_list =[foodp, drinkp, dessertp]


print("Would you like me to print your grocery list for you!")
answer1 = input()

if answer1 =='yes':

    print(my_grocery_list)

else:
    print("Okay!")

#print ("So tonight, I am going to eat %s, I am going to drink %s, and for desert I am going to have %s") %("food, drink, dessert")

print("should I add Total?")
answer2 = input()

if answer2 =='yes':
    print(foodp + drinkp + dessertp)

else:
    print("Okay!")

print("Would you like me to close this program?")
answer3 = input()

if answer3 =='yes':
    print("Ok... Bye")

else:
    print("ERROR...100010111101011010001011111101000101000101111010100110001010001011110101010010010111110101001010001010010001001000011111110111010000010101010010000101011110101111110000000000111101000101010001010101010001010")
    print("Input:")

    answer4 = input()

if answer4 =='101101001':
    print("Loading...")
    print("Enter: 1100100100011110")

else:
    print("ERROR...")
    
answer6 = input()

if answer6 =='1100100100011110':
    print("Closing...")

else:
    print("ERROR...")
    
    answer7 = input()

    if answer7 =='1100100100011110':
      print("Closing...")  
    
    else:
        for i in range(1000000000000000000000000000000000000000):
            print("ERROR...")
        
    

    

















