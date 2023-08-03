cities = {
    'juba': {
        'country': 'South Sudan',
        'continent': 'Africa'
    },
    'kampala': {
        'country': 'Uganda',
        'continent': 'Africa'
    }
}

for city, data in cities.items():
    print(city)
    print(data['country'])