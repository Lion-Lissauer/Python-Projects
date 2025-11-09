# x = int(input("waarde: "))
# if x % 5 == 0:
#     print(f"{x} is deelbaar door 5")
#     if x == 10:
#         print("getal is tien")
#
# else:
#     print("Plop!")


x = -5
if x % 2 == 0:
    print(f"{x} is an even number")

elif x % 2 == 1:
    print(f"{x} is an odd number")

# else:
#     print(f"{x} is a float")

age = int(input("Je leeftijd: "))

if age < 12:
    korting = 50

# from random import randint
#
# weekdag = randint (a:1, b:7)
#
# match weekdag:
#     case 1: print("Maandag")
#     case 2: print("Dinsdag")

# keep_going = True
#
# while keep_going:
#     print("Keep goin'")
#     keep_going = False
#
# print("Stop")

counter = 0
while counter < 5:
    print(counter)
    counter+=1

print("Stop!")