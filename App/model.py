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
    catalog["artists"]=lt.newList()
    catalog["artworks"]=lt.newList()
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    lt.addLast(catalog["artists"], artist)
    
def addArtworks(catalog, artwork):
    lt.addLast(catalog["artworks"], artwork)

# Funciones para creacion de datos
def newArtist(nombre, nac, gen, año_nac, año_def, wiki, ulan):
    artist={
        "nombre":nombre,
        "nacionalidad":nac,
        "genero":gen,
        "año de nacimiento":año_nac,
        "año de defuncion":año_def, 
        "Wiki QID":wiki, 
        "Ulan ID":ulan
        }
    return artist

def newArtwork(tit, art, fecha_cre, medio, dim, fecha_adq, credit, acc, clas, dep, cat, url, circ, prof, diam, alt, larg, ancho, peso):
    artwork={
        "titulo":tit,
        "artista":art,
        "fecha de creacion":fecha_cre,
        "medio":medio,
        "dimension":dim,
        "fecha de adquisicion":fecha_adq,
        "credit line":credit,
        "numero de acceso":acc,
        "clasificacion":clas,
        "departamento":dep,
        "Catalogado":cat,
        "url":url,
        "Circunferencia":circ,
        "profundidad":prof,
        "diametro":diam,
        "altura":alt,
        "largo":larg,
        "ancho":ancho,
        "peso":peso
        }
    return artwork

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
    
def compareYears(artista1, artista2):
    return (int(artista1['año de nacimiento']) < int(artista2['año de nacimiento']))

# Funciones de ordenamiento

def sortArtists(catalog):
    return sa.sort(catalog['artists'], compareYears)

# Requerimientos 

def req_1(catalog, año_in, año_fin):
    lista = lt.newList()
    total = 0
    artistas = sortArtists(catalog)
    for artista in artistas:
        if artista["año de nacimiento"] > año_in and artista["año de nacimiento"] < año_fin:
            dic_artist = {"nombre": artista["nombre"], "año de nacimiento": artista["año de nacimiento"],  "nacionalidad": artista["nacionalidad"],  "genero": artista["genero"] }
            lt.addLast(lista, dic_artist)
            total += 1
    lista_def = lt.newList()
    lt.addLast(lista_def, total)
    lt.addLast(lista_def, lt.getElement(lista, 1))
    lt.addLast(lista_def, lt.getElement(lista, 2))
    lt.addLast(lista_def, lt.getElement(lista, 3))
    lt.addLast(lista_def, lt.getElement(lista, -3))
    lt.addLast(lista_def, lt.getElement(lista, -2))
    lt.addLast(lista_def, lt.getElement(lista, -1))
    return lista_def