import pandas as pd
import numpy as np
import math

def evaluate_function(function_expression, x_value):
    """Evaluate the function at a given point x."""
    return eval(function_expression, {"x": x_value, "np": np, "math": math, "abs": abs})

def secant_method(x0, x1, tolerance, max_iterations, function_expression):
    """Perform the Secant method."""
    function_values = []
    root_approximations = []
    errors = []
    iteration_numbers = []
    
    iteration_count = 0
    error = 100
    
    f_x0 = evaluate_function(function_expression, x0)
    f_x1 = evaluate_function(function_expression, x1)
    
    # Storing initial values
    function_values.append(f_x1)
    root_approximations.append(x1)
    errors.append(error)
    iteration_numbers.append(iteration_count)
    
    while error > tolerance and f_x1 != 0 and iteration_count < max_iterations:
        # Secant method formula
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        f_x_next = evaluate_function(function_expression, x_next)
        
        # Store the current values
        function_values.append(f_x_next)
        root_approximations.append(x_next)
        iteration_count += 1
        error = abs(root_approximations[iteration_count] - root_approximations[iteration_count-1])
        
        iteration_numbers.append(iteration_count)
        errors.append(error)
        
        # Update for next iteration
        x0, x1 = x1, x_next
        f_x0, f_x1 = f_x1, f_x_next
    
    return root_approximations, function_values, errors, iteration_numbers

def print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations):
    """Print the results in a table format."""
    results = pd.DataFrame({
        'Iteration': iteration_numbers,
        'x_n': root_approximations,
        'f(x_n)': function_values,
        'Error': errors
    })
    
    print(results)
    
    # Check the outcome
    if function_values[-1] == 0:
        print(f"{root_approximations[-1]} is a root of f(x)")
    elif errors[-1] < tolerance:
        print(f"{root_approximations[-1]} is an approximation of a root of f(x) with tolerance {tolerance}")
    else:
        print(f"Failed to converge in {max_iterations} iterations")
    
def main():
    method = input("Enter the method to use (newton/secant): ").strip().lower()
    tolerance = float(input("Enter the desired tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    
    if method == "newton":
        initial_guess = float(input("Enter the initial value X0: "))
        function_expression = input("Enter the function f(x) to evaluate (use 'x' as the variable): ")
        derivative_expression = input("Enter the derivative function f'(x) (use 'x' as the variable): ")

        # Run the Newton-Raphson method
        root_approximations, function_values, errors, iteration_numbers = newton_raphson_method(
            initial_guess, tolerance, max_iterations, function_expression, derivative_expression)
    
    elif method == "secant":
        x0 = float(input("Enter the first initial value X0: "))
        x1 = float(input("Enter the second initial value X1: "))
        function_expression = input("Enter the function f(x) to evaluate (use 'x' as the variable): ")

        # Run the Secant method
        root_approximations, function_values, errors, iteration_numbers = secant_method(
            x0, x1, tolerance, max_iterations, function_expression)
    
    else:
        print("Invalid method. Choose either 'newton' or 'secant'.")
        return
    
    # Print the results
    print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations)

if __name__ == "__main__":
    main()
