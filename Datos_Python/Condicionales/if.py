#Ejemplo Básico de condicionales.

def obtener_calificacion(nota):
    if nota >= 90:
        return "Excelente"
    elif 70 <= nota < 90:
        return "Bueno"
    else:
        return "Debes esforzarte más."
    
def mensaje():
    print("-----Notas Escolares------")

def main():
    mensaje()
    try:
        nota = float(input("Ingresa la nota: "))
        if 0 <= nota <= 100:
            calificacion = obtener_calificacion(nota)
            print(f"Calificación: {calificacion}")
        else:
            print("La nota debe estar en el rango de 0 a 100.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
