## Problem 5.00
def make_string(dd):
    return "{0} - {1}".format(dd['title'], dd['genre'])

## Problem 5.01
def get_value(dd, k):
    if k in dd.keys():
        return dd[k]

## Problem 5.02
def extract_data(dd, k):
    if k in dd.keys():
        distance = (abs(dd[k][0])**2)+(abs(dd[k][1])**2)
        return round(distance**0.5, 2)

## Problem 5.03
def create_dictionary(fruits, prices):
    if len(fruits) != len(prices):
        return None

    dd = {}
    for i in range(len(fruits)):
        dd[fruits[i]] = prices[i]

    return dd

## Problem 5.04
def get_base_counts(dna):
    dd = {'A':0,'C':0,'G':0,'T':0}
    for char in dna:
        if not char in dd.keys():
            return "The input DNA string is invalid"
        else:
            dd[char] += 1

    return dd

## Problem 5.05
def evaluate_polynomial(dd, x):
    result = 0
    for key in dd.keys():
        result += (x**key)*dd[key]

    return round(result, 2)

## Problem 5.06
def diff(pp):
    dp = {}
    for key in pp.keys():
        if key == 0:
            continue
        else:
            dp[key - 1] = key*pp[key]

    return dp

## Problem 5.07
def read_list(ls, reg_no, key):
    for car in ls:
        if car['reg'] == reg_no:
            try:
                return car[key]
            except:
                return None


## Problem 5.08
def get_highest_value(dd):
    highest = 0
    highkey = ''
    for key in dd:
        if dd[key] > highest:
            highkey = key
            highest = highkey
    
    return (highkey, highest)



