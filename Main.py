#print("plop!")
#print("")
#user_input = input("Hoe heet je? ")
#print("Ik heet " + user_input)
#print(f"Ik heet {user_input}")
#my_string = "7!"
#print(type(my_string))

#x = 5
#x =+ 2
#print(x)
#x *= 2
#print(x)
#x %= 3
#print(x)

nummers = [2, 5, 7, 11, 13, 15]
lijst_element = nummers[0]
print(nummers)
print(type(nummers))
print(lijst_element)
print(nummers[-2])
print('7', 7 in nummers)
print('8', 8 not in nummers)
print(nummers.index(13))
print('het aantal elementen is', len(nummers))

nummers = [2, 5, 7, 11, 13, 15]
som = 0

for getal in nummers:
    som += getal

print("De som van de lijst is", som)