def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    sumTotal = 0
    point = start

    while start <= point < stop:
        sumSub = step * f(point)
        sumTotal += sumSub
        point += step

    return sumTotal

print radiationExposure(0, 5, 1)
