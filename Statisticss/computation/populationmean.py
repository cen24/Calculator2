from Calculator.computation.addition import add
from Calculator.computation.division import div



def mean(list):
    try:
        n = len(list)
        total = 0
        for var in range(0, n, 1):
            total = float(add(total, list[var]))
        z = float(div(n, total))
        return z
    except Exception as e:
        print("Exception in Mean",e)
        return 0


