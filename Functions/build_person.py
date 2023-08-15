def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

dic_item = build_person('ayume', 'francis', 23)

print(dic_item)