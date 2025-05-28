import random
with open('nums.txt', 'w') as f:
    f.write(f'{random.randint(1,10000)}')
    for i in range(9999):
        f.write(f'\n{random.randint(1,10000)}')

with open('nums.txt', 'r') as f:
    nums = f.read().split('\n')
    int_nums = []
    for num in nums:
        num = int(num)
        int_nums.append(num) 
    print(sum(int_nums))