def build_profile(name, surname, age, national, profession, **kwargs):
    kwargs['name'] = name
    kwargs['surname'] = surname
    kwargs['age'] = age
    kwargs['national'] = national
    kwargs['profession'] = profession
    return kwargs


print(build_profile('Boris', 'Bondarenko', '29', 'Ukraine', 'Entrepreneur'))


# short version
def build_profile(**kwargs):
    return kwargs


print(build_profile(name='Boris', surname='Bondarenko', age='29', national='Ukraine', profession='Entrepreneur'))
