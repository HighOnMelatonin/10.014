##Problem 2.11
def compound_interest(amount, rate, periods, time):
    return round(amount*(1 + (rate/periods))**(periods*time),3)


## Problem 2.12
import math

def area_vol_cylinder(radius, length):
    area = (math.pi)*(radius**2)
    volume = area*length
    return round(area, 2), round(volume, 2)


## Problem 2.13
def seconds_to_hours(seconds):
    totalMinutes = seconds//60
    hours = totalMinutes//60
    minutes = totalMinutes%60
    sec = seconds%60

    return (hours, minutes, sec)


## Problem 2.14
def fahrenheit_to_celcius(f):
    ABSOLUTE_ZERO = -273.15
    c = (f - 32) /(9/5)
    if c < ABSOLUTE_ZERO:
        return None

    else:
        return round(c, 2)


## Problem 2.15
def sequence(n):
    if n < -0.5 and n >= -3:
        return None

    else:
        num = 2*n + 1
        deno = n + 3
        return round((num/deno)**0.5, 4)

## Problem 2.16
def check_value(n1, n2, n3, x):
    if x > n1 and x > n2:
        if x < n3:
            return True

    return False

