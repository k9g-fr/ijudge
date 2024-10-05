"""Compo func"""
def f(x):
    """function f"""
    return x*2

def g(x):
    """function g"""
    return x/2 + 1
print(f(g(-5)))
print(g(f(-5)))
