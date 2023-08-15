def get_formated_user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print('Please tell me your name.')
    print('Press q to quite anytime.')
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break
    print(f"Hello, {get_formated_user(f_name, l_name)}")
