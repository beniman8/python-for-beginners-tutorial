even_num = []

rest_num = []


for number in range(0,10):

    if number % 2 ==0:
        even_num.append(number)

        continue



    rest_num.append(number)


print(f"all the even numbers are {even_num} , all the odd numbers are {rest_num}")