import math


def sin(num):
    if isinstance(num, DualNumber):
        # Use power series definition to show
        return DualNumber(math.sin(num.real), num.dual * math.cos(num.real))
    return math.sin(num)


def cos(num):
    if isinstance(num, DualNumber):
        # Use power series definition to show
        return DualNumber(math.cos(num.real), -num.dual * math.sin(num.real))
    return math.cos(num)


def tan(num):
    if isinstance(num, DualNumber):
        # Use power series definition to show
        return DualNumber(math.tan(num.real), num.dual / (math.cos(num.real) ** 2))
    return math.tan(num)


def asin(num):
    if isinstance(num, DualNumber):
        return DualNumber(
            math.asin(num.real), num.dual / (math.sqrt(1 - num.real * num.real))
        )
    return math.asin(num)


def acos(num):
    if isinstance(num, DualNumber):
        return DualNumber(
            math.acos(num.real), -num.dual / (math.sqrt(1 - num.real * num.real))
        )
    return math.acos(num)


def atan(num):
    if isinstance(num, DualNumber):
        return DualNumber(math.atan(num.real), num.dual / (1 + num.real * num.real))
    return math.atan(num)


def sqrt(num):
    if isinstance(num, DualNumber):
        return num**0.5
    return math.sqrt(num)


def exp(num):
    if isinstance(num, DualNumber):
        real_result = math.exp(num.real)
        return DualNumber(real_result, real_result * num.dual)
    return math.exp(num)


def log(num):
    if isinstance(num, DualNumber):
        return DualNumber(math.log(num.real), num.dual / num.real)
    return math.log(num)


class DualNumber:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = DualNumber(other, 0)
        return DualNumber(self.real + other.real, self.dual + other.dual)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = DualNumber(other, 0)
        return DualNumber(self.real - other.real, self.dual - other.dual)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = DualNumber(other, 0)
        return DualNumber(
            self.real * other.real, self.dual * other.real + self.real * other.dual
        )

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = DualNumber(other, 0)
        return DualNumber(
            self.real / other.real,
            (self.dual * other.real - self.real * other.dual)
            / (other.real * other.real),
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            other = DualNumber(other, 0)

        real_result = self.real**other.real
        dual_result = real_result * (
            other.real * math.log(self.real) + (self.dual * other.real / self.real)
        )
        return DualNumber(real_result, dual_result)

    def __str__(self):
        return f"{self.real} + {self.dual}e"
