def div(a, b):
    a = float(a)
    b = float(b)
    try:
        c = b / a
        return  c
    except ZeroDivisionError:
        print("Number Cannot be Devided by zero")
        c = 0
        return c
