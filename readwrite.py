# file = open('text.txt','r')

# read_data = file.read()
# print(read_data)

# file.close()

with open('text.txt','r') as file:
    read_data = file.read()

    print(read_data)

file.close()