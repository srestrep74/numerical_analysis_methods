import pandas as pd
import numpy as np
import math

def evaluate_function(function_expression, x_value):
    """Evaluate the function at a given point x."""
    return eval(function_expression, {"x": x_value, "np": np, "math": math, "abs": abs})

def false_position_method(x0, x1, tolerance, max_iterations, function_expression):
    """Perform the False Position (Regla Falsa) method."""
    function_values = []
    root_approximations = []
    errors = []
    iteration_numbers = []
    
    function_x0 = evaluate_function(function_expression, x0)
    function_x1 = evaluate_function(function_expression, x1)
    iteration_count = 0
    error = 100
    
    if function_x0 * function_x1 > 0:
        print("No se puede aplicar el método: f(x0) y f(x1) tienen el mismo signo.")
        return
    
    # Initial storage
    function_values.append(function_x0)
    root_approximations.append(x0)
    errors.append(error)
    iteration_numbers.append(iteration_count)
    
    while error > tolerance and iteration_count < max_iterations:
        # Calculate the point of intersection with the x-axis
        x_next = x1 - (function_x1 * (x1 - x0)) / (function_x1 - function_x0)
        function_x_next = evaluate_function(function_expression, x_next)
        
        # Store the current values
        function_values.append(function_x_next)
        root_approximations.append(x_next)
        iteration_count += 1
        error = abs(root_approximations[iteration_count] - root_approximations[iteration_count - 1])
        
        iteration_numbers.append(iteration_count)
        errors.append(error)
        
        if function_x_next == 0:
            break
        elif function_x0 * function_x_next < 0:
            x1 = x_next
            function_x1 = function_x_next
        else:
            x0 = x_next
            function_x0 = function_x_next
    
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
        print(f"{root_approximations[-1]} es una raíz de f(x)")
    elif errors[-1] < tolerance:
        print(f"{root_approximations[-1]} es una aproximación de una raíz de f(x) con una tolerancia de {tolerance}")
    else:
        print(f"El método fracasó en {max_iterations} iteraciones")
    
def main():
    x0 = float(input("Ingrese el valor inicial X0: "))
    x1 = float(input("Ingrese el valor inicial X1: "))
    tolerance = float(input("Ingrese la tolerancia deseada: "))
    max_iterations = int(input("Ingrese el número máximo de iteraciones: "))
    function_expression = input("Ingrese la función f(x) a evaluar (use 'x' como la variable): ")

    # Run the False Position method
    root_approximations, function_values, errors, iteration_numbers = false_position_method(
        x0, x1, tolerance, max_iterations, function_expression)
    
    # Print the results
    print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations)

if __name__ == "__main__":
    main()


# Ejemplo de uso:
# f -> 2*np.sin(np.sqrt(np.abs(x+2)))-x
