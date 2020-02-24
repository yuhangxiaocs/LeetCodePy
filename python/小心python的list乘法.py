'''

'''

res = [1] * 4
res[0] = 1
print(res)

s = ["d"] * 4

s[1] = "23"
print(s)


def f(x):
    x += 1


x = 5
f(x)
print(x)
'''
'''
some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print(some_guy, first_names, another_list_of_names)
