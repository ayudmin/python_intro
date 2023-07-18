for value in range(1, 5):
    print(f"{value}\n")

numbers = list(range(1, 6))

print(numbers)

even_numbers = list(range(2, 11, 2))

print(even_numbers)

squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


players = ['charles', 'martina', 'micheal', 'florina', 'eli']

print('Here are the first 3 players in my team:')
for player in players[:3]:
    print(player.title())