def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name('ayume', 'francis')
name_long = get_formatted_name('ayume', 'francis', 'joseph')

print(name)
print(name_long)