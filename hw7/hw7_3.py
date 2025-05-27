def generator(num:int):
    start_num = 1
    while start_num <= num:
        yield start_num
        start_num += 1

for num in generator(123):
    print(num)