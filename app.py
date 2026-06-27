# Autor: Francisco Solórzano
# Calculadora básica en Python

def solicitar_numero(mensaje):
    """Solicita un número y valida la entrada."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def mostrar_menu():
    print("\n===== CALCULADORA BÁSICA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    print("Bienvenido a la Calculadora")
    print("Autor: Francisco Solórzano")

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("Gracias por utilizar la calculadora.")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1 = solicitar_numero("Ingrese el primer número: ")
            num2 = solicitar_numero("Ingrese el segundo número: ")

            if opcion == "1":
                resultado = suma(num1, num2)
                print(f"Resultado de la suma: {resultado}")

            elif opcion == "2":
                resultado = resta(num1, num2)
                print(f"Resultado de la resta: {resultado}")

            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"Resultado de la multiplicación: {resultado}")

            elif opcion == "4":
                resultado = division(num1, num2)
                print(f"Resultado de la división: {resultado}")

        else:
            print("Opción no válida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
    