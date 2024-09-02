import pandas as pd
import numpy as np

def get_user_input():
    """
    Prompts the user for initial values required to execute the bisection method.
    Returns the lower bound, upper bound, tolerance, maximum iterations, and the function as a string.
    """
    initial_left_bound = float(input("Enter the initial value Xi (lower bound): "))
    initial_right_bound = float(input("Enter the initial value Xs (upper bound): "))
    tolerance = float(input("Enter the desired tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    function_expression = input("Enter the function to evaluate (use 'x' as the variable): ")
    return initial_left_bound, initial_right_bound, tolerance, max_iterations, function_expression

def evaluate_function_at_point(function_expression, x):
    """
    Evaluates the mathematical function at a given point.
    The function expression is evaluated at the point 'x'.
    """
    function_expression = function_expression.replace('^', '**')  # Replace ^ with ** for exponentiation
    return eval(function_expression)

def print_result_root_found(root):
    """
    Prints that an exact root has been found.
    """
    print(f"{root} is an exact root of f(x)")

def print_result_approximation(approximation, tolerance):
    """
    Prints that an approximation of the root has been found within the given tolerance.
    """
    print(f"{approximation} is an approximation of a root of f(x) with a tolerance of {tolerance}")

def print_result_failure(max_iterations):
    """
    Prints that the bisection method failed to find a root within the maximum number of iterations.
    """
    print(f"Failed to find a root within {max_iterations} iterations")

def bisection_method(initial_left_bound, initial_right_bound, tolerance, max_iterations, function_expression):
    """
    Implements the bisection method to find a root of the given function.
    The method works by repeatedly narrowing down the interval [Xi, Xs] until the root is found or the tolerance is met.
    """
    iteration_data = []  # List to store data for each iteration

    # Evaluate the function at the initial bounds
    function_at_left = evaluate_function_at_point(function_expression, initial_left_bound)
    function_at_right = evaluate_function_at_point(function_expression, initial_right_bound)

    # Check if the initial bounds are roots
    if function_at_left == 0:
        print_result_root_found(initial_left_bound)
        return initial_left_bound, [0]
    elif function_at_right == 0:
        print_result_root_found(initial_right_bound)
        return initial_right_bound, [0]
    elif function_at_left * function_at_right < 0:
        # The function changes sign, so a root exists within [Xi, Xs]
        iteration_count = 0
        midpoint = (initial_left_bound + initial_right_bound) / 2
        function_at_midpoint = evaluate_function_at_point(function_expression, midpoint)
        error = 100  # Initial error is arbitrarily set high

        # Store the initial values
        iteration_data.append((iteration_count, midpoint, function_at_midpoint, error))

        # Iterate until the error is less than the tolerance, the root is found, or max iterations are reached
        while error > tolerance and function_at_midpoint != 0 and iteration_count < max_iterations:
            if function_at_left * function_at_midpoint < 0:
                # Root is in the left subinterval [Xi, midpoint]
                initial_right_bound = midpoint
            else:
                # Root is in the right subinterval [midpoint, Xs]
                initial_left_bound = midpoint

            previous_midpoint = midpoint
            midpoint = (initial_left_bound + initial_right_bound) / 2
            function_at_midpoint = evaluate_function_at_point(function_expression, midpoint)
            error = abs(midpoint - previous_midpoint)

            # Store iteration data
            iteration_count += 1
            iteration_data.append((iteration_count, midpoint, function_at_midpoint, error))

        # Check the termination conditions
        if function_at_midpoint == 0:
            # An exact root was found
            print_result_root_found(midpoint)
        elif error < tolerance:
            # The approximation is within the desired tolerance
            print_result_approximation(midpoint, tolerance)
        else:
            # The method failed to converge to a root within the given number of iterations
            print_result_failure(max_iterations)

        # Convert iteration data to a DataFrame and display it
        iteration_df = pd.DataFrame(iteration_data, columns=["Iteration", "X_m", "f(X_m)", "Error"])
        print("\nResulting Table:")
        print(iteration_df.to_string(index=False))

        return midpoint, iteration_data
    else:
        # The initial interval does not contain a root (no sign change)
        print("The initial interval is inadequate. The bisection method cannot be applied.")
        return None, []

def main():
    sol = np.log2((4)/(abs(-3.1415-(-3.1418))))
    print(sol)

    """
    Main function that coordinates the execution of the bisection method.
    """
    initial_left_bound, initial_right_bound, tolerance, max_iterations, function_expression = get_user_input()
    _, _ = bisection_method(initial_left_bound, initial_right_bound, tolerance, max_iterations, function_expression)

if __name__ == "__main__":
    main()

# f -> 