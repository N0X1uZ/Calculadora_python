# calculadora.py

import operaciones

def main():
    print("=== Calculadora Modular ===")

    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        if operador == '+':
            resultado = operaciones.suma(a, b)
        elif operador == '-':
            resultado = operaciones.resta(a, b)
        elif operador == '*':
            resultado = operaciones.multiplicacion(a, b)
        elif operador == '/':
            resultado = operaciones.division(a, b)
        elif operador == '**':
            resultado = operaciones.potencia(a, b)
        elif operador == '//':
            resultado = operaciones.division_entera(a, b)
        else:
            print("Operador inválido. Use +, -, *, /, ** o //.")
            return

        print(f"Resultado: {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
