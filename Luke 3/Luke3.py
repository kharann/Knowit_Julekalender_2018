def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,num):
            if num % div == 0:
                return False
        return True
primes = [num for num in range(2,512) if is_prime(num)]
def increment(indexes, pos, end):
    print(indexes)

lol = [1,2,3,4,5,6,7]
sum = 1
for i in lol:
    sum *= i
print(sum)