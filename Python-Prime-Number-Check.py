## Python Program to check for Prime Numbers by Nilesh

import math

def is_prime(n):
    if n <= 1:
        return "Sorry Enter a valid number!"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Sorry, It's not a Prime Number!"
    return "It's a Prime Number!"

n = int(input("\nEnter a Number to check whether its prime or not: "))
print(is_prime(n))