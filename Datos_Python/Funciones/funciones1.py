
print("--------Funciones en Python---------")


def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def separacion(): 
    print("*******************************")    

def main():
    for x in range(5):
        carga_suma()
        separacion()

# programa principal
if __name__ == "__main__":
  main()