
number = int(input('Please enter a number to test the program : '))

result=''

if number < 0:
    result='The number is less than zero'
elif number == 0:
    result='the number is equal to zero'
elif number < 1:
    result= ' The number is greater than zero but less than one'
else:
    result = 'The Number is bigger than or equal to one'

print(result)