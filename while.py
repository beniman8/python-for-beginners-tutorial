
# number = 3

# power = 5

# result = 1

# while power > 0:
#     result *= number
#     power -= 1

# print(result)

number = int(input("Enter a number: "))

count = 1

while count <= 10:
    product = number * count
    print(number, "x", count , "=", product)
    count = count + 1

    