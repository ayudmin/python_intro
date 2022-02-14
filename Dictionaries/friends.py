favourite_language = {
    'phil': 'java',
    'sarah': 'c',
    'john' : 'c'
}
friends = ['phil', 'sarah']
for name in favourite_language.keys():
    pass
    # print(name.title())
    if name in friends:
        pass
        # print("Hi " + name.title() + " I see your favourite language is " + favourite_language[name].title())
if 'erin' not in favourite_language.keys():
    pass
    # print('Please Erin take our poll.')

for language in set(favourite_language.values()):
    print(language.title())