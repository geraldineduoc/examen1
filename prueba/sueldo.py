import random
import statistics

trabajadores = ['nombre:' "Juan perez", 'nombre' "maria garcia", 'nombre' "carlos lopez", 'nombre' "ana martinez",'nombre' "pedro rodriguez" 'nombre' "laura hernandez" 'nombre' "miguel sanchez" 'nombre' "isabel gomez" 'nombre' "francisco diaz" 'nombre' "elena fernandez"]

valores = [300000, 2500000]
sueldo_aleatorio = random.randint(valores)
dato = statistics.geometric_mean(valores)

def menu():
    print("1.- asignar sueldo: ")
    print("2.- clasificar sueldos: ")
    print("3.- ver estadisticas: ")
    print("4.- reporte de sueldo: ")
    print("5: salir")


def sueldo():
    bajo = min(valores)
    alto = max(valores)


    with open('empleados.txt', 'r') as empleados_txt:
        for linea in empleados_txt:
            empleados_data = linea.strip().split(',')
            trabajadores.append(empleados_data) 


    while bajo < alto:
        menu()
        op = int(input("ingrese una opcion"))
        if op == 1:
            trabajadores = ['nombre:' "Juan perez", 'nombre' "maria garcia", 'nombre' "carlos lopez", 'nombre' "ana martinez",'nombre' "pedro rodriguez" 'nombre' "laura hernandez" 'nombre' "miguel sanchez" 'nombre' "isabel gomez" 'nombre' "francisco diaz" 'nombre' "elena fernandez"]
            trabajadores.append(input(f"trabajador: {trabajadores[0, 9]}")) 
            trabajadores.append(input(f"ingresar sueldo: {sueldo_aleatorio[valores]}"))
          
            trabajadores.append(trabajadores)         
            print("sueldo ingresado correctamente.")   
        elif op == 2: 
            clasificar = input("mostar lista de empleados ")
            if sueldo  == clasificar:
                print("nombre trabajador: ")
                print("sueldo: ")

           # if op == 3:
           
           # if op == 4: 
               # ("")
   # else:
    #    op == 5:
     #   print("salir")
    