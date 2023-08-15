def make_car(manufacturer, model_name, **car):
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)