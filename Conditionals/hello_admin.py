server_users = []

if server_users:
    for server_user in server_users:
        if server_user == 'admin':
            print(f"Hello {server_user}, would you like to see some status report?")
        else:
            print(f"Hello {server_user}, thank you for logging in again")
else:
    print('We need to find some users.')


current_users = ['ayume', 'john', 'peter', 'mary']

new_users = ['AYUME', 'Mary', 'boy']

for user in new_users:
    if user.lower() in current_users:
        print('username already exists')
    else:
        print(f"{user}, is available.")


numbers_list = [1,2,3,4,5,6,7,8,9]

for num in numbers_list:
    if num == 1:
        print(f"\n{num}st")
    elif num == 2:
        print(f"\n{num}nd")
    elif num == 3:
        print(f"\n{num}rd")
    else:
        print(f"\n{num}th")