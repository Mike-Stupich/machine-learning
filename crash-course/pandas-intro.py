# Intro from here
# https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=en#scrollTo=U5ouUp1cU6pC

from __future__ import print_function
import pandas as pd
import numpy as np


pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({'City name': city_names, 'Population': population})

cities = pd.DataFrame({'City name': city_names, 'Population': population})

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / \
    cities['Area square miles']
# print(type(cities['City name']))
# print(cities['City name'])

# print(type(cities['City name'][1]))
# print(cities['City name'][1])

# print(type(cities[0:2]))
# print(cities[0:2])

# print(population/1000)
# print(np.log(population))

# print(population.apply(lambda val: val > 1000000))

# Exercise 1
# Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:

# The city is named after a saint.
# The city has an area greater than 50 square miles.

cities['Big Saint City'] = (cities['City name'].apply(lambda name: name.startswith('San'))) & (
    cities['Area square miles'] > 50)

# print(cities)

# print(cities.reindex([2, 0, 1]))
# print(cities.reindex(np.random.permutation(cities.index))) # np.random.permutation can be used to shuffle dataframes so that training data isn't in order i.e. better training

# Exercise 2
# The reindex method allows index values that are not in the original DataFrame's index values. Try it and see what happens if you use such values! Why do you think this is allowed?

print(cities.reindex([2, 0, 1, 3, 4]))

# Reasoning: allows parital datasets to be pulled from a source without need for sanitizing the input
