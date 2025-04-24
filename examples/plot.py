from auto_diff import calculate_derivative
from dual_numbers import sin
from matplotlib import pyplot as plt  # pip install matplotlib
from math import pi


def main():
    """A simple example plotting sin(x) for x from 0 to 2pi and its derivate i.e. cos(x) for the same interval"""
    xs = [x * pi / 100.0 for x in range(0, 200)]
    plt.plot(xs, [sin(x) for x in xs], label="f(x) -> sin(x)")
    plt.plot(xs, [calculate_derivative(sin, x) for x in xs], label="df(x)/dx -> cos(x)")
    plt.title("Example 2 AutoDiff of sin(x) gives cos(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Usage: python -m examples.plot
    main()
