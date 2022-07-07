
from traceback import print_tb


car_sets = {"Nissan","Mercedes","BMW"}

# print(type(car_sets))


# print(len(car_sets))

car_sets.add("Audi")

# print(car_sets)

car_sets.remove("BMW")

# print(car_sets)

first_char_set = set('abracadabra')
second_char_cet = set('alacazam')

print(first_char_set ^ second_char_cet)

# print(second_char_cet)