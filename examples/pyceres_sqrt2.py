from auto_diff import calculate_derivative
import pyceres  # pip install pyceres
import math
import numpy as np


class SqrtTwo(pyceres.CostFunction):
    def __init__(self):
        pyceres.CostFunction.__init__(self)
        self.set_num_residuals(1)
        self.set_parameter_block_sizes([1])

    def Evaluate(self, parameters, residuals, jacobians):
        residuals[0] = fun(parameters[0][0])
        if jacobians is not None:
            jacobians[0][0] = calculate_derivative(fun, parameters[0][0])
        return True


def fun(a):
    return a * a - 2.0


def main():
    """Example finding the square root of 2."""
    initial_guess = np.array([1.0])
    params = np.copy(initial_guess)

    prob = pyceres.Problem()
    cost = SqrtTwo()
    prob.add_residual_block(cost, None, [params])
    options = pyceres.SolverOptions()
    options.minimizer_progress_to_stdout = True
    summary = pyceres.SolverSummary()
    pyceres.solve(options, prob, summary)

    print(summary.BriefReport())
    print(f"a: {initial_guess[0]:.2f} -> {params[0]}")
    print(f"math.sqrt(2) -> {math.sqrt(2)}")


if __name__ == "__main__":
    # Usage: python -m examples.pyceres_sqrt2
    main()
