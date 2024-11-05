## Problem 3.00a
def calculate_sum_odd(n):
    total = 0
    for i in range(1,n,2):
        total += i

    return total


## Problem 3.00b
def alternating(n):
    total = 0
    for i in range(1, n + 1):
        total += ((-1)**(i+1))/i

    return total

## Problem 3.01a
def compound_interest(principal, rate, months):
    amount = 0
    monthlyRate = rate/12
    for i in range(months):
        amount += amount*monthlyRate
    return round(amount, 2)

## Problem 3.01b
def regular_savings(deposit, rate, months):
    amount = 0
    monthlyRate = rate/12
    for i in range(months):
        amount = (amount + deposit)*(1 + monthlyRate)

    return round(amount,2)

## Problem 3.02
def sum_of_series(n):
    amount = 0
    for i in range(1, n + 1):
        amount += 1/(i**2)

    return round(amount, 2)


## Problem 3.03
def is_prime(n):
    if n < 2:
        return None
    else:
        for i in range(2, n - 1):
            if n%i == 0:
                return False

        return True

## Problem 3.04
def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i

    return result

def binomial_coefficient(n, k):
    nume = factorial(n)
    deno = (factorial(k)*factorial(n - k))

    return int(nume/deno)


## Problem 3.05a
def calculate_sum_even(n):
    total = 0
    i = 0
    while i < n:
        total += i
        i += 2

    return total

## Problem 3.05b
def alternating_while(stop):
    total = 0
    frac = 1
    n = 1
    while abs(frac) > stop:
        total += frac
        n += 1
        frac = ((-1)**(n + 1))/n

    return total


## Problem 3.06
import math

def sum_of_series(n):
    amount = 0
    for i in range(n):
        amount += i/(i**2)

    return amount

def fraction_of_pisq(s):
    return (s/((math.pi)**2)/6)

def terms_required(p):
    count = 0
    result = 0
    while result < p:
        count += 1
        amount = sum_of_series(count)
        result = fraction_ofpisq(amount)

    return count

