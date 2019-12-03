#Variance of population proportion = σP2 = PQ / n
from Statisticss.computation.populationstdev import stdev


def Variance_of_population_proportion(list):

    listx = []
    listy = []
    std = stdev(list)

    for row in range(0,len(list)):
        if list[row] <= std:
            listx.append(int(list[row]))
        else:
            listy.append(int(list[row]))


    p = (len(listx)*100/len(list))/100
    q = 1 - p


    c = (p*q)/len(list)
    return c