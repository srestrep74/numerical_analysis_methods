import pandas as pd

def evaluate_function(function_str, x):
    return eval(function_str)

def incremental_search(x0, delta, max_iter, function_str):
    x_current = x0
    f_current = evaluate_function(function_str, x_current)
    
    results = [{"Iteration": 0, "x": x_current, "f(x)": f_current}]
    
    if f_current == 0:
        return results, f"{x0} es raíz de f(x)"
    
    for iteration in range(1, int(max_iter) + 1):
        x_next = x_current + delta
        f_next = evaluate_function(function_str, x_next)
        
        results.append({"Iteration": iteration, "x": x_next, "f(x)": f_next})
        
        if f_next == 0:
            return results, f"{x_next} es raíz de f(x)"
        elif f_current * f_next < 0:
            return results, f"Existe una raíz de f(x) entre {x_current} y {x_next}"
        
        x_current, f_current = x_next, f_next
    
    return results, f"Fracaso en {max_iter} iteraciones"

def analyze_cases():
    # Definir los casos
    cases = [
        {"x0": 0.8, "n": 1, "delta": 0.1, "function": "(x - 0.875)"},
        {"x0": -0.5, "n": 14, "delta": 0.1, "function": "(x - 0.875)"},
        {"x0": -0.8, "n": 16, "delta": 0.1, "function": "(x - 0.875)"},
        {"x0": 0, "n": 10, "delta": 0.1, "function": "(x - 0.875)"}
    ]
    
    for idx, case in enumerate(cases, start=1):
        results, message = incremental_search(case["x0"], case["delta"], case["n"], case["function"])
        df_results = pd.DataFrame(results)
        
        print(f"\nCaso {chr(96 + idx).upper()}: x0 = {case['x0']}, n = {case['n']}")
        print(message)
        print(df_results)

if __name__ == "__main__":
    analyze_cases()
