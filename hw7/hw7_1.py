def generator_rev(iterable):
    for value in iterable[::-1]:
        yield value


mylist = [1, 4, 6, 1, 7, 78, 10, 8, 10]

for value in generator_rev(mylist):
    print(value)