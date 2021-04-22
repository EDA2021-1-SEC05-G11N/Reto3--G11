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
    mapa = analyzer["context"]
    track_id = context["track_id"]
    om.put(mapa,track_id,context)

def agregaruser_trackfile(analyzer,track):
    mapa= analyzer["user_track"]
    user_id = track["user_id"]
    om.put(mapa,user_id,track)
    

    





# Funciones para creacion de datos

# Funciones de consulta

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
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1


# Funciones de ordenamiento
