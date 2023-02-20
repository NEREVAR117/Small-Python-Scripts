print("This program returns the largest prime divisor of a number.")
number = input("Please input an integer. ")
def isprime(n, k):
    for primeIndex in range(2, int(k ** 0.5), 1):
        if n % primeIndex == 0 and n != primeIndex:
            value = 0
            break
        elif n % primeIndex == 0 and n == primeIndex:
            pass
        elif n % primeIndex == 0:
            value = 0
            break
        else:
            value = 1
            break
    if value == 0:
        return 0
    else:
        return 1
for divisor in range(1, int((number ** 0.5) * 4), 1):
    if number % divisor == 0:
        if isprime(divisor, number) == 1:
            prime = divisor
if prime == 1:
    prime = number
print("The largest prime is " + str(prime) + ".")