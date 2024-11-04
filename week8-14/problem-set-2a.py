## Problem 2.01
def calculate_bmi(weight, height):
    height = height/100
    bmi = weight/(height**2)
    return round(bmi, 1)


##Problem 2.02
def position_velocity(vo, t):
    g = 9.81
    velocity = round(vo - g*t, 3)
    position = round(vo*t - 0.5*g*(t**2),3)
    return (position, velocity)


## Problem 2.03
import math

def decay(a,t):
    cosine = math.cos(a*t)
    x = cosine*((math.e)**(-a*t))
    return x


## Problem 2.04
def describe_bmi(bmi):
    if bmi >= 27.5:
        return 'high risk'

    elif bmi >= 23:
        return 'moderate risk'

    elif bmi >= 18.5:
        return 'low risk'

    else:
        return 'nutritional deficiency'


## Problem 2.05
def is_positive_even(n):
    return (n%2 == 0) and (n > 0)


## Problem 2.06
def letter_grade(mark):
    if mark > 100 or mark < 0:
        return None
    
    elif mark >= 90:
        return 'A'

    elif mark >= 80:
        return 'B'

    elif mark >= 70:
        return 'C'

    elif mark >= 60:
        return 'D'

    else:
        return 'E'


## Problem 2.07
def largest_area(s, u, v):
    ## s: length of side of paper
    ## u: determines horizontal length
    if s < 0 or u < 0 or v < 0 or s < u or s < v:
        ## check if s, u or v is negative
        ## then check if u or v is > s
        return None

    else:
        if u < s/2:
            width = s - u

        else:
            width = u

        if v < s/2:
            breadth = s - v

        else:
            breadth = v

        return breadth*width
