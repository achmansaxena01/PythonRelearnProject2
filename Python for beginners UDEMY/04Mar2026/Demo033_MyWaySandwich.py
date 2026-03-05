#i have written in the below way. Please see the below if you are stuck at a place.

Toppings = {
    1: "onion",
    2: "lettuce",
    3: "tomato",
    4: "olives",
    5: "peppers",
}

print(Toppings)

item1_number = int(input("\nEnter the number of first topping which you want to select: "))
item1_name = Toppings.get(item1_number, "onion")
print(f"You have selected the topping {item1_name} .")
item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))

item2_number = int(input("\nEnter the number of second topping which you want to select: "))
item2_name = Toppings.get(item2_number, "lettuce")
print(f"You have selected the topping {item2_name} .")
item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))

item3_number = int(input("\nEnter the number of Third topping which you want to select: "))
item3_name = Toppings.get(item3_number, "tomato")
print(f"You have selected the topping {item3_name} .")
item3_quantity = int(input(f"Enter the quantity of {item3_name}: "))

item1_total = 5 * item1_quantity
item2_total = 5 * item2_quantity
item3_total = 5 * item3_quantity

total = item1_total + item2_total + item3_total

print("\n----------Receipt----------")
print(f"{item1_name.capitalize()} : {item1_quantity} @  $5 each = ${item1_total:.2f}")
print(f"{item2_name.capitalize()} : {item2_quantity} @  $5 each = ${item2_total:.2f}")
print(f"{item3_name.capitalize()} : {item3_quantity} @  $5 each = ${item3_total:.2f}")

print(f"Subtotal : ${total:.2f}")
