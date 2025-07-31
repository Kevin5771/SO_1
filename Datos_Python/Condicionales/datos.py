salarioPresidente = int(input("Introduce el salario Presidente: "))

print("Salario Presidente: " + str(salarioPresidente))

salarioAuditor = int(input("Introduce el salario Auditor: "))

print("Salario Auditor: " + str(salarioAuditor))

if salarioPresidente > salarioAuditor:
    print("Todo funciona correctamente")

elif salarioAuditor > salarioPresidente:
    print("Algo anda mal")