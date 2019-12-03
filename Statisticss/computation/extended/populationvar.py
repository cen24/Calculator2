import statistics

def populationvar(list):
    c = statistics.pvariance(list, mu = None)
    return c
