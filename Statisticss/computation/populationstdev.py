import statistics

def stdev(list):
    try:
        c = statistics.pstdev(list, mu = None)
        return c
    except statistics.StatisticsError as e:
        print("  Median Error --> ", e)