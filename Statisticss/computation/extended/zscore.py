from Statisticss.computation.populationmean import mean
from Statisticss.computation.populationstdev import stdev




def zscore(z, list):
    c = (z * stdev(list)) + mean(list)
    return c



# z = (X - μ) / σ
#where z is the z-score, X is the value of the element,
#μ is the mean of the population,
#and σ is the standard deviation. ( Z  and List wouold be a pulled from CSV)


