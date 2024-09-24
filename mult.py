import pandas as pd
import numpy as np
import math

def evaluate_function(function_expression, x_value):
    """Evaluate the function at a given point x."""
    return eval(function_expression, {"x": x_value, "np": np, "math": math, "abs": abs})

def newton_raphson_multiple_roots_method(initial_guess, tolerance, max_iterations, function_expression, derivative_expression, multiplicity=1):
    """Perform the Newton-Raphson method for multiple roots."""
    function_values = []
    root_approximations = []
    errors = []
    iteration_numbers = []
    
    x_current = initial_guess
    function_current = evaluate_function(function_expression, x_current)
    derivative_current = evaluate_function(derivative_expression, x_current)
    iteration_count = 0
    error = 100
    
    # Storing initial values
    function_values.append(function_current)
    root_approximations.append(x_current)
    errors.append(error)
    iteration_numbers.append(iteration_count)
    
    while error > tolerance and function_current != 0 and derivative_current != 0 and iteration_count < max_iterations:
        # Newton-Raphson method for multiple roots (m = multiplicity)
        x_next = x_current - multiplicity * function_current / derivative_current
        derivative_current = evaluate_function(derivative_expression, x_next)
        function_current = evaluate_function(function_expression, x_next)
        
        # Store the current values
        function_values.append(function_current)
        root_approximations.append(x_next)
        iteration_count += 1
        error = abs(root_approximations[iteration_count] - root_approximations[iteration_count-1])
        
        iteration_numbers.append(iteration_count)
        errors.append(error)
        
        # Update for next iteration
        x_current = x_next
    
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
    initial_guess = float(input("Enter the initial value X0: "))
    tolerance = float(input("Enter the desired tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    function_expression = input("Enter the function f(x) to evaluate (use 'x' as the variable): ")
    derivative_expression = input("Enter the derivative function f'(x) (use 'x' as the variable): ")
    multiplicity = int(input("Enter the multiplicity of the root: "))

    # Run the Newton-Raphson method for multiple roots
    root_approximations, function_values, errors, iteration_numbers = newton_raphson_multiple_roots_method(
        initial_guess, tolerance, max_iterations, function_expression, derivative_expression, multiplicity)
    
    # Print the results
    print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations)

if __name__ == "__main__":
    main()

# Example:
# f(x) = (x - 2)**3
# f'(x) = 3*(x - 2)**2
