## Problem 3.10a
def middle_list(ls):
    return ls[1:-1]

## Problem 3.10b
def is_sum_greater(ls, n):
    return sum(ls) > n
    
## Problem 3.11a
def is_index_valid(ls, index):
    max_pos_index = len(ls) - 1
    max_neg_index = -len(ls)
    if index < 0:
        return index >= max_neg_index
    else:
        return index <= max_pos_index
## Problem 3.11a
## Alternative code that works, but is not what the problem wants
def is_index_valid(ls, index):
    try:
        ls[index]
        return True

    except IndexError:
        return False


## Problem 3.11b
def swap_elements(ls, index1, index2):
    if not is_index_valid(ls, index1):
        return None

    if not is_index_valid(ls, index2):
        return None

    newls = ls[:]
    newls[index1], newls[index2] = newls[index2], newls[index1]
    return newls

## Problem 3.12
def median(ls):
    ls.sort()
    n = len(ls)//2
    if len(ls)%2:
        return ls[n]

    else:
        total = ls[n] + ls[n - 1]
        return total/2
    

## Problem 3.13
def sum_odd_numbers(ls):
    total = 0
    for i in ls:
        if i%2 and i > 0:
            total += i

    return total

## Problem 3.14
def hailstone(n):
    sequence = [n]
    while n > 1:
        if n%2:
            n = 3*n + 1

        else:
            n = n/2
        
        sequence += [int(n)]

    return sequence


## Problem 3.15:
def get_odd_numbers(ls):
    odd = []
    for i in ls:
        if i%2:
            odd += [i]
    
    odd.sort()
    return odd


## Problem 3.16
def moving_average(ls):
    ma = []
    for i in range(0, len(ls) - 2):
        total = sum(ls[i:i+3])
        ma += [round(total/3, 1)]

    return ma

## Problem 3.17
def trapezoidal_rule(f, dx):
    if len(f) <= 1:
        return 0
    return 0.5*dx*(2*sum(f[1:-1]) + f[0] + f[-1])


## Problem 3.18
def left_riemann_sum(x, y):
    if len(x) <= 1 or len(y) <= 1:
        return 0
    
    total = 0
    for i in range(len(x) - 1):
        total += (x[i + 1] - x[i])*y[i]

    return total

