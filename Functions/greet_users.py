def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['ayume', 'francis', 'ayudmin']
greet_users(usernames)