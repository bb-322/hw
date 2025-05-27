def generator(iter):
    even_nums = []
    for num in iter:    
        if num % 2 == 0:
            even_nums.append(num)
    for item in even_nums:
        yield item ** 2


my_list = [10, 4, 100, 53, 11, 35, 49, 20]

sqr_list_gen = []
for num in generator(my_list):
    sqr_list_gen.append(num)
print(sqr_list_gen)


sqr_list = []
for num in my_list:
    if num % 2 == 0:
        result = num ** 2
        sqr_list.append(result)
print(sqr_list)