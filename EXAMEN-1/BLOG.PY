print("=== REGISTRO DE ALQUILES ===")

# Solicitar datos
Responsable = input("Ingrese su nombre: ")
Equipo = (input("Ingrese el equipo: "))
Costo_por_dia = input("Ingrese el costo por dia: ")
Dias_de_Alquiler =int(input("Ingrese Dias de Alquiler: "))
Disponible = input("\nDisponible:")

# Estado de matrícula
matriculado = True

# Solicitar la primera nota
nota1 = float(input("Equipos_Disponibles:"))
while nota1 < 0 or nota1> 20:
    print("la nota debe estar entre 0 y 20")
    nota1 = float(input("ingresa la nota 1"))
 
nota2 = float(input("ingresa la nota 2:"))
while nota2 < 0 or nota2 > 20:
    print("la nota debe estar entre 0 y 20")
    nota2 = float(input("ingresa la nota 2"))
    
nota3 = float(input("ingresa la nota 3:"))
while nota3 < 0 or nota3> 20:
    print("la nota debe estar entre 0 y 20")
    nota3 = float(input("ingresa la nota 3"))
    
    
       
#creamos una lista de notas
notas =[nota1, nota2, nota3]

#Acumuladores y contadores
suma = 0
aprobada = 0
desaprobadas = 0
# Cursos

#procesador de notas 
for nota in notas:
    suma = suma + nota
    if nota >=13:
        aprobadas = aprobada + 1
    else:
        desaprobadas = desaprobadas +1
        
#calcular promedio
promedio = suma / len(notas)

#Clasificar al estudiante
if promedio >= 17: 
    estado = "puede acceder a la beca en URUSAYHUA"
else:
    estado = "tiene que pagar la matricula completa"

#EQUIPOS DISPONIBLES
Equipos_Disponibles = [
    "-Laptop"
    "-royector"
    "-Parlante"
]

# Mostrar datos
print("\n=== REGISTRO DE ALQUILER ===")
print("Responsable:", Responsable)
print("Equipo:", Equipo)
print("Costo_por_Dia:", Costo_por_dia)
print("Dias_de_Alquiler", Dias_de_Alquiler)
print("Disponible", Disponible)

print( "\nNotas:")
    
for i in range(len(notas)):
    print("nota", 1+1, ":", notas[i])
    
    print("\nPromedio:", round(promedio,2))
    print("notas aprobadas:", aprobadas)
    print("notas desaprobadas:", desaprobadas)
    print("Estado:", estado)