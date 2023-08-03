favorite_languages = {
    'jen': 'Python',
    'ayume': 'Php',
    'ayudmin': 'Javascript',
    'francis': 'Sql'
}

friends = ['jen', 'ayudmin']

language = favorite_languages['ayume'].title()
language_1 = favorite_languages['francis'].title()

print(f" Ayume's favorite language is {language}")
print(f" Francis' favorite language is {language_1}")

print('\n')

for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}")

print('\n')

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language} ")