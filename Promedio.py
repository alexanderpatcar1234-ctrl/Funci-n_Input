nota1 = float(input("Ingrese la nota1: "))
nota2 = float(input("ingrese la nota2: "))
nota3 = float(input("ingrese la nota3: "))

suma_de_notas = nota1 + nota2 + nota3

promedio = suma_de_notas / 3

print ("Promedio: ", round(promedio,2))

if promedio>=13:
    estado = "aprobado"
elif promedio>=11:
    estado = "Desaprobado"
else:
    estado = "Desaprobado"

print ("Estado del estudiante: ", estado)

    
    