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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def iniciar():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el model
    p = model.newAnalyzer()
    return p
# Funciones para la carga de datos
def loadData(analyzer, context,sentiment,user_track):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    user_trackfile = cf.data_dir + user_track
    contextfile= cf.data_dir + context
    sentimentfile =  cf.data_dir + sentiment

    input_file_user_trackfile = csv.DictReader(open(user_trackfile, encoding="utf-8"),
                                delimiter=",")
    input_file_contextfile = csv.DictReader(open(contextfile, encoding="utf-8"),
                                delimiter=",")
    input_file_sentimentfile = csv.DictReader(open(sentimentfile, encoding="utf-8"),
                                delimiter=",")

    for songs in input_file_sentimentfile:
        loadsentimentfile(analyzer,songs)
    for songs in input_file_contextfile:
        loadcontextfile(analyzer,songs)
    for songs in input_file_user_trackfile:
        loaduser_trackfile(analyzer,songs)
        
        
    return analyzer


def loadsentimentfile(mapa, sentiment):
    model.agregarsentimentfile(mapa,sentiment)
def loadcontextfile(mapa,context):
    model.agregarcontextfile(mapa,context)
def loaduser_trackfile(mapa,track):
    model.agregaruser_trackfile(mapa,track)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def artistSize(analyzer):
    """
    Numero de artistas leidos
    """
    return model.artistSize(analyzer)

def registroSize(analyzer):
    return model.registroSize(analyzer)

def tracksize(analyzer):
    return model.tracksize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)

def caracterizar(caracteristica,valor_minimo,valor_maximo,mapa):
    return model.caracterizar(caracteristica,valor_minimo,valor_maximo,mapa)

def musica_festejar(valor_min_energy,valor_max_energy,valor_min_Danceability,valor_max_Danceability,mapa):
    return model.musica_festejar(valor_min_energy,valor_max_energy,valor_min_Danceability,valor_max_Danceability,mapa)
def musica_estudiar(valor_min_instrumentalness,valor_max_instrumentalness,valor_min_tempo,valor_max_tempo,mapa):
    return model.musica_estudiar(valor_min_instrumentalness,valor_max_instrumentalness,valor_min_tempo,valor_max_tempo,mapa)
def encontrar_genero(lista_genero,centinela,generos_usuario,mapa):
    return model.encontrar_genero(lista_genero,centinela,generos_usuario,mapa)
def saber_tempo_genero(genero):
    return model.saber_tempo_genero(genero)