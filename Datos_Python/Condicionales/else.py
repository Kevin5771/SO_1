booleano = True  

def separador():
    print("-------------") 

def main():
    global booleano  

    while booleano:  
        print("Verificación de edad")

        try:
            edad = int(input("Introduce tu edad, por favor: "))

            if edad < 18:
                print("No puedes pasar, eres menor de edad.")
                separador()
            elif 18 <= edad < 100:
                print("Eres mayor de edad.")
                separador()
            else:
                print("Dato inválido.")
                separador()
        except ValueError:
            print("Por favor, introduce un número válido.")
            separador()
    
if __name__ == "__main__":
    main()
