from dual_numbers import DualNumber


def evaluate_with_derivatives(
    fun: callable, parameters: list[float]
) -> tuple[float, list[float]]:
    """Evaluates function "fun" at parameters and give partial derivatives for each of the provided parameters.
    For example given fun(x, y): return x + y
    then calling this function with parameters [1, 2] will return (3, [1, 1]) because
    f() 1 + 2 = 3
    d/dx(x + 2) = 1
    d/dy(1 + y) = 1

    Args:
        fun (callable): Some function to evaluate and give derivatives for.
        parameters (list[float]): List of arguments to fun. Partial derivative for each parameter will be returned.

    Returns:
        tuple[float, list[float]]: fun evaluated at parameters, partial derivatives w.r.t each parameter.
    """
    dual_numbers = []
    for param in parameters:
        dual_numbers.append(DualNumber(param, 0.0))

    derivatives = []
    for i in range(len(dual_numbers)):
        # calculating derivative with respect to parameter i.
        dual_numbers[i].dual = 1.0
        result = fun(*dual_numbers)
        derivatives.append(result.dual)
        # reset to zero to prepare for derivative w.r.t i+1
        dual_numbers[i].dual = 0.0

    return result.real, derivatives


def calculate_jacobian(fun: callable, parameters: list[float]) -> list[float]:
    # Auto differentiation using dual numbers
    dual_numbers = []
    for param in parameters:
        dual_numbers.append(DualNumber(param, 0.0))

    derivatives = []
    for i in range(len(dual_numbers)):
        # calculating derivative with respect to parameter i.
        dual_numbers[i].dual = 1.0
        result = fun(*dual_numbers)
        derivatives.append(result.dual)
        # reset to zero to prepare for derivative w.r.t i+1
        dual_numbers[i].dual = 0.0

    return derivatives


def calculate_derivative(fun: callable, parameter: float):
    dual_num = DualNumber(parameter, 1)
    result = fun(dual_num)
    return result.dual
