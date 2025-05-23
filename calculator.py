# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def main():
    print("Calculadora básica en Python")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        choice = input("Seleccione una operación (1/2/3/4) o 'q' para salir: ")
        if choice == 'q':
            print("Saliendo de la calculadora.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Opción inválida. Intente de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor ingrese números.")
            continue

        if choice == '1':
            print(f"Resultado: {add(num1, num2)}")
        elif choice == '2':
            print(f"Resultado: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Resultado: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Resultado: {divide(num1, num2)}")

if __name__ == "__main__":
    main()