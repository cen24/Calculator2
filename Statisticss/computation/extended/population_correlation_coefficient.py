from Statisticss.computation.populationstdev import stdev
from Statisticss.computation.populationmean import mean

def cov(a, b):

    if len(a) != len(b):
        return

    a_mean = mean(a)
    b_mean = mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)

def population_correlation_coefficient(a,b):

    x = cov(a,b)
    y = stdev(a) * stdev(b)
    c = x/y
    return c