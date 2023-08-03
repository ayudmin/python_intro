rivers = {
    'nile': 'egypt',
    'missisippi': 'tanzania'
}

for key, value in rivers.items():
    print(f"The {key} flows through {value}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)