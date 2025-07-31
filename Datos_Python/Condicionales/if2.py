def clasificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Igual a cero"

def main():
    try:
        numero = float(input("Ingresa un número: "))
        resultado = clasificar_numero(numero)
        
        print(f"El número ingresado es {resultado}.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
