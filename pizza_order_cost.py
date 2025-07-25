#!/usr/bin/python3

# pseudocode
'''
This script takes in three user inputs
- pizza size : (small / large) string
- number of toppings : integer
- delivery distance (in miles) :integer

Then calculate...
- the base cost of the pizza using conditional statements
- the cost of toppings
- the delivery fee

Sum up the total cost
Display the result using an f-string
'''

# pizza size input and validation loop
while True:
    pizza_size = str(input("Which size pizza would you like (small / large)?:").lower())
    # small pizza = $8; large pizza = $12
    if pizza_size == "small":
        pizza_cost = int(8)
        break
    elif pizza_size == "large":
        pizza_cost = int(12)
        break
    # break loop & return to let the user retry input if invalid
    else:
        print("Please choose either 'small' or 'large'")

# toppings count input
toppings_count = int(input("How many toppings would you like?:"))
# toppings = $1 per topping
toppings_cost = 1 * toppings_count

# delivery distance input
delivery_distance = int(input("How far away is the destination (in miles)?:"))
# $2 for first 5 miles; $1 for each additional mile
if delivery_distance == 0:
    delivery_fee = int(0)
elif delivery_distance <= 5:
    delivery_fee = int(2)
elif delivery_distance:
    # base cost of 2 for 5 or more miles + (total distance - 5) to account for base cost 
    # and add the rest at the additional mile rate
    delivery_fee = int(2 + (delivery_distance - 5))

# total cost
total_cost = pizza_cost + toppings_cost + delivery_fee

# itemized receipt
print(f"\nYour order summary:")
print(f"- One {pizza_size} pizza: ${pizza_cost}")
print(f"- {toppings_count} topping(s): ${toppings_cost}")
print(f"- Delivery fee ({delivery_distance} miles): ${delivery_fee}")
print(f"TOTAL COST: ${total_cost}")

# sentence receipt
print()
print()
print(f"The total cost for your order for a {pizza_size} pizza with {toppings_count} toppings and a delivery distance of {delivery_distance} miles comes out to ${total_cost}.")