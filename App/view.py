"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

user_track="user_track_hashtag_timestamp-small.csv"
context="context_content_features-small.csv"
sentiment = "sentiment_values.csv"

cont = None
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- caracterizar las reproducciones")
    print("4-  Encontrar música para festejar")
    print("5-  Encontrar música para estudiar")
    print("6-  Estimar las reproducciones de los géneros musicales ")
    print("7- Indicar el género musical más escuchado en un tiempo")


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.iniciar()

    elif int(inputs[0]) == 2:
        print("\nCargando información de canciones ....")
        controller.loadData(cont, context,sentiment,user_track)
        print('registros de eventos de escucha cargados: ' + str(controller.registroSize(cont)))
        print('artistas cargados: ' + str(controller.artistSize(cont)))
        print('canciones cargadas: ' + str(controller.tracksize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('primeros 5 y los ultimos 5 eventos de escucha ' + str(controller.indexSize(cont)))
    elif int(inputs[0]) == 3:
        caracteristica = input("ingresa la caracteristica que deseas consultar: ")
        valor_minimo = input("ingresa el valor minimo de la caracteristica: ")
        valor_maximo = input("ingresa el valor maximo de la caracteristica: ")
        respuesta = controller.caracterizar(caracteristica,valor_minimo,valor_maximo,cont)
        print("el total de artistas que cumplen con las condiciones son: " + str(respuesta[0]))
        print("el total de canciones que cumplen con las condiciones son: " + str(respuesta[1]))
    elif int(inputs[0]) == 4:
        valor_min_energy = float(input("ingresa el valor minimo de energy: "))
        valor_max_energy = float(input("ingresa el valor maximo de energy: "))
        valor_min_Danceability = float(input("ingresa el valor minimo de danceability: "))
        valor_max_Danceability = float(input("ingresa el valor maximo de danceability: "))
        respuesta = controller.musica_festejar(valor_min_energy,valor_max_energy,valor_min_Danceability,valor_max_Danceability,cont)
        print("total de canciones unicas que cumplen con las condiciones: "+ str(respuesta[1]))
        cancion1=respuesta[0][0]
        cancion2 =respuesta[0][1]
        cancion3 =respuesta[0][2]
        cancion4 =respuesta[0][3]
        cancion5 =respuesta[0][4]
        print("cancion 1: {0} con energy {1} y dancehall {2}".format(cancion1[2],cancion1[1],cancion1[0]))
        print("cancion 2: {0} con energy {1} y dancehall {2}".format(cancion2[2],cancion2[1],cancion2[0]))
        print("cancion 3: {0} con energy {1} y dancehall {2}".format(cancion3[2],cancion3[1],cancion3[0]))
        print("cancion 4: {0} con energy {1} y dancehall {2}".format(cancion4[2],cancion4[1],cancion4[0]))
        print("cancion 5: {0} con energy {1} y dancehall {2}".format(cancion5[2],cancion5[1],cancion5[0]))
    elif int(inputs[0]) == 5:
        valor_min_instrumentalness = input("ingrese el valor minimo para instrumentalness: ")
        valor_max_instrumentalness = input("ingresa el valor maximo para instrumentalness: ")
        valor_min_tempo = input("ingresa el valor maximo para tempo: ")
        valor_max_tempo = input("ingresa el valor maximo para temo: ")
        respuesta = controller.musica_estudiar(valor_min_instrumentalness,valor_max_instrumentalness,valor_min_tempo,valor_max_tempo,cont) 
        print("total de canciones unicas que cumplen con las condiciones: "+ str(respuesta[1]))
        cancion1=respuesta[0][0]
        cancion2 =respuesta[0][1]
        cancion3 =respuesta[0][2]
        print("cancion 1: {0} con instrumentalness {1} y tempo {2}".format(cancion1[0],cancion1[1],cancion1[2]))
        print("cancion 2: {0} con instrumentalness {1} y tempo {2}".format(cancion2[0],cancion2[1],cancion2[2]))
        print("cancion 3: {0} con instrumentalness {1} y tempo {2}".format(cancion3[0],cancion3[1],cancion3[2]))
    elif int(inputs[0]) == 6:
        print("¿deseas introducir tu propio genero?")
        centinela = input("si lo deseas oprima 1 en caso de que no oprima cualquier otro numero: ")
        generos_usuario={} #es un diccionario que almacena los datos de los nuevos generos
        numero_genero_buscar_centinela = 0 #determina el numero de generos que desea buscar
        lista_genero = [] #lista de generos que se desea buscar
        if int(centinela) == 1:
            o=0
            numero_genero = int(input("¿cuantos generos deseas añadir? ingrese el numero: "))
            while (o < numero_genero ):
                lst_tempo=[] #almacena temporalmente los datos del tempo
                nombre_genero = input("¿que nombre desea para el nuevo genero?: ")
                tempo_min = input("¿que tempo minimo desea para el nuevo genero?: ")
                tempo_max = input("¿que tempo maximo desea para el nuevo genero?: ")
                lst_tempo.append(tempo_min)
                lst_tempo.append(tempo_max)
                generos_usuario[nombre_genero]=lst_tempo
                o+=1
        numero_genero_buscar= input("¿cuantos generos desea buscar?: ")
        while numero_genero_buscar_centinela < int(numero_genero_buscar):
            genero= input("ingrese un genero: ")
            lista_genero.append(genero)
            numero_genero_buscar_centinela+=1

        respuesta=controller.encontrar_genero(lista_genero,centinela,generos_usuario,cont)  
        for h in respuesta:
            temmpo_genero = controller.saber_tempo_genero(h)
            print("======== {0} ========".format(h))
            print("el total de artistas unicos son : {0} ".format(len(respuesta[h])))
            print("el tempo del genero esta entre {0} y {1}".format(temmpo_genero[0],temmpo_genero[1]))
            print("artista 1: {0}".format(respuesta[h][0]))
            print("artista 2: {0}".format(respuesta[h][1]))
            print("artista 3: {0}".format(respuesta[h][2]))
            print("artista 4: {0}".format(respuesta[h][3]))
            print("artista 5: {0}".format(respuesta[h][4]))
            print("artista 6: {0}".format(respuesta[h][5]))
            print("artista 7: {0}".format(respuesta[h][6]))
            print("artista 8: {0}".format(respuesta[h][7]))
            print("artista 9: {0}".format(respuesta[h][8]))
            print("artista 10: {0}".format(respuesta[h][9]))
        
    else:
        sys.exit(0)
sys.exit(0)
