import math
import pandas as pd
import numpy as np

def get_input(prompt):
    return float(input(prompt))

def evaluate_function(function_str, x):
    return eval(function_str)

def incremental_search(x0, delta, max_iter, function_str):
    x_current = x0
    f_current = evaluate_function(function_str, x_current)
    
    # Almacenar datos para la tabla
    results = [{"Iteration": 0, "x": x_current, "f(x)": f_current}]
    
    if f_current == 0:
        print(f"{x0} es raíz de f(x)")
        return results
    
    for iteration in range(1, int(max_iter) + 1):
        x_next = x_current + delta
        f_next = evaluate_function(function_str, x_next)
        
        results.append({"Iteration": iteration, "x": x_next, "f(x)": f_next})
        
        if f_next == 0:
            print(f"{x_next} es raíz de f(x)")
            return results
        elif f_current * f_next < 0:
            print(f"Existe una raíz de f(x) entre {x_current} y {x_next}")
            return results
        
        x_current, f_current = x_next, f_next
    
    print(f"Fracaso en {max_iter} iteraciones")
    return results

def main():
    x0 = get_input("X0: ")
    delta = get_input("Delta: ")
    max_iter = get_input("Número de iteraciones: ")
    function_str = input("Función (en términos de 'x'): ")
    
    results = incremental_search(x0, delta, max_iter, function_str)
    
    # Convertir a DataFrame e imprimir la tabla
    df_results = pd.DataFrame(results)
    print("\nTabla de resultados:")
    print(df_results)

if __name__ == "__main__":
    main()
