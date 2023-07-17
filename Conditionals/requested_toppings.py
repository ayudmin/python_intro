requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

##################

requested__toppings = []

if requested__toppings:
    for requested__topping in requested__toppings:
        print(f"Adding {requested__topping}.")
else:
    print('Are you sure you want a plain pizza?')

##################
print('\n')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested___toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested___topping in requested___toppings:
    if requested___topping in available_toppings:
        print(f"Adding {requested___topping}.")
    else:
        print(f"Sorry we don't have {requested___topping}.")
print('\nFinished making your pizza.')
