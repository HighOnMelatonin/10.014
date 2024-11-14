## Problem 5.10
def search(ls, value):
    for i in range(len(ls)):
        if ls[i] == value:
            return i

## Problem 5.11
def increase_value(dd, k):
    if k in dd.keys():
        dd[k] += 1


## Problem 5.12a
def translate_point(dd, key, vector):
    if key in dd.keys():
        coord = dd[key]
        coord = (coord[0] + vector[0], coord[1] + vector[1])
        dd[key] = coord

## Problem 5.12b
def translate_point_new(dd, key, vector):
    dd_out = dd.copy()
    if key in dd_out.keys():
        translate_point(dd_out, key, vector)

    return dd_out

## Problem 5.13a
def replace_values(ls, value1, value2):
    count = ls.count(value1)
    for i in range(count):
        ls[ls.index(value1)] = value2


## Problem 5.13b
def replace_values_new(ls, value1, value2):
    ls_new = ls.copy()
    replace_values(ls_new, value1, value2)
    return ls_new

## Problem 5.14
def equation_of_line(point1, point2):
    a = point2[0] - point1[0]
    b = point1[1] - point2[1]
    c = point1[0]*b - point1[1]*a
    return (a, b, c)

def reflect(point, eqn):
    a = eqn[0]
    b = eqn[1]
    c = eqn[2]
    p = point[0]
    q = point[1]
    pnume = p*(a**2 - b**2) - 2*b*(a*q + c)
    pdeno = (a)**2 + (b)**2
    newp = pnume/pdeno

    qnume = q*(b**2 - a**2) - 2*a*(b*p + c)
    qdeno = (a)**2 + (b)**2
    newq = qnume/qdeno

    return (newp, newq)

def reflect_triangle(dd, point):
    keys = list(dd.keys())
    keys.pop(keys.index(point))
    dd_new = dd.copy()
    eqn = equation_of_line(dd_new[keys[0]], dd_new[keys[1]])
    newPoint = reflect(dd_new[point], eqn)
    dd_new[point] = newPoint
    
    return dd_new



