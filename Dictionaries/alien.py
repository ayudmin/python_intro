alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)
print(f"The alien is {alien_1['color']}")
alien_1['color'] = 'yellow'
print(f"The alien is {alien_1['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': ''}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Final position: {alien_0['x_position']}")
