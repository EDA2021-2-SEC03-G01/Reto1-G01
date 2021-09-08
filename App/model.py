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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog={"artists":None,"artworks":None}
    catalog["artists"]=lt.newList(cmpfunction=compareArtists)
    catalog["artworks"]=lt.newList()
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    lt.addLast(catalog["artists"], artist)
    
def addArtworks(catalog, artwork):
    lt.addLast(catalog["artworks"], artwork)

# Funciones para creacion de datos


# Funciones de consulta

def getFirstArtists (catalog):
    primeros = lt.newList()
    for pos in range(1, 3):
        artista = lt.getElement(catalog["artists"], pos)
        lt.addLast(primeros, artista)

    return primeros

def getLastArtists (catalog):
    ultimos = lt.newList()
    largoLista = int(lt.size(catalog["artists"]))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(catalog["artists"], pos)
            lt.addLast(ultimos, artista)

    return ultimos

def getLastArtworks (catalog):
    ultimos = lt.newList()
    largoLista = int(lt.size(catalog["artworks"]))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(catalog["artworks"], pos)
            lt.addLast(ultimos, artista)

    return ultimos

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtists (artista1, artista2):
    if artista1["DisplayName"] < artista2["DisplayName"]:
        return -1
    elif artista1["DisplayName"] > artista2["DisplayName"]:
        return 1
    else:
        return 0

def compareYears(artista1, artista2):
    if (int(artista1['BeginDate']) <= int(artista2['BeginDate'])):
        return True
    else:
        return False

# Funciones de ordenamiento

def sortArtists(catalog):
    return sa.sort(catalog['artists'], compareYears)


# Requerimientos 

def req_1(catalog, año_in, año_fin):
    print("hola")
    lista = lt.newList()
    total = 0
    artistas = sortArtists(catalog)
    print("hola.2")
    for artista in artistas:
        print("hola.3")
        if int(artista["BeginDate"]) > int(año_in) and int(artista["BeginDate"]) < int(año_fin):
            dic_artist = {"DisplayName": artista["DisplayName"], "BeginDate": artista["BeginDate"],  "Nationality": artista["Nationality"],  "Gender": artista["Gender"] }
            lt.addLast(lista, dic_artist)
            total += 1
    lista_def = lt.newList()
    lt.addLast(lista_def, total)
    for pos in range(1, 3):
        artista = lt.getElement(lista, pos)
        lt.addLast(lista_def, artista)
    largoLista = int(lt.size(lista))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(lista, pos)
            lt.addLast(lista_def, artista)
    return lista_def
