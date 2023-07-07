""" Using Variables in Strings """

first_name = 'Ada'

last_name = 'Lovalace'

""" using f strings """

full_name = f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.lower()}!")

my_greeting = f"Hello, {full_name.upper()}!"

print(my_greeting)


""" using format """

my_full_name = "{} {}".format(first_name, last_name)

print(my_full_name)