
# def greet(name):

#     return f"Hello, {name}!"

# # print(greet('jhon cena'))


def decor_with_happy(func):

    def func_happy(name):
        return f"{func(name)} are you happy today ?"

    return func_happy

# my_text = decor_with_happy(greet)

# print(greet('jonny'))
# print(my_text('jhon cena'))
@decor_with_happy
def greet(name):
    return f"{name}!"

print(greet('david'))
