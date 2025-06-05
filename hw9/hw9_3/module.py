def is_prime(num:int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True

def get_primes(last_num: int):
    prime_list = []
    for i in range(2, last_num + 1):
        is_prime = True
        for x in range(2, int(i**0.5) + 1):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list