def get_commands():
    return {
        "calc": calc_expr
    }

def calc_expr(*args):
    expr = " ".join(args)
    try:
        result = eval(expr, {"__builtins__": {}})
        return f"Result: {result}"
    except Exception as e:
        return f"[ERROR] Calculation failed: {e}"
