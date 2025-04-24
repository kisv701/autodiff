from auto_diff import evaluate_with_derivatives


def main():
    """Example generating the derivative of x squared for integers 0 to 4."""

    def square(x):
        return x * x

    xs = list(range(5))
    print("f(x): x*x, df(x)/dx: 2*x")
    for x in xs:
        result, derivatives = evaluate_with_derivatives(square, [x])
        print(f"f({x}) = {result}, df/dx({x}) = {derivatives[0]}")


if __name__ == "__main__":
    # Usage: python -m examples.simple
    main()
