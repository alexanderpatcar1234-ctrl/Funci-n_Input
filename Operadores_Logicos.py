# and : ambas condiciones deben cumplirse
# or : basta que una condicion se cumpla
# not : invierte una condicion 

import Promedio


matriculado = True

if Promedio >= 13 and matriculado == True:
    print("puede ingresar al curso en el aula virtual")
else:
    print ("Estudiante no puede ingresar al aula virtual")
    if Promedio >= 13 or matriculado == False:
        print("Contactarse con el estudiante")
        