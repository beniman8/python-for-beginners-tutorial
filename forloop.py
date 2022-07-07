
# words=['house','cat','love']
# words_length=0

# for word in words:
#     words_length += len(word)


# print(words_length)

# for word in words[:]:
#     if len(word) < 4:
#         words.insert(0,word)

# print(words)


# itr_num=[]

# for num in range(10): 
#     itr_num.append(num)

# print(itr_num)


words = ['words','cars','loop']
cont = ''

# for word_indx in range(len(words)):
#     cont += words[word_indx] + ' '


# for word_indx, word in enumerate(words):
#     cont += word + ' '

# print(cont)

# villagers_name = [] 
# villagers_income = []

# villagers = {'jonny':'$1200','cindy':'$2390','robert':'$5643'}

# for key , value in villagers.items():
#     villagers_name.append(key)
#     villagers_income.append(value)

# print(f'The names of the villagers are : {villagers_name}')
# print(f'The income of the villagers are : {villagers_income}')


# indices = []
# values = []

# for index , value in enumerate(['hey','sup','ok']):
#     indices.append(index)
#     values.append(value)


# print(indices)
# print(values)


questions = ['name','age','favorite color']
answers = ['jonny','45','blue']

combinations = []

for question, answer in zip(questions, answers):
    combinations.append(f'What is your {question} : it is {answer}')

print(combinations)