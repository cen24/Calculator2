from Calculator.computation.addition import add
from Calculator.computation.substraction import sub
from Calculator.computation.multiplication import times
from Calculator.computation.division import div
from Calculator.computation.square import square
from Calculator.computation.squareroot import sqrt

class calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = sub(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = times(a, b)
        return self.result

    def division(self, a, b):
        self.result = div(a, b)
        return self.result

    def square_(self, a):
        self.result = square(a)
        return self.result

    def sqrt_(self, a):
        self.result = sqrt(a)
        return self.result
