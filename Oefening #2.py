#start
#kamer geel/rood/blauw
#vanuit kamer geel > groen/rood/
#vanuit kamer blauw > groen/rood
#rood = finish
#groen = dood!

print("Welcome to my lair. Choose your fate!\n")
option = input("Blue door, yellow door or the red door: ").lower()
while not(option == "blue" or option == "yellow" or option == "red"):
    option = input("blue, yellow or red: ").lower()

if option == "blue":
    print()
    print("Nothing to see here. Moving on!\n")
    option2 = input("Continue your path, the green door or the red door? ").lower()
    if option2 == "green":
        print()
        print("You just sealed your fate, you little maggot. You shall perish!!")
    elif option2 == "red":
        print("Mmm, next time you will be mine...")
    else:
        print("You're wasting my time. I hereby condemn you too the deepest pits of hell!")
elif option == "yellow":
    print()
    print("You just found some treasure. Not bad, maggot!\n")
    option2 = input("Continue your path, the green door or the red door? ").lower()
    if option2 == "green":
        print("You just sealed your fate, you little maggot. You shall perish!!")
    elif option2 == "red":
        print()
        print("Mmm, next time you will be mine...")
    else:
        print()
        print("You're wasting my time. I hereby condemn you too the deepest pits of hell!")

else:
    print()
    print("You're wasting my time. I hereby condemn you too the deepest pits of hell!")

#"Knock {x} times (gevolgd door while loop + counter)

# counter = 0
# while counter < 5:
#     print(counter)
#     counter+=1
#
# print("Stop!")

# Tomb of the pharao