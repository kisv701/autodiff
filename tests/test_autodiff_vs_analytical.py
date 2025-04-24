import unittest
from auto_diff import calculate_derivative
from dual_numbers import sin, cos, tan, acos, asin, atan
import math


class AutoDiffVsAnalyticalDiff(unittest.TestCase):
    def test_linear_function(self):
        def fun(x):
            return 5.0 * x

        analytical_derivative = 5.0
        auto_derivative = calculate_derivative(fun, 5.0)
        self.assertAlmostEqual(analytical_derivative, auto_derivative)

    def test_sin(self):
        for i in range(100):
            angle = (i / 100.0) * 2.0 * math.pi
            analytical_derivative = math.cos(angle)  # d/dx sin(x) = cos(x)
            auto_derivative = calculate_derivative(sin, angle)
            self.assertAlmostEqual(analytical_derivative, auto_derivative)

    def test_cos(self):
        for i in range(100):
            angle = (i / 100.0) * 2.0 * math.pi
            analytical_derivative = -math.sin(angle)  # d/dx cos(x) = -sin(x)
            auto_derivative = calculate_derivative(cos, angle)
            self.assertAlmostEqual(analytical_derivative, auto_derivative)
