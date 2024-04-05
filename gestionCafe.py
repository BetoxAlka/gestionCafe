import pytest # Importar pytest para las pruebas
import numpy as np # Importar numpy para operaciones
import math # Importar math para redondeo

def cafe(drink): # Funcion que representa la Gestion de las Bebidas, recibe la lista con los valores de esta [Nombre, t1, t2, t3, t4, t5]
    name = drink[0] # El primer elemento de la lista siempre deberá ser el nombre
    name = name.replace(" ","") # Se eliminan espacios en blanco
    
    if len(name) >= 2 and len(name) <= 15 and name.isalpha(): # Se comprueba que el primer elemento sea un nombre alfabetico entre 2 y 15 caracteres
        key = True # Llave de paso para la condicion de que todos los tamanios sean validos
        if len(drink) > 1 and len(drink) < 7: # Condicion que define si hay al menos un tamanio, y menos de cinco
            sizes = [] # Lista de tamanios
            for s in range(1, len(drink)): # Recorre la lista para obtener todos los tamanios
                size = drink[s] # Se define una variable como el tamanio actual
                size = size.replace(" ","") # Se eliminan los espacios del tamanio
                if float(size) >= 1 and float(size) <= 48: # Condicion que revisa que el tamanio este en un rango de entre 1 y 48
                    sizes.append(math.floor(float(size))) # Se convierte de string a numero, se redondea y se agrega a la lista de tamanios
                else:
                    key = False # Si la condicion anterior no se cumple, la llave de paso se cierra
                    return "Tamanio INVALIDO" #Se regresa el texto que le hace saber al usuario que su entrada fue invalida
        
            if key == True:    
                if lista_es_ordenada(sizes): # Se comprueba que la lista de tamanios este ordenada de manera ascendente
                    registro = "Nombre de la bebida: " + name + " | Tamanios para la bebida: " + "".join(str(sizes)) # Una vez se revisa que todo se cumpla, se escribe el registro
                    write_in_file("RegistroBebidas.txt",registro) # Se sube el registro de la bebida a un archivo
                    return registro # Y se le muestra al usuario su registro
                else:
                    return "Los tamanios no estan ordenados de forma ascendente" # Invalido
            
        else:
            return "Cantidad de tamanios INVALIDO" # Invalido
            
    else:
        return "Nombre de la bebida INVALIDO" # Invalido

def lista_es_ordenada(lista): # Funcion que comprueba que una lista esta ordenada de manera ascendente
    ordenada = True # Define si esta ordenada
    for i in range(1, len(lista)): # Se recorre la lista
        if lista[i] < lista[i - 1]: # Se compara con su anterior
            ordenada = False # Si este es menor entonces la condicion no se cumples
            break
    return ordenada # Regresa si la lista esta ordenada o no

def stringtolist(str): # Funcion que transforma un string a una lista
    delim = "," # Indicador para separar el string por las comas
    arrange = str.split(delim) # Funcion que separa el string conforme al indicador
    return arrange # Regresa el texto dividido
    
def write_in_file(fileName,text): # Funcion para sobreescribir un archivo existente, recibe nombre del archivo y texto a escribir
    with open(fileName,"a", encoding="utf8") as file: # Abre o crea un archivo con el metodo de sobreescribir sobre la ultima linea
        newline = "\n" + text # Se crea una nueva linea con el texto especificado
        file.write(newline) # Se escribe la linea
    
    file.close() # Es importante cerar el Archivo
    
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
    entrada = input() # Input del usuario
    
    bebida = stringtolist(entrada) # De string a lista
    
    respuesta = cafe(bebida) # Registro de Bebida
    print(respuesta) # Respuesta al usuario
    
    
    