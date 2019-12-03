from Statisticss.computation.populationmean import mean
from Statisticss.computation.populationstdev import stdev
from Calculator.computation.squareroot import sqrt


def cintreval(list):
    try:
        mean_var = mean(list)
        cin = 0.95
        value_of_z = (1-cin) / 2
        stdev_var = stdev(list)
        n = sqrt(len(list))
        result = [mean_var - value_of_z*stdev_var / n, mean_var + value_of_z*stdev_var / n]
        return result
    except Exception as e:
        print("Error with Cintreval")
        return [0,0]




