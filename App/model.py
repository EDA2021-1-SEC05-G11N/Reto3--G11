"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import random 
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    analyzer = {'user_track': None,
                'context': None,
                "sentiment":None
                }                
    analyzer['user_track'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    analyzer['context'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    analyzer['sentiment'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return analyzer



# Funciones para agregar informacion al catalogo
def agregarsentimentfile(analyzer,sentiment):
    mapa = analyzer["sentiment"]
    hashtag = sentiment["hashtag"]
    om.put(mapa,hashtag,sentiment)
def agregarcontextfile(analyzer,context):
    primeros=0
    mapa = analyzer["context"]
    track_id = context["track_id"]
    om.put(mapa,track_id,context)

def agregaruser_trackfile(analyzer,track):
    mapa= analyzer["user_track"]
    user_id = track["user_id"]
    om.put(mapa,user_id,track)

def artistSize(analyzer):
    """
    Número de artistas
    """
    return om.size(analyzer["user_track"])

def registroSize(analyzer):
    return om.size(analyzer["user_track"])

def tracksize(analyzer):
    return om.size(analyzer["context"])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer["user_track"])

def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['user_track'])
    
# Funciones para creacion de datos

# Funciones de consulta

def caracterizar(caracteristica,valor_minimo,valor_maximo,mapa):
    lst = om.valueSet(mapa["context"]) #saca todos los valores de context en una lista
    p=0 # centinela para recorrer lst
    canciones=0 #centinela para saber el numero de canciones que cumplen los requisitos
    artistas= [] # se creo una lista nueva para almacenar los artistas
    llaves = ["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","mode","key","artist_id","tweet_lang","track_id","created_at","lang","time_zone","user_id","id"] #lista sobre las caracteristicas posibles
    while p < lt.size(lst): #recorrecomos los diccionarios dentro de lst
        x=lt.getElement(lst,p) #contiene un diccionario
        if caracteristica in llaves: #verifica si la llave que introducimos es valida 
            if (x[caracteristica] <= valor_maximo) and  (x[caracteristica] >= valor_minimo): #verifica si cumplen con las condiciones
                canciones+=1 #si cumple con las condiaciones sube la cantidad de canciones 
                if x["artist_id"] not in artistas:
                    artistas.append(x["artist_id"]) #en caso de que el id del artista no este en la lista lo agrega
        else: #en caso de que no sea valida muestra este mensaje
            print("no incluyo una caracteristica valida")
            break
        p+=1
    return (len(artistas),canciones)
    
def musica_festejar(valor_min_energy,valor_max_energy,valor_min_Danceability,valor_max_Danceability,mapa):
    lst = om.valueSet(mapa["context"]) #saca todos los valores de context en una lista
    p=0 # centinela para recorrer lst
    tracks = 0 #centinela para saber el numero de canciones unicas que cumplen con las condiciones 
    tracklst = [] #lista para saber la cantidad de canciones unicas
    id_list = [] # lista de id track
    entregar_id = [] #almacena los datos para entregarlos como lista al final
    while p < lt.size(lst): #recorrecomos los diccionarios dentro de lst
        x=lt.getElement(lst,p) #contiene un diccionaio
        if (float(x["danceability"]) >= valor_min_Danceability ) and (float(x["danceability"]) <= valor_max_Danceability) :
            if ( float(x["energy"]) >= valor_min_energy) and (float(x["energy"]) <= valor_max_energy): #comprueba si cumple con las condiciones
                if x["track_id"] not in tracklst:
                    tracklst.append(x["track_id"])
                    tracks +=1
                    agregar = []
                    agregar.append(x["danceability"])
                    agregar.append(x["energy"])
                    agregar.append(x["track_id"])
                    id_list.append(agregar)
        p+=1   

    #selecciona 5 canciones al azar entre todas las canciones que cumplen con el requisito
    cancion1 = random.choice(id_list)
    id_list.remove(cancion1)
    entregar_id.append(cancion1)
    cancion2 = random.choice(id_list)
    id_list.remove(cancion2)
    entregar_id.append(cancion2)
    cancion3 = random.choice(id_list)
    id_list.remove(cancion3)
    entregar_id.append(cancion3)
    cancion4 = random.choice(id_list)
    id_list.remove(cancion4)
    entregar_id.append(cancion4)
    cancion5 = random.choice(id_list)
    id_list.remove(cancion5)
    entregar_id.append(cancion5)
    return (entregar_id,tracks)

def musica_estudiar(valor_min_instrumentalness,valor_max_instrumentalness,valor_min_tempo,valor_max_tempo,mapa):
    lst = om.valueSet(mapa["context"]) #saca todos los valores de context en una lista
    p=0 # centinela para recorrer lst
    artistas= [] # se creo una lista nueva para almacenar los artistas
    respuesta_canciones=[] #almacena los id_track , el tempo y el instrumentalness
    entregar =[]
    while p < lt.size(lst): #recorrecomos los diccionarios dentro de lst
        x=lt.getElement(lst,p)
        if (x["instrumentalness"] >= valor_min_instrumentalness) and (x["instrumentalness"] <= valor_max_instrumentalness):
            if (x["tempo"] >= valor_min_tempo) and (x["tempo"] <= valor_max_tempo):
                if x["track_id"] not in artistas:
                    agregar = []
                    artistas.append(x["track_id"]) #en caso de que el id del artista no este en la lista lo agrega
                    agregar.append(x["track_id"])
                    agregar.append(x["instrumentalness"])
                    agregar.append(x["tempo"])
                    respuesta_canciones.append(agregar)
        p+=1

    #selecciona 3 canciones al azar que cumplan con las condiciones
    cancion1 = random.choice(respuesta_canciones)
    respuesta_canciones.remove(cancion1)
    entregar.append(cancion1)

    cancion2 = random.choice(respuesta_canciones)
    respuesta_canciones.remove(cancion2)
    entregar.append(cancion2)

    cancion3 = random.choice(respuesta_canciones)
    respuesta_canciones.remove(cancion3)
    entregar.append(cancion3)

    return(entregar,len(artistas))

def encontrar_genero(lista_genero,centinela,generos_usuario,mapa):
    lst = om.valueSet(mapa["context"]) #saca todos los valores de context en una lista
    p=0
    artistas = {}
    generos = {}
    diccionario_generos={"Reggae":[60,90],"Down-tempo":[70,100],"Chill-out":[90,120],"Hip-hop":[85,115],"Jazz and Funk":[120,125],"Pop":[100,130],"R&B":[60,70],"Rock":[110,140],"Metal":[100,160]}
    if int(centinela) == 1:
        for i in generos_usuario:
            diccionario_generos[i]=generos_usuario[i]
    while p < lt.size(lst): #recorrecomos los diccionarios dentro de lst
        x=lt.getElement(lst,p)
        for u in lista_genero:
            if u in diccionario_generos:
                tempo = diccionario_generos[u]
                tempo_min = tempo[0]
                tempo_max = tempo[1]
                if (float(x["tempo"]) >= float(tempo_min)) and (float(x["tempo"]) <= float(tempo_max)):
                    if u not in generos:
                        artista_id = []
                        artista_id.append(x["artist_id"])
                        generos[u]=artista_id
                    else:
                        lista_x = generos[u]
                        if x["artist_id"] not in lista_x:
                            lista_x.append(x["artist_id"])
                            generos[u]=lista_x
        p+=1

    return generos
    
def saber_tempo_genero(genero):
    diccionario_generos={"Reggae":[60,90],"Down-tempo":[70,100],"Chill-out":[90,120],"Hip-hop":[85,115],"Jazz and Funk":[120,125],"Pop":[100,130],"R&B":[60,70],"Rock":[110,140],"Metal":[100,160]}
    respuesta=["genero propio","genero propio"]
    if genero in diccionario_generos:
        respuesta=diccionario_generos[genero]
    return respuesta

def por_horas(mapa,hora_min,hora_max):
    p=0
    lst = om.valueSet(mapa["context"]) #saca todos los valores de context en una lista
    o=0
    y=len(hora_min)
    g=len(hora_max)
    if len(hora_min) != 6:
        while y=len(hora_min) < 7:
            o+=1
            hora_min+= "0"
            y+=1

    #while p < lt.size(lst): #recorrecomos los diccionarios dentro de lst
    #    x=lt.getElement(lst,p) #contiene un diccionario
    #    k=x["created_at"])
    #    j=k.split(' ')
    #    o=j[1].split(':')
    #    centinela=""
    #    for i in o:
    #        centinela+=i

    #    p+=1
# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareOffenses(offense1, offense2):
    
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1


# Funciones de ordenamiento
