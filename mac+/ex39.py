states = {
    'Oregon': 'Or',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    "Michigan": 'MI'
}


cities = {
    'CA': 'San Francisxo',
    'NI': 'Detroit',
    "FL": 'Jaxksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('_' * 10)
print("NY States has: ", cities['NY'])
print("OR States has: ", cities['OR'])


print('_' * 10)
print("Michigan's has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


print('_' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida's has: ", cities[states['Florida']])

print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
    
print('_' * 10)
for abbrev, city in list(states.item()):
    print(f"{abbrev} has the city {city}")
    
    
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} states is abberviated {abbrev}")


if not state:
    print("Sorry, no Texas.")
    
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
