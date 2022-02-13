""" Basic Python Dictionaries """

alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2022
}


# print(thisdic['model'])

new_model = thisdic['model']
model_year = thisdic['year']
# print("You got the " + new_model + " model " + "in " + str(model_year))

thisdic['color'] = 'red'
thisdic['price'] = 6800

# print(thisdic)

campany = {}

campany['name'] = 'Eirmonshop'
campany['worth'] = 55000
campany['year_established'] = 2022
campany['owner'] = 'Ayume'

print(campany)
