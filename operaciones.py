# operaciones.py

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Devuelve la división de dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(a, b):
    """Devuelve la potencia de a elevado a b."""
    return a ** b

def division_entera(a, b):
    """Devuelve la división entera (sin decimales)."""
    if b == 0:
        raise ValueError("No se logra dividir entre cero.")
    return a // b
