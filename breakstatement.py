number_to_find = 34

number_iteration=0


for number in range(50):
    if number == number_to_find:
        break

    else:
        number_iteration +=1


print(number_iteration)