" nesting dictionary inside dictionary "

users = {
    'ocnarf': {
        'first_name': 'ayume',
        'last_name': 'francis',
        'location': 'juba'
    },
    'mehra': {
        'first_name': 'vikram',
        'last_name': 'developer',
        'location': 'mumbai'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
print(users)