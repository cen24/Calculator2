import statistics

def median(list):
    try:
        c = statistics.median(list)
        return c
    except statistics.StatisticsError as e:
        print("Median error: ", e)