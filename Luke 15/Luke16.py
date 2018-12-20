import timeit
start = timeit.default_timer()
with open("input-palindrom.txt","r") as f:
    numbers = list(map(lambda x: int(x),f.read().split(",")))

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_palindrome(input):
    palindrome_sums = []
    for i in range(1,len(numbers)-1):
        y = 1
        while numbers[i-y] == numbers[i+y]:
            try:
                palindrome = numbers[i-y:i+y+1]
                if is_prime(sum(palindrome)) and sum(palindrome) not in palindrome_sums:
                    palindrome_sums.append(sum(numbers[i-y:i+y+1]))
            except IndexError:
                break 
            if not i+y == len(numbers)-1:
                y += 1
            else:
                break
    return max(palindrome_sums)
print(find_palindrome(numbers))
end = timeit.default_timer()
print(end-start)