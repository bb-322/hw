def generator(iter):
    even_nums = []
    for num in iter:    
        if num % 2 == 0:
            even_nums.append(num)
    for item in even_nums:
        yield item ** 2


my_list = [10, 4, 100, 53, 11, 35, 49, 20]

for num in generator(my_list):
    print(num)

print('----------------------------------')

for num in my_list:
    if num % 2 == 0:
        print(num**2)