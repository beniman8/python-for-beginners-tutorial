
# def poem(name, state="being", action="run"):

#     message = f"{name} could of {state} but instead he decided to {action}"

#     return message

# print(poem("the rock"))


def poem_two(first_param,*arguments,**keywords):

    print(first_param)
    print(arguments)
    print(keywords)


poem_two("one","two","three","Five",cars="bently")