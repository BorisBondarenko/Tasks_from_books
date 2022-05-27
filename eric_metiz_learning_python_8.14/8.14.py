def make_car(brand, model, **kwargs):
    kwargs['brand'] = brand
    kwargs['model'] = model
    return kwargs


print(make_car('BMW', 'Z4', engine='3.0', type_engine='patrol', color='grey'))
