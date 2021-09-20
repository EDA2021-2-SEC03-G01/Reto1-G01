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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from datetime import date
from statistics import mode 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos,
otra para las categorias de los mismos.
"""

# Construccion de modelos
def newCatalog(tipo_artistas, tipo_obras):
    catalog={"artists":None,"artworks":None}
    if tipo_artistas == 1:
        tipo_artistas = "ARRAY_LIST"
    else:
        tipo_artistas = "LINKED_LIST"

    if tipo_obras == 1:
        tipo_obras = "ARRAY_LIST"
    else:
        tipo_obras = "LINKED_LIST"

    catalog["artists"]=lt.newList(datastructure = tipo_artistas, cmpfunction = compareArtists)
    catalog["artworks"]=lt.newList(datastructure = tipo_obras, cmpfunction = compareArtworks)
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

#Artists
def compareArtists (artista1, artista2):
    if artista1["DisplayName"] < artista2["DisplayName"]:
        return -1
    elif artista1["DisplayName"] > artista2["DisplayName"]:
        return 1
    else:
        return 0

def compareYears(artista1, artista2):
    if (int(artista1["Fecha de nacimiento"]) <= int(artista2["Fecha de nacimiento"])):
        return True
    else:
        return False

#Artworks
def compareArtworks(obra1, obra2):
    if obra1["ObjectID"] < obra2["ObjectID"]:
        return -1
    elif obra1["ObjectID"] > obra2["ObjectID"]:
        return 1
    else:
        return 0

def compareDateAcquired(obra1, obra2):
    if (date.fromisoformat(obra1["Adquisicion"]) <= date.fromisoformat(obra2["Adquisicion"])):
        return True
    else:
        return False

# Funciones de ordenamiento

def sortArtists(catalog, tipo_ord):
    return tipo_ord.sort(catalog['artists'], compareYears)

def sortArtworks(catalog):
    return sa.sort(catalog['artworks'], compareDateAcquired)

# Requerimientos 

def req_1(catalog, año_in, año_fin, tipo_ord):
    lista = lt.newList()
    total = 0
    artistas = catalog["artists"]
    for i in range(1, lt.size(artistas)+1) :
    
        artista = lt.getElement(artistas, i)
        if int(artista["BeginDate"]) > int(año_in) and int(artista["BeginDate"]) < int(año_fin):
            dic_artist = {"nombre": artista["DisplayName"], "Fecha de nacimiento": artista["BeginDate"], 
            "Fecha de fallecimiento": artista["EndDate"],  "Nacionalidad": artista["Nationality"],  "Genero": artista["Gender"] }
            lt.addLast(lista, dic_artist)
            total += 1
    #Medir tiempos
    if tipo_ord == 1:
        start_time = time.process_time()
        lista = sa.sort(lista, compareYears)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif tipo_ord == 2:
        start_time = time.process_time()
        lista = ins.sort(lista, compareYears)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif tipo_ord == 3:
        start_time = time.process_time()
        lista = ms.sort(lista, compareYears)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    else:
        start_time = time.process_time()
        lista = qs.sort(lista, compareYears)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    #Primeros y últimos tres
    lista_def = lt.newList()
    for pos in range(1, 4):
        artista = lt.getElement(lista, pos)
        lt.addLast(lista_def, artista)
    largoLista = int(lt.size(lista))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(lista, pos)
            lt.addLast(lista_def, artista)
    return (total, elapsed_time_mseg, lista_def)


#Encontrar los nombres de los autores
def nombres_autores(artistas, obra):
    autores = lt.newList(datastructure="ARRAY_LIST")
    idprueba = ""
    cadena = str(obra["ConstituentID"])
    for j in range(1, len(cadena)):
        if cadena[j] != "[" and cadena[j] != "," and cadena[j] != " " and cadena[j] != "]":
            idprueba += cadena[j]
        elif cadena[j] == "," or cadena[j] == "]":
            seguir = True
            while seguir:
                for i in range(1, lt.size(artistas)+1):
                    autor = lt.getElement(artistas, i)
                    if int(idprueba) == int(autor["ConstituentID"]):
                        lt.addLast(autores, autor["DisplayName"])
                        seguir = False
            idprueba = ""
    return autores
        
def req_2(catalog, fecha_in, fecha_fin, tipo_ord):
    lista = lt.newList(datastructure="ARRAY_LIST")
    total = 0
    purchase = 0
    obras = catalog["artworks"]
    artistas = catalog["artists"]
    for i in range(1, lt.size(obras)+1) :
        obra = lt.getElement(obras, i)
        if obra["DateAcquired"] != "":
            fecha_adq = date.fromisoformat(obra["DateAcquired"])
        else:
            fecha_adq = date.fromisoformat("0001-01-01")
        fecha_ini = date.fromisoformat(fecha_in)
        fecha_final = date.fromisoformat(fecha_fin)
        autores = lt.newList(datastructure="ARRAY_LIST")
        if fecha_adq > fecha_ini and fecha_adq < fecha_final:
            #Encontrar los nombres de los autores
            autores = nombres_autores(artistas, obra)
            #Crear el diccionario
            dic_artwork = {"Titulo": obra["Title"], "Artistas": autores, "Fecha": obra["Date"], "Medio": obra["Medium"],  "Dimensiones": obra["Dimensions"], "Adquisicion": obra["DateAcquired"]  }
            lt.addLast(lista, dic_artwork)
            total += 1
            if obra["CreditLine"] == "Purchase":
                purchase += 1       
    #Medir tiempos
    if tipo_ord == 1:
        start_time = time.process_time()
        lista = sa.sort(lista, compareDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif tipo_ord == 2:
        start_time = time.process_time()
        lista = ins.sort(lista, compareDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif tipo_ord == 3:
        start_time = time.process_time()
        lista = ms.sort(lista, compareDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    else:
        start_time = time.process_time()
        lista = qs.sort(lista, compareDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    #Primeras y últimas tres
    lista_def = lt.newList()
    for pos in range(1, 4):
        artista = lt.getElement(lista, pos)
        lt.addLast(lista_def, artista)
    largoLista = int(lt.size(lista))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(lista, pos)
            lt.addLast(lista_def, artista)
    return (total, purchase, elapsed_time_mseg, lista_def)


def req_3(catalog, nom_artista):
    artista=nom_artista
    lista=lt.newList()
    obras_tecnica = lt.newList(datastructure="ARRAY_LIST")
    total_obras = 0
    total_tecnicas = 0
    mas_utilizada = ""
    obras = catalog["artworks"]
    artistas = catalog["artists"]
    for i in range(1, lt.size(obras)+1) :
        obra = lt.getElement(obras, i)
        idprueba=""
        cadena = str(obra["ConstituentID"])
        autores = lt.newList(datastructure="ARRAY_LIST")
        for j in range(1, len(cadena)):
            if cadena[j] != "[" and cadena[j] != "," and cadena[j] != " " and cadena[j] != "]":
                idprueba += cadena[j]
            elif cadena[j] == "," or cadena[j] == "]":
                seguir = True
                while seguir:
                    for i in range(1, lt.size(artistas)+1):
                        autor = lt.getElement(artistas, i)
                        if idprueba == autor["ConstituentID"]:
                            lt.addLast(autores, autor["DisplayName"])
                            seguir = False
                    idprueba = ""
        dic_artworks = {"Titulo": obra["Title"], "Artistas": autores, "Fecha": obra["Date"], "Medio": obra["Medium"],  "Dimensiones": obra["Dimensions"], "Adquisicion": obra["DateAcquired"]  }
        lt.addLast(lista, dic_artworks)
    for k in range(1,lt.size(lista)+1):
        for l in range(1,lt.size((lista[k]["Artistas"])+1)):
            if lista[k]["Artistas"][l] == artista:
                total_obras=+1
                lista_tecnicas=lt.newList()
                lt.addLast(lista_tecnicas, lista[k]["Medio"])
    mas_utilizada=mode(lista_tecnicas)
    for m in range(1,lt.size(lista_tecnicas)+1):
        lista_tecnicas_def=lt.newList()
        if lista_tecnicas[m] not in lista_tecnicas_def:
            lt.addLast(lista_tecnicas_def,lista_tecnicas[m])
            total_tecnicas=+1
    lista_obras=lt.newList()
    for n in range(1, lt.size(lista)+1):
        if artista in lista[n]["Artistas"] and lista[n]["Medio"]==mas_utilizada:
            dic_obra={"Titulo": lista[n]["Titulo"], "Fecha": lista[n]["Fecha"], "Medio": lista[n]["Medio"], "Dimensiones": lista[n]["Dimensiones"]}
            lt.addLast(lista_obras, dic_obra)
    return (total_obras, total_tecnicas, mas_utilizada, lista_obras)

#Encontrar las nacionalidades de los autores
def nac_autores(artistas, obra):
    autores = lt.newList(datastructure="ARRAY_LIST")
    idprueba = ""
    cadena = str(obra["ConstituentID"])
    for j in range(1, len(cadena)):
        if cadena[j] != "[" and cadena[j] != "," and cadena[j] != " " and cadena[j] != "]":
            idprueba += cadena[j]
        elif cadena[j] == "," or cadena[j] == "]":
            seguir = True
            while seguir:
                for i in range(1, lt.size(artistas)+1):
                    autor = lt.getElement(artistas, i)
                    if int(idprueba) == int(autor["ConstituentID"]):
                        lt.addLast(autores, autor["Nationality"])
                        seguir = False
            idprueba = ""
    return autores

def req_4(catalog):
    obras = catalog["artworks"]
    artistas = catalog["artists"]
    solo_nac = lt.newList(datastructure="ARRAY_LIST")
    obras_nac_mas = lt.newList(datastructure="ARRAY_LIST")
    dic_nac = {}
    for o in range(1, lt.size(obras)+1):
        obra = lt.getElement(obras, o)
        idprueba = ""
        cadena = str(obra["ConstituentID"])
        for j in range(1, len(cadena)):
            if cadena[j] != "[" and cadena[j] != "," and cadena[j] != " " and cadena[j] != "]":
                idprueba += cadena[j]
            elif cadena[j] == "," or cadena[j] == "]":
                seguir = True
                while seguir:
                    for a in range(1, lt.size(artistas)+1):
                        autor = lt.getElement(artistas, a)
                        if int(idprueba) == int(autor["ConstituentID"]):
                            seguir = False
                            if lt.isPresent(solo_nac, autor["Nationality"]) == 0:
                                nacionalidad = autor["Nationality"]
                                lt.addLast(solo_nac, nacionalidad)
                                dic_nac[nacionalidad] = 1
                                if autor["Nationality"] == "":
                                    dic_nac["Nationality unknown"] += 1
                            else:
                                if autor["Nationality"] == "":
                                    dic_nac["Nationality unknown"] += 1
                                else:
                                    dic_nac[autor["Nationality"]] += 1
                idprueba = ""
    sorted_values = sorted(dic_nac.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in dic_nac.keys():
            if dic_nac[k] == i:
                if  len(sorted_dict) < 10:
                    sorted_dict[k] = dic_nac[k]
                else:
                    break
    nac_mas = list(sorted_dict.keys())[0]
    for o in range(1, lt.size(obras)+1):
        obra = lt.getElement(obras, o)
        nacionalidades = nac_autores(artistas, obra)
        if lt.isPresent(nacionalidades, nac_mas) != 0:
            lt.addLast(obras_nac_mas, obra)
    n_obras_nac_mas = lt.size(obras_nac_mas)
    #Primeras y últimas tres
    lista_def = lt.newList()
    for pos in range(1, 4):
        artista = lt.getElement(obras_nac_mas, pos)
        lt.addLast(lista_def, artista)
    largoLista = int(lt.size(obras_nac_mas))
    for pos in range(1, largoLista + 1):
        if (largoLista - pos) < 3:
            artista = lt.getElement(obras_nac_mas, pos)
            lt.addLast(lista_def, artista)
    return (sorted_dict, lista_def, nac_mas, n_obras_nac_mas)
