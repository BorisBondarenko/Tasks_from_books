def describe_city(city, country):
    return f'{city.title()}, {country.title()}'

print(describe_city('Los Angeles', 'USA'))
print(describe_city('Kyiv', 'Ukraine'))
print(describe_city('Moscow', 'Russia'))
