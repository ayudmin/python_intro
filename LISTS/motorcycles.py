motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('gnl')
motorcycles.append('bajaj')

motorcycles.insert(0, 'ducati')
motorcycles.insert(1, 'senke')
motorcycles.insert(3, 'tvs')



print(motorcycles)

del motorcycles[0]
del motorcycles[-1]

poped_motorcycle = motorcycles.pop()
second_poped_motorcycle = motorcycles.pop()
motorcycles.remove('tvs')

print(poped_motorcycle)
print(motorcycles)

print('\n')

dinner_members = ['ayume', 'ayudmin', 'admin']

print(f"Your welcome for dinner mr {dinner_members[0]}.")
print(f"Your welcome for dinner mr {dinner_members[1]}.")
print(f"Your welcome for dinner mr {dinner_members[2]}.")

print('\n')
print(dinner_members)
not_coming = dinner_members.pop(1)
new_coming = dinner_members.insert(1, 'adme')
print('\n')

print(f"{not_coming} will not be coming so am inviting {dinner_members[1]}")
print('\n')

print(dinner_members)
print('\n')
print('Good news we added more')
dinner_members.insert(0, 'new_1')
dinner_members.insert(3, 'new_3')
dinner_members.append('new_last')
print('\n')

print(dinner_members)

poped_first = dinner_members.pop()
print(f"Removed {poped_first}")
poped_second = dinner_members.pop()
print(f"Removed {poped_second}")
poped_third = dinner_members.pop()
print(f"Removed {poped_third}")
poped_fourth = dinner_members.pop()
print(f"Removed {poped_fourth}")

print('\n')
print(dinner_members)

del dinner_members[0]
del dinner_members[0]

print('\n')
print(dinner_members)




