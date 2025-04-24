from auto_diff import calculate_jacobian
import pyceres  # pip install pyceres
import numpy as np  # pip install numpy


class HypFiveTriangle(pyceres.CostFunction):
    def __init__(self):
        pyceres.CostFunction.__init__(self)
        self.set_num_residuals(1)
        self.set_parameter_block_sizes([2])

    def Evaluate(self, parameters, residuals, jacobians):
        a = parameters[0][0]
        b = parameters[0][1]
        residuals[0] = fun(a, b)
        if jacobians is not None:
            jac = calculate_jacobian(fun, [a, b])  # jac is [df/da, df/db]
            jacobians[0][0] = jac[0]
            jacobians[0][1] = jac[1]
        return True


class SideFourTriangle(pyceres.CostFunction):
    def __init__(self):
        pyceres.CostFunction.__init__(self)
        self.set_num_residuals(1)
        self.set_parameter_block_sizes([2])

    def Evaluate(self, parameters, residuals, jacobians):
        b = parameters[0][1]
        residuals[0] = b - 4
        if jacobians is not None:
            jacobians[0][0] = 0  # put 0 since a does not matter when we look for b=4.
            jacobians[0][1] = 1  # df/db of f(b) = b - 4 is 1
        return True


def fun(a, b):
    hypotenuse = 5  # Goal is to find a and b such that hypotenuse is 5.
    # Pythagoras tells us a*a + b*b = c*c
    return a * a + b * b - hypotenuse * hypotenuse


def main():
    """Example finding the side lengths of a right triangle with hypotenuse 5 and one side 4 using pyceres and autodiff."""
    initial_guess = np.array([1.0, 1.0])
    params = np.copy(initial_guess)

    prob = pyceres.Problem()
    cost_hyp = HypFiveTriangle()
    cost_side = SideFourTriangle()
    prob.add_residual_block(cost_hyp, None, [params])
    prob.add_residual_block(cost_side, None, [params])
    options = pyceres.SolverOptions()
    options.minimizer_progress_to_stdout = True
    summary = pyceres.SolverSummary()
    pyceres.solve(options, prob, summary)

    print(summary.BriefReport())
    print(f"a: {initial_guess[0]:.2f} -> {params[0]:.2f}")
    print(f"b: {initial_guess[1]:.2f} -> {params[1]:.2f}")
    if (round(params[0]) == 3 and round(params[1]) == 4) or (
        round(params[0]) == 4 and round(params[1]) == 3
    ):
        print("We found classic 3-4-5 triangle!")


if __name__ == "__main__":
    # Usage: python -m examples.pyceres_triangle
    main()
