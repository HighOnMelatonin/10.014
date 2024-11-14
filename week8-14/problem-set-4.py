## Problem 4.00
def calculate_bmi (weight, height):
    height = height/100
    bmi = weight/(height**2)
    return round(bmi, 1)

def describe_bmi(bmi):
    if bmi >= 27.5:
        return 'high risk'

    elif bmi >= 23:
        return 'moderate risk'

    elif bmi >= 18.5:
        return 'low risk'

    else:
        return 'nutritional deficiency'

def bmi_information(weight, height):
    bmi = calculate_bmi(weight, height)
    description = describe_bmi(bmi)
    info = "Your BMI is {0} and your category is {1}.".format(bmi, description)
    return info


## Problem 4.01a
def reverse(s):
    return s[-1:0:-1] + s[0]

## Problem 4.01b
def make_name(first, last):
    return str(first.title() + ' ' + last.upper())

## Problem 4.02
def is_palindrome(s):
    mid = len(s)//2
    if len(s)%2 == 0:
        left = s[:mid]
        right = s[-1:mid - 1:-1]
        return left == right

    else:
        left = s[:mid]
        right = s[-1:mid:-1]
        return left == right

## Problem 4.03
def match(a, b):
    index = len(a)
    end = b[-index:]
    return end == a

## Problem 4.04
def clean_string(s):
    out = ""
    for char in s:
        if char.isalnum():
            out += char

        elif ord(char) == 32:
            out += char

        elif char.isdigit():
            out += char

        else:
            pass

    return out

## Problem 4.05
def digits_in_string(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1

    return count

def check_password(pwd):
    if len(pwd) < 8:
        return False
    
    elif digits_in_string(pwd) < 2:
        return False

    elif not pwd.isalnum():
        return False

    else:
        return True

## Problem 4.06
def longest_common_prefix(s1, s2):
    length1 = len(s1)
    length2 = len(s2)
    if length1 > length2:
        length = length2

    else:
        length = length1

    pref = ''
    for i in range(length):
        if s1[i] == s2[i]:
            pref += s1[i]

        else:
            break

    return pref


## Problem 4.07
def binary_to_decimal(s):
    den = 0
    n = len(s)
    for i in range(n):
        den += int(2)**(n - (i+1))

    return den


## Problem 4.08
def uncompressed(s):
    out = ""
    for char in s:
        if char.isdigit():
            multiplier = int(char)

        else:
            out += char*multiplier

    return out


## Problem 4.09
def get_base_counts(dna):
    total = len(dna)
    a = dna.count('A')
    c = dna.count('C')
    t = dna.count('T')
    g = dna.count('G')
    if total > (a + c + t + g):
        return []

    else:
        return [a,c,g,t]

