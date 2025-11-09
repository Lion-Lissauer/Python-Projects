from xxsubtype import bench

naam = input("Hoe heet je? ")
leeftijd = int(input("Hoe oud ben je? "))
werk = input("Wat is je beroep? ")
ervaring_werk = int(input("Hoe lang doe je dit werk al? "))
drank = input("Wat is je favoriete drank? ")
jaren = leeftijd - ervaring_werk

print('')
print(f"Mijn naan is {naam}, ik ben {leeftijd} jaar oud. \nIk werk sinds m'n {jaren}e als {werk} en ik snak naar een {drank}.")