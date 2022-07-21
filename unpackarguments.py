print(list(range(3,6)))

arg_list =[3,6]

print(list(range(*arg_list)))


def test_func(first,second):
    return first+','+second+'!'

arg_dic = {'first':'Hello', 'second': 'World'}

print(test_func(**arg_dic))