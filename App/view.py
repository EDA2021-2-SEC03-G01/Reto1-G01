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
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")
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
        (total, elapsed_time_mseg, tiempo_req, artistas) = controller.req_1(catalog, año_in, año_fin, tipo_ord)
        print("Para mostrar estos datos el tiempo (mseg) fue: " + str(elapsed_time_mseg))
        print("Hay " + str(total) + " artistas entre " + str(año_in) + " y " + str(año_fin))
        print("A continuación se muestran los primeros y ultimos tres: ")
        print(artistas)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))

    elif int(inputs[0]) == 3:
        print("Tipos de algoritmos de ordenamiento iterativo:\n1- Shell\n2- Insertion\n3- Merge\n4- Quick")
        tipo_ord = int(input("Seleccione el tipo ordenamiento: "))
        fecha_in = (input("Ingrese la fecha inicial (YYYY-MM-DD): "))
        fecha_fin = (input("Ingrese la fecha final (YYYY-MM-DD): "))
        (total, purchase, elapsed_time_mseg, tiempo_req, obras) = controller.req_2(catalog, fecha_in, fecha_fin, tipo_ord)
        print("Para mostrar estos datos el tiempo (mseg) fue: " + str(elapsed_time_mseg))
        print("Fueron adquiridas " + str(total) + " obras entre " + str(fecha_in) + " y " + str(fecha_fin))
        print(str(purchase) + " de estas fueron compradas. ")
        print("A continuación se muestran las primeras y ultimas tres: ")
        print(obras)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))

    elif int(inputs[0]) == 4:
        artista=input("Ingrese el nombre del artista de interés:  ")
        (total_obras, total_tecnicas, mas_utilizada, tiempo_req, lista_obras) = controller.req_3(catalog, artista)
        print(artista + " tiene un total de " + total_obras + " en el museo.")
        print("Hay " + total_tecnicas + " tipos diferentes de medios/tecnicas en su colección.")
        print("Su tecnica mas utilizada es " + mas_utilizada)
        print("A continuación se muestran las obras en las que " + artista + "utilizó esta tecnica")
        print(lista_obras)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))

    elif int(inputs[0]) == 5:
        (sorted_dict, lista_def, nac_mas, tiempo_req, n_obras_nac_mas) = controller.req_4(catalog)
        print("El Top 10 de nacionalidades en el MoMA es: " + str(sorted_dict))
        print("La nacionalidad más frecuente en el MoMA es " + (nac_mas) + " con " + str(n_obras_nac_mas) + " obras.")
        print("A continuación se muestran las primeras y ultimas tres: ")
        print(lista_def)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))
    
    elif int(inputs[0]) == 6:
        dep = input("Ingrese el departamento del que desea transportar las obras: ")
        (total_obras, costo_tot, peso_tot, lista_transp_def, tiempo_req, obras_costos_def) = controller.req_5(catalog, dep)
        print("El costo por transportar las obras del departamento " + dep + " fue: " + str(costo_tot))
        print("El numero total de obras por transportar es " + str(total_obras))
        print("El peso total de las obras es de: " + str(peso_tot))
        print("Las cinco obras más antiguas por transportar son: ")
        for obra in lt.iterator(lista_transp_def):
            print(obra)
        print("Las cinco obras más costosas por transportar son: ")
        for obra in lt.iterator(obras_costos_def):
            print(obra)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))
    
    elif int(inputs[0]) == 7:
        ano_ini=input("Ingrese el año inicial de su busqueda: ")
        ano_fin=input("Ingrese el año final de su busqueda: ")
        Area_disp=input("Ingrese el area disponible: ")
        (tot_obras_anos, tot_obras, Area_usada, tiempo_req, prim_ult_5)= controller.req_6(catalog, ano_ini, ano_fin, Area_disp)
        print("El MoMA va a exhibir obras desde " + str(ano_ini) + " hasta " + str(ano_fin))
        print("Hay " + str(tot_obras_anos) + " obras posibles en un area de " + str(Area_disp) + " m^2")
        print("De las cuales " + str(tot_obras) + " fue posible ubicarlas")
        print("Llenando " + str(Area_usada) + " m^2")
        print("A continuación las primeras y ultimas 5 obras ubicadas en este area")
        for obra in lt.iterator(prim_ult_5):
            print(obra)
        print("El tiempo de respuesta para este requerimiento fue: " + str(tiempo_req))

    else:
        sys.exit(0)
sys.exit(0)

#Drawings & Prints
