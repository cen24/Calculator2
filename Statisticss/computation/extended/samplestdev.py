from Statisticss.computation.populationstdev import stdev
from Statisticss.computation.sample import Sample

def samplestdev(list):
    s = 50
    r = Sample(list,s)
    c = stdev(r)
    return c