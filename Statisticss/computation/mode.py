import statistics

def mode(list):
    c = 0
    try:
        c = statistics.mode(list)
        return c
    except statistics.StatisticsError as e:
        print("  Mode Error --> ", e)
