import numpy as np # Importar numpy para operaciones
import math # Importar math para redondeo

def cafe(drink):
    name = drink[0]
    name = name.replace(" ","")
    
    if len(name) >= 2 and len(name) <= 15 and name.isalpha():
        key = True
        if len(drink) > 1 and len(drink) < 7:
            sizes = []
            for s in range(1, len(drink)):
                size = drink[s]
                size = size.replace(" ","")
                if float(size) >= 1 and float(size) <= 48:
                    sizes.append(math.floor(float(size)))
                else:
                    print("Un tamanio es INVALIDO")
                    key = False
        
            if key == True:    
                if lista_es_ordenada(sizes):
                    registro = "Nombre de la bebida: " + name + " | Tamanios para la bebida: " + "".join(str(sizes))
                    print(registro)
                    write_in_file("RegistroBebidas.txt",registro)
                else:
                    print("Los tamanios no estan ordenados de forma ascendente")
            
        else:
            print("Cantidad de tamanios INVALIDO")
            
    else:
        print("Nombre de la bebida INVALIDO")

def lista_es_ordenada(lista):
    ordenada = True
    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            ordenada = False
            break
    return ordenada

def stringtolist(str):
    delim = ","
    arrange = str.split(delim)
    return arrange
    
def write_in_file(fileName,text): 
    with open(fileName,"a", encoding="utf8") as file: 
        newline = "\n" + text
        file.write(newline) 
    
    file.close()
    
if __name__ == '__main__':
    print("-------------------- Bienvenido al sistema para registrar bebidas a la Cafeteria --------------------")
    print("***** A continuacion, podras registrar una bebida *****")
    print("Para hacerlo deberas ingresar el nombre de la bebida, seguido de hasta maximo 5 tamanios para esta")
    print("Toma en cuenta los siguientes lineamientos:")
    print("El nombre debe ser el primero en ser ingresado, este debe ser alfabetico y tener entre 2 y 15 caracteres")
    print("Los tamanios seran ingresados despues, cada uno separado por una coma, se debe ingresar al menos uno")
    print("Los tamanios deben estar en un rango de 1 a 48")
    print("Estos deben ser tamanios enteros en caso contrario se redondeara hacia abajo")
    print("Se deben ingresar de forma ascendente")
    print("RECUERDA: Separar el nombre y cada tamanio con una coma")
    
    print("Ingresa la bebida: ")
    entrada = input()
    
    bebida = stringtolist(entrada)
    
    cafe(bebida)
    
    
    