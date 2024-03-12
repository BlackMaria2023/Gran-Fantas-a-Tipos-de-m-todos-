import random
from personaje import Personaje

print("Bienvenido a Gran Fantasía")
nombre = input("Ingrese el nombre del personaje: ")

#Instanciacion de la clase Personaje en el objeto 'p' 
p = Personaje(nombre) 
#Se llama al getter
print(p.estado)

print("¡Oh no! ¡Ha aparecido un orco!")
#Orco fuerte y peligroso :c 
#instancia orco 
o = Personaje("Orco")
#Le paso 'o' que es la instancia del orco a la probabilidad de ganar. 
probabilidad = p.probabilidad_ganar(o)
#Le paso la probabilidad, para que la escriba en el texto. 
#Esta es la forma de llamar a los metodos estáticos : forma Clase.Metodo_estático(Variable a pasar en caso de ser necesario)
opcion_orco = Personaje.mostrar_dialogo(probabilidad)

while opcion_orco == 1: 
    resultado = "Ganaste" if random.uniform(0,1) < probabilidad else "Perdiste"
    if resultado =="Ganaste":
        print("""
              ¡Felicidades! ¡Le has ganado al orco!\n 
              "Recibirás 50 puntos de experiencia c: y el orco perderá 30 puntos C: 
              """)
        
        #Para cada dato a modificar, se necesita llamar el metodo setter
        #Modifica el nivel a partir de la experiencia. 
        #El interprete decide cual metodo ocupar dependiento de que si quiere agregar o mostrar
        #En este caso se agrega, utilizando el metodo setter
        p.estado = 50
        o.estado = -30
    
    else: 
        print("""¡Lo siento! ¡Has perdido!\n
              El Orco te ha derrotado... Pierdes 30 puntos y el Orco gana 50 puntos :c \n""")
        
        
        p.estado = -30
        o.estado = 50 
    
    #Detalle de resultados, a diferencia del caso anterior, solo muestra, por lo cual llama al getter 
    print(p.estado)
    print(o.estado)    
    
    probabilidad = p.probabilidad_ganar(o)
    opcion_orco = Personaje.mostrar_dialogo(probabilidad)
