toppings = ['tomaat', 'kaas', 'tonijn', 'kappertjes', 'oregano']
print(f"De eerste topping op mijn pizza is {toppings[0]}.")
print(f"De derde topping op mijn pizza is {toppings[2]}.")
print(f"De laatste topping op mijn pizza is {toppings[-1]}.")
print(f"Mijn pizza bevat de volgende toppings: {', '.join(toppings)}.")
extra_topping = input("\nWelke toppings wil je d'r nog bij? ").lower()
toppings.append(extra_topping)
print(f"Mijn extra topping is {extra_topping}.")
print(f"Mijn pizza bevat nu de volgende toppings: {', '.join(toppings)}.")
remove_topping = input("\nWelke topping uit deze lijst vind je niet lekker? ")
if remove_topping in toppings:
    toppings.remove(remove_topping)
    print(f"{remove_topping} is nu uit de lijst gehaald. De overgebleven toppings zijn {', '.join(toppings)}.")
else:
    print(f"Deze lijst bevat geen {remove_topping}. De overgebleven toppings zijn {', '.join(toppings)}.")
