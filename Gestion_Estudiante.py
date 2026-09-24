print("=== REGISTRO DE ESTUDIANTE ===")

# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
semestre = int(input("Ingrese su semestre: "))

# Estado de matrícula
matriculado = True

# Solicitar la primera nota
nota1 = float(input("ingresa la nota 1:"))
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

# Cursos  
cursos = [
    "Herramientas de Desarrollo de Software",
    "Base de Datos",
    "Redes"
]

# Mostrar datos
print("\n=== DATOS DEL ESTUDIANTE ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)
print("Semestre:", semestre)

print( "\nNotas:")
    
for i in range(len(notas)):
    print("nota", 1+1, ":", notas[i])
    
    print("\nPromedio:", round(promedio,2))
    print("notas aprobadas:", aprobadas)
    print("notas desaprobadas:", desaprobadas)
    print("Estado:", estado)
    
    #RODRIGO PEPE
print("Hiii")    

