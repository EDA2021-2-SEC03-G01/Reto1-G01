﻿"""
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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar cronológicamente los artistas")
    print("3- Ordenar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por su técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("0- Salir")

def initCatalog(tipo_artistas, tipo_obras):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo_artistas, tipo_obras)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1: 
        print("1 - ARRAY LIST \n2 - LINKED_LIST")
        tipo_artistas = int(input("Seleccione el tipo de representacion de la lista de artistas: "))
        tipo_obras = int(input("Seleccione el tipo de representacion de la lista de obras: "))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo_artistas, tipo_obras)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Últimos tres artistas:\n' + str(controller.getLastArtists(catalog)))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Últimas tres obras:\n' + str(controller.getLastArtworks(catalog)))

    elif int(inputs[0]) == 2:
        print("Tipos de algoritmos de ordenamiento iterativo:\n1- Shell\n2- Insertion\n3- Merge\n4- Quick")
        tipo_ord = int(input("Seleccione el tipo ordenamiento: "))
        año_in = int(input("Ingrese el año inicial: "))
        año_fin = int(input("Ingrese el año final: "))
        (total, elapsed_time_mseg, artistas) = controller.req_1(catalog, año_in, año_fin, tipo_ord)
        print("Para mostrar estos datos el tiempo (mseg) fue: " + str(elapsed_time_mseg))
        print("Hay " + str(total) + " artistas entre " + str(año_in) + " y " + str(año_fin))
        print("A continuación se muestran los primeros y ultimos tres: ")
        print(artistas)

    elif int(inputs[0]) == 3:
        print("Tipos de algoritmos de ordenamiento iterativo:\n1- Shell\n2- Insertion\n3- Merge\n4- Quick")
        tipo_ord = int(input("Seleccione el tipo ordenamiento: "))
        fecha_in = (input("Ingrese la fecha inicial (YYYY-MM-DD): "))
        fecha_fin = (input("Ingrese la fecha final (YYYY-MM-DD): "))
        (total, purchase, elapsed_time_mseg, obras) = controller.req_2(catalog, fecha_in, fecha_fin, tipo_ord)
        print("Para mostrar estos datos el tiempo (mseg) fue: " + str(elapsed_time_mseg))
        print("Fueron adquiridas " + str(total) + " obras entre " + str(fecha_in) + " y " + str(fecha_fin))
        print(str(purchase) + " de estas fueron compradas. ")
        print("A continuación se muestran las primeras y ultimas tres: ")
        print(obras)

    elif int(inputs[0]) == 4:
        artista=input("Ingrese el nombre del artista de interés:  ")
        (total_obras, total_tecnicas, mas_utilizada, lista_obras) = controller.req_3(catalog, artista)
        print(artista + " tiene un total de " + total_obras + " en el museo.")
        print("Hay " + total_tecnicas + " tipos diferentes de medios/tecnicas en su colección.")
        print("Su tecnica mas utilizada es " + mas_utilizada)
        print("A continuación se muestran las obras en las que " + artista + "utilizó esta tecnica")
        print(lista_obras)

    else:
        sys.exit(0)
sys.exit(0)

