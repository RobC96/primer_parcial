import os
from datetime import datetime
import json


PATH = 'Proyectos.csv'
PATH_JSON = 'ProyectosFinalizados.json'


def obtener_id():
    with open(PATH, 'r') as file:
        lineas = file.readlines()
        id = lineas[len(lineas) - 1].split(',')[0]
    return int(id)

id_auto_incremental = obtener_id()

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1

def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1



def analizar_proyectos_activos(proyectos: list[dict]) -> int:
    '''
    Esta función recorre la lista de diccionarios y retorna la cantidad de proyectos activos
    '''
    proyectos_activos = 0

    for proyecto in proyectos:
        if proyecto['estado'].capitalize() == 'Activo':
            proyectos_activos += 1

    return proyectos_activos



def limite_de_proyectos(limite_activos: int, proyectos: list[dict]):
    '''
    Analiza la cantidad de proyectos activos para que no supere el límite, retorna False si el límite es superado
    '''
    cantidad_de_activos = analizar_proyectos_activos(proyectos)
    estado = True
    if cantidad_de_activos > limite_activos:
        estado = False

    return estado



_b_red: str = '\033[41m'
_b_green: str = '\033[42m'
_b_blue: str = '\033[44m'
_f_white: str = '\033[37m'
_no_color: str = '\033[0m'

def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    This function prints a message with a specified type (error, success, or info) in a colored format.
    
    :param mensaje: a string containing the message to be printed
    :type mensaje: str
    :param tipo_mensaje: The parameter "tipo_mensaje" is a string that represents the type of message
    that will be printed. It can be "Error", "Success", or "Info"
    :type tipo_mensaje: str
    """
    tipo_mensaje = tipo_mensaje.strip().capitalize()
    match tipo_mensaje:
        case 'Error':
            print(f'{_b_red}{_f_white}> Error: {mensaje}{_no_color}')
        case 'Success':
            print(f'{_b_green}{_f_white}> Success: {mensaje}{_no_color}')
        case 'Info':
            print(f'{_b_blue}{_f_white}> Information: {mensaje}{_no_color}')



def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input('Presione una tecla para continuar...')
    if os.name in ['ce', 'nt', 'dos']: os.system("cls")
    else: os.system("clear")



def obtener_nombre() -> str:
    '''
    Esta función recibe un string y valida que sea un nombre que cumpla con los requisitos
    (No puede exceder los 30 caracteres ni contener números o caracteres especiales)
    '''
    bandera = False

    while True:
        nombre = input("Ingrese el nombre del proyecto: ")
        if len(nombre) > 30:
            imprimir_mensaje('El nombre no debe superar los 30 caracteres', 'Error')
            continue

        lista_palabras = nombre.split(' ')

        for palabra in lista_palabras:
            if palabra.isalpha() != True:
                imprimir_mensaje('Debe ingresar un nombre compuesto solamente por caracteres alfabéticos', 'Error')
                bandera = False
                break
            else:
                bandera = True

        if bandera:
            imprimir_mensaje('Nombre agregado con éxito', 'Success')
            break

    return nombre.capitalize()



def obtener_descripcion() -> str:
    '''
    Esta funcion recibe un string y valida que sea una descripcion que cumpla con los requisitos
    \n(No puede exceder los 200 caracteres y debe ser alfanumérico)
    '''
    bandera = False

    while True:
        descripcion = input("Ingrese la descripcion de su proyecto: ")
        if len(descripcion) > 200:
            imprimir_mensaje('La descripción de su proyecto no puede superar los 200 caracteres', 'Error')
            continue

        lista_palabras = descripcion.split(' ')

        for palabra in lista_palabras:
            if palabra.isalnum() != True:
                imprimir_mensaje('Debe ingresar una descripción compuesta solo por caracteres alfanuméricos', 'Error')
                bandera = False
                break
            else:
                bandera = True

        if bandera:
            imprimir_mensaje('Descripción agregada con éxito', 'Success')
            break

    return descripcion.capitalize()



def obtener_presupuesto() -> int:
    '''
    Esta funcion recibe un string y valida que sea un presupuesto válido 
    \n(Un número no menor a 500000)
    '''

    while True:
        presupuesto = input("Ingrese el presupuesto de su proyecto: ")
        if presupuesto.isdigit() != True:
            imprimir_mensaje('Asegúrese de ingresar un número válido', 'Error')
        elif int(presupuesto) < 500000:
            imprimir_mensaje('El presupuesto no puede ser menor a 500k', 'Error')
        else:
            imprimir_mensaje('Presupuesto agregado correctamente', 'Success')
            break

    return int(presupuesto)



def obtener_fecha_inicio():

    while True:
        fecha_inicio_str = input("Ingrese la fecha de inicio del proyecto con el siguiente formato: DD-MM-AAAA: ")

        try:
            fecha_inicio_formateada = datetime.strptime(fecha_inicio_str, '%d-%m-%Y')
            break

        except ValueError:
            imprimir_mensaje('Por favor, ingrese la fecha en el formato correcto (DD-MM-AAAA): ', 'Info')

    return fecha_inicio_formateada



def obtener_fecha_fin():

    while True:
        fecha_fin_str = input("Ingrese la fecha de fin del proyecto con el siguiente formato: DD-MM-AAAA: ")

        try:
            fecha_fin_formateada = datetime.strptime(fecha_fin_str, '%d-%m-%Y')
            break

        except ValueError:
            imprimir_mensaje('Por favor, ingrese la fecha en el formato correcto (DD-MM-AAAA): ', 'Info')

    return fecha_fin_formateada



def validar_fecha_inicio_fin(fecha_inicio, fecha_fin):
    '''
    Esta funcion recibe dos fechas (inicio y fin), se asegura de que sean fechas válidas y que la fecha de fin no sea menor a la de inicio
    '''

    if fecha_inicio > fecha_fin:
        imprimir_mensaje('La fecha de inicio no puede ser posterior a la de fin', 'Error')
        validacion = False
    else:
        imprimir_mensaje('Fecha agregada correctamente', 'Success')
        validacion = True

    return validacion



def obtener_estado():
    '''
    Esta función solicita un estado y valida que este sea una de las opciones disponibles
    '''
    estados_posibles = ['Activo', 'Cancelado', 'Finalizado']

    while True:
        eleccion = input("Ingrese el estado del proyecto: ").capitalize().strip()
        if eleccion not in estados_posibles:
            imprimir_mensaje(f'El estado no se encuentra entre las opciones válidas: {estados_posibles}', 'Error')
        else:
            imprimir_mensaje('Estado asignado con éxito', 'Success')
            break

    return eleccion



def obtener_estado_limitado():
    '''
    Esta función solicita un estado y será llamada cuando se haya alcanzado el limite de Activos, impidiendo seleccionar este mismo.
    '''
    estados_posibles = ['Cancelado', 'Finalizado']

    while True:
        eleccion = input("Ingrese el estado del proyecto: ").capitalize().strip()
        if eleccion not in estados_posibles:
            imprimir_mensaje(f'El estado no se encuentra entre las opciones válidas: {estados_posibles}', 'Error')
        else:
            imprimir_mensaje('Estado asignado con éxito', 'Success')
            break

    return eleccion



def mostrar_proyecto(proyecto: dict):
    '''
    Esta función recibe un diccionario que representa un proyecto y lo imprime
    '''

    print(f"\n{'ID':<3} | {'Nombre':<40} | {'Fecha de inicio':<15} \t| {'Fecha de fin':<15} \t| {'Presupuesto':<15} | {'Estado':<15} |")
    print(f"{proyecto['id']:<3} | {proyecto['nombre']:<40} | {proyecto['fecha_inicio']:<15} \t| {proyecto['fecha_fin']:<15} \t| ${proyecto['presupuesto']:<14} | {proyecto['estado']:<15} | ")
    print(f"\nDescripcion: {proyecto['descripcion']}\n")
    print("\n")
    print("\n")



def agregar_proyecto () -> dict:
    '''
    Esta función recibe y valida todos los datos necesarios para agregar un proyecto
    '''
    proyecto = {}
    incrementar_id()
    nombre_proyecto = obtener_nombre()
    descripcion_proyecto = obtener_descripcion()
    while True:
        fecha_inicio = obtener_fecha_inicio()
        fecha_fin = obtener_fecha_fin()
        if validar_fecha_inicio_fin(fecha_inicio, fecha_fin):
            break
    presupuesto = obtener_presupuesto()
    estado = obtener_estado()

    proyecto['id'] = id_auto_incremental
    proyecto['nombre'] = nombre_proyecto
    proyecto['descripcion'] = descripcion_proyecto
    proyecto['fecha_inicio'] = datetime.strftime(fecha_inicio, '%d-%m-%Y')
    proyecto['fecha_fin'] = datetime.strftime(fecha_fin, '%d-%m-%Y')
    proyecto['presupuesto'] = presupuesto
    proyecto['estado'] = estado

    mostrar_proyecto(proyecto)

    proyecto['fecha_inicio'] = datetime.strptime(proyecto['fecha_inicio'], '%d-%m-%Y')
    proyecto['fecha_fin'] = datetime.strptime(proyecto['fecha_fin'], '%d-%m-%Y')

    while True:
        opcion = input("Desea agregar el proyecto? (S/N): ").upper()
        if opcion == 'S':
            imprimir_mensaje('Proyecto agregado con éxito', 'Success')
            break
        elif opcion == 'N':
            decrementar_id()
            imprimir_mensaje('Proyecto descartado', 'Info')
            return False
        else:
            imprimir_mensaje('Debe ingresar una opción válida', 'Error')

    return proyecto



def agregar_proyecto_memoria (proyectos: list[dict], bandera: bool):
    '''
    Esta función crea un nuevo proyecto y lo carga en la lista trabajada en memoria
    '''
    if bandera:
        nuevo_proyecto = agregar_proyecto()
        proyectos.append(nuevo_proyecto)
    else:
        imprimir_mensaje('Ha superadl el límite de proyectos activos', 'Error')



def cargar_csv_en_memoria(PATH: str) -> list[dict]:
    '''
    Esta función lee un archivo csv y lo carga en memoria como una lista de diccionarios
    '''
    lista_proyectos = []
    with open(PATH, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        for linea in lineas[1:]:
            proyecto = {}
            claves = linea.split(',')
            proyecto['id'] = int(claves[0])
            proyecto['nombre'] = claves[1]
            proyecto['descripcion'] = claves[2]
            proyecto['fecha_inicio'] = datetime.strptime(claves[3], '%d-%m-%Y')
            proyecto['fecha_fin'] = datetime.strptime(claves[4], '%d-%m-%Y')
            proyecto['presupuesto'] = int(claves[5])
            proyecto['estado'] = claves[6].strip()
            lista_proyectos.append(proyecto)

    return lista_proyectos



def agregar_proyectos_csv(proyectos: list[dict]):
    '''
    Esta función reescribe el archivo csv para guardar todos los cambios al cerrar la aplicación
    '''
    claves = proyectos[0].keys()
    encabezado = ''

    for clave in claves:
        encabezado += clave + ','
    encabezado = encabezado.rstrip(',')

    normalizar_fechas_a_strftime(proyectos)

    with open(PATH, 'w', encoding='utf-8') as file:
        file.write(encabezado)
        for proyecto in proyectos:
            linea = '\n'
            for clave in proyecto:
                linea += str(proyecto[clave]) + ','
            linea = linea.rstrip(',')
            file.write(linea)

    normalizar_fechas_a_strptime(proyectos)



def guardar_proyectos_finalizados(proyectos: list[dict]):
    '''
    Al salir de la aplicación, verifica que proyectos están finalizados y los escribe en un json
    '''

    lista_terminados = []

    for proyecto in proyectos:
        if proyecto['estado'] == 'Finalizado':
            lista_terminados.append(proyecto)

    normalizar_fechas_a_strftime(proyectos)

    with open(PATH_JSON, 'w', encoding='utf-8') as file:
        json.dump(lista_terminados, file, ensure_ascii=False, indent=4)

    normalizar_fechas_a_strptime(proyectos)



def encontrar_proyecto(proyectos: list[dict], id: int) -> dict:
    '''
    Esta funcón recibe una lista de diccionarios y devuelve el diccionario que corresponda con el id
    '''
    proyecto_encontrado = {}

    for proyecto in proyectos:
        if proyecto['id'] == id:
            proyecto_encontrado = proyecto
    
    if not proyecto_encontrado:
        imprimir_mensaje('No se encontró el proyecto, verifique su ID', 'Error')
        return
    else:
        imprimir_mensaje('Proyecto encontrado', 'Success')
    
    return proyecto_encontrado



def menu_modificacion(proyecto: dict, bandera: bool) -> bool:
    '''
    Esta función recibe una opción y valida que sea un entero, además recibe bandera para analizar la disponibilidad de estados\n
    bandera: True (Todos permitidos)\n
    bandera: False (Activo no permitido)\n
    Si modificó algún valor, retorna True
    '''
    se_modifico = False

    while True:        
        proyecto['fecha_inicio'] = datetime.strftime(proyecto['fecha_inicio'], '%d-%m-%Y')
        proyecto['fecha_fin'] = datetime.strftime(proyecto['fecha_fin'], '%d-%m-%Y')
        mostrar_proyecto(proyecto)
        proyecto['fecha_inicio'] = datetime.strptime(proyecto['fecha_inicio'], '%d-%m-%Y')
        proyecto['fecha_fin'] = datetime.strptime(proyecto['fecha_fin'], '%d-%m-%Y')
        menu = '''
                1 - Nombre
                2 - Descripción
                3 - Fecha inicio
                4 - Fecha fin
                5 - Presupuesto
                6 - Estado
                7 - Salir
                '''
        print(menu)
        opcion_str = input("Que desea modificar? ")
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            match opcion:
                case 1:
                    proyecto['nombre'] = obtener_nombre()
                    se_modifico = True
                case 2:
                    proyecto['descripcion'] = obtener_descripcion()
                    se_modifico = True
                case 3:
                    proyecto['fecha_inicio'] = obtener_fecha_inicio()
                    se_modifico = True
                case 4:
                    proyecto['fecha_fin'] = obtener_fecha_fin()
                    se_modifico = True
                case 5:
                    proyecto['presupuesto'] = obtener_presupuesto()
                    se_modifico = True
                case 6:
                    if bandera:
                        proyecto['estado'] = obtener_estado()
                    else:
                        proyecto['estado'] = obtener_estado_limitado()
                    se_modifico = True
                case 7:
                    break
                case _:
                    imprimir_mensaje('Ingrese una opción válida', 'Error')
        else:
            imprimir_mensaje('Opción inválida', 'Error')

    return se_modifico



def modificar_proyecto(proyectos: list[dict], bandera: bool):
    '''
    Esta función solicita un id para buscar un proyecto y modificarlo
    '''
    modificar = True

    while modificar:
        if bandera == False:
            imprimir_mensaje('Se alcanzó el límite de proyectos activos, este estado no estará disponible', 'Info')

        id_str = input("Ingrese el id del proyecto que desea modificar: ")
        if id_str.isdigit():
            id = int(id_str)
        else:
            imprimir_mensaje('Ingrese un número válido', 'Error')
            modificar = False
            break

        proyecto = encontrar_proyecto(proyectos, id)
        if proyecto:
            proyecto_modificado = menu_modificacion(proyecto, bandera)
            if proyecto_modificado:
                imprimir_mensaje('Se ha modificado el proyecto con éxito', 'Success')
                normalizar_fechas_a_strftime(proyectos)
                mostrar_proyecto(proyecto)
                normalizar_fechas_a_strptime(proyectos) 

            while True:
                opcion = input("Desea seguir modificando? (S/N): ").upper().strip()
                if opcion == 'S':
                    break
                elif opcion == 'N':
                    modificar = False
                    break
                else:
                    imprimir_mensaje('Opción inválida', 'Error')

        else:
            modificar = False
            break



def cancelar_proyecto(proyectos: list[dict]):
    '''
    Recibe una lista de diccionarios y solicita un id, cambia el valor de 'estado' a 'Cancelado'
    '''
    proyectos_activos = []
    for proyecto in proyectos:
        if proyecto['estado'] == 'Activo':
            proyectos_activos.append(proyecto)

    while True:
        mostrar_todos_los_proyectos(proyectos_activos)
        imprimir_mensaje('Estos son los proyectos activos que puede cancelar', 'Info')
        id_str = input("Ingrese el id del proyecto que desea cancelar: ")
        if id_str.isdigit():
            id = int(id_str)
        else:
            imprimir_mensaje('Ingrese un número válido', 'Error')
            break

        proyecto_a_cancelar = encontrar_proyecto(proyectos_activos, id)

        if proyecto_a_cancelar:
            proyecto_a_cancelar['estado'] = 'Cancelado'
            imprimir_mensaje('El proyecto se ha cancelado con éxito', 'Success')
            break
        else:
            break

    return



def comprobar_fecha_fin(proyectos: list[dict]):
    '''
    Esta función analiza la lista de diccionarios para cambiar el estado de los proyectos cuya fecha de finalización ya haya pasado
    '''
    cambios_realizados = 0
    fecha_hoy = datetime.today()

    for proyecto in proyectos:
        if proyecto['fecha_fin'] < fecha_hoy and proyecto['estado'] == 'Activo':
            cambios_realizados += 1
            proyecto['estado'] = 'Finalizado'

    if cambios_realizados > 0:
        imprimir_mensaje(f'Se encontraron {cambios_realizados} proyectos con estado activo cuya fecha de fin ya pasó', 'Success')
        imprimir_mensaje('Los proyectos encontrados fueron cambiados a Finalizado', 'Info')
    else:
        imprimir_mensaje('No se encontraron proyectos cuya fecha de finalización haya pasado', 'Info')

    return



def mostrar_todos_los_proyectos(proyectos: list[dict]):
    '''
    Muestra todos los proyectos
    '''

    normalizar_fechas_a_strftime(proyectos)

    for proyecto in proyectos:
        mostrar_proyecto(proyecto)

    normalizar_fechas_a_strptime(proyectos)



def calcular_presupuesto_promedio(proyectos: list[dict]):
    '''
    Calcula y muestra el presupuesto promedio total de los proyectos
    '''

    presupuesto_acumulado = 0

    for proyecto in proyectos:
        presupuesto_acumulado += proyecto['presupuesto']

    promedio_final = presupuesto_acumulado / len(proyectos)
    
    imprimir_mensaje(f'El presupuesto promedio es: {promedio_final}', 'Info')

    return 



def buscar_proyecto_por_nombre(proyectos: list[dict]):
    '''
    Solicita un nombre y muestra el proyecto que coincida
    '''

    nombre_a_buscar = input("Ingrese el nombre del proyecto: ")
    nombre_encontrado = False

    normalizar_fechas_a_strftime(proyectos)

    for proyecto in proyectos:
        if proyecto['nombre'].lower() == nombre_a_buscar.lower():
            imprimir_mensaje('Proyecto encontrado', 'Success')
            mostrar_proyecto(proyecto)
            nombre_encontrado = True
            limpiar_consola()
    if nombre_encontrado == False:
        imprimir_mensaje('Verifique el nombre ingresado, no se encontraron coincidencias', 'Error')
        limpiar_consola()

    normalizar_fechas_a_strptime(proyectos)

    return



def quick_sort_asc(proyectos: list[dict], key: str) -> list:   

    if len(proyectos) < 2:
        return proyectos    

    pivot = proyectos.pop()
    mas_grandes = []
    mas_chicos = []

    for proyecto in proyectos:
        if proyecto[key] > pivot[key]:
            mas_grandes.append(proyecto)
        elif proyecto[key] < pivot[key]:
            mas_chicos.append(proyecto)
        else:
            if proyecto['id'] > pivot['id']:
                mas_grandes.append(proyecto)
            else:
                mas_chicos.append(proyecto)

    return quick_sort_asc(mas_chicos, key) + [pivot] + quick_sort_asc(mas_grandes, key)



def quick_sort_desc(proyectos: list[dict], key: str) -> list:   

    if len(proyectos) < 2:
        return proyectos    

    pivot = proyectos.pop()
    mas_grandes = []
    mas_chicos = []

    for proyecto in proyectos:
        if proyecto[key] > pivot[key]:
            mas_grandes.append(proyecto)
        elif proyecto[key] < pivot[key]:
            mas_chicos.append(proyecto)
        else:
            if proyecto['id'] > pivot['id']:
                mas_chicos.append(proyecto)
            else:
                mas_grandes.append(proyecto)

    return quick_sort_desc(mas_grandes, key) + [pivot] + quick_sort_desc(mas_chicos, key)



def ordenar_asc_desc(proyectos: list[dict], tipo_orden: str, key: str):
    '''
    Recibe una lista de diccionarios, tipo de orden y una key
    para ordenar la lista de manera ascendente/descendente 
    analizando los valores de la key
    \ntipo_orden = 'asc' 'desc'
    '''

    opciones_validas = ['asc', 'desc']

    if not proyectos:
        return -1
    elif tipo_orden not in opciones_validas:
        imprimir_mensaje(f'Debe ingresar una de las opciones validas: {opciones_validas}', 'Error')
    else:
        if tipo_orden == 'asc':
            lista_ordenada = quick_sort_asc(proyectos, key)
        else:
            lista_ordenada = quick_sort_desc(proyectos, key)

    return lista_ordenada



def ordenar_proyectos(proyectos: list[dict]):

    opciones_validas_clave = ['nombre', 'presupuesto', 'fecha_inicio']
    opciones_validas_orden = ['asc', 'desc']

    while True:
        opcion_clave = input(f"Elija por que clave desea ordenar ({opciones_validas_clave}): ")
        if opcion_clave not in opciones_validas_clave:
            imprimir_mensaje('La clave ingresada no es válida', 'Error')
            limpiar_consola()
        else:
            break
    
    while True:
        opcion_orden = input(f"Elija el tipo de orden ({opciones_validas_orden}): ")
        if opcion_orden not in opciones_validas_orden:
            imprimir_mensaje('El orden ingresado no es válido', 'Error')
            limpiar_consola()
        else:
            break

    proyectos_ordenados = ordenar_asc_desc(proyectos[:], opcion_orden, opcion_clave)

    mostrar_todos_los_proyectos(proyectos_ordenados)

    return 



def normalizar_fechas_a_strptime(proyectos: list[dict]):
    '''
    Esta función será llamada para normalizar las fechas del tipo datetime usando el metodo strptime
    '''

    for proyecto in proyectos:
        proyecto['fecha_inicio'] = datetime.strptime(proyecto['fecha_inicio'], '%d-%m-%Y')
        proyecto['fecha_fin'] = datetime.strptime(proyecto['fecha_fin'], '%d-%m-%Y')



def normalizar_fechas_a_strftime(proyectos: list[dict]):
    '''
    Esta función será llamada para normalizar las fechas del tipo datetime usando el metodo strftime
    '''

    for proyecto in proyectos:
        proyecto['fecha_inicio'] = datetime.strftime(proyecto['fecha_inicio'], '%d-%m-%Y')
        proyecto['fecha_fin'] = datetime.strftime(proyecto['fecha_fin'], '%d-%m-%Y')



def retomar_proyecto(proyectos: list[dict], bandera: bool):
    '''
    Esta función filtra los proyectos cancelados y vuelve a activo el que el usuario decida
    '''
    if bandera:

        proyectos_cancelados = []

        for proyecto in proyectos:
            if proyecto['estado'] == 'Cancelado':
                proyectos_cancelados.append(proyecto)

        normalizar_fechas_a_strftime(proyectos)
        
        if not proyectos_cancelados:
            imprimir_mensaje('No se han encontrado proyectos cancelados', 'Info')
        else:

            for proyecto in proyectos_cancelados:
                mostrar_proyecto(proyecto)
            imprimir_mensaje('Se han encontrado esos proyectos cancelados, ingrese el id del proyecto a retomar', 'Success')
            id_str = input("id: ")
            if id_str.isdigit():
                id = int(id_str)
                proyecto_a_retomar = encontrar_proyecto(proyectos_cancelados, id)
                if proyecto_a_retomar:
                    proyecto_a_retomar['estado'] = 'Activo'
                    imprimir_mensaje('El proyecto se actualizó a activo', 'Success')
            else:
                imprimir_mensaje('El id no es válido', 'Error')

        normalizar_fechas_a_strptime(proyectos)

    else:
        imprimir_mensaje('Ha alcanzado el límite de proyectos activos', 'Error')
    
    return   



def menor_presupuesto(proyectos: list[dict]) -> list[dict]:
    '''
    Esta función recorre una lista de diccionarios buscando los diccionarios que contengan el menor presupuesto\n
    Retorna -1 si la lista está vacía
    '''
    if not proyectos:
        return -1
    
    presupuesto_mas_bajo = proyectos[0]['presupuesto']
    proyectos_buscados = [proyectos[0]]

    for proyecto in proyectos[1:]:
        if presupuesto_mas_bajo > proyecto['presupuesto']:
            presupuesto_mas_bajo = proyecto['presupuesto']
            proyectos_buscados = [proyecto]
        elif presupuesto_mas_bajo == proyecto['presupuesto']:
            proyectos_buscados.append(proyecto)

    return proyectos_buscados



def mayor_menor_año_proyectos(proyectos: list[dict], key: str, eleccion: str) -> int:
    '''
    Esta función recorre la lista y devuelve un entero que representa el mayor o menor año, según corresponda\n
    key: 'fecha_inicio', 'fecha_fin'\n
    eleccion: 'mayor', 'menor'
    '''
    
    fecha_buscada = None

    if eleccion.lower() == 'mayor':
    
        for proyecto in proyectos:
            if fecha_buscada is None:
                fecha_buscada = proyecto[key]
            elif fecha_buscada < proyecto[key]:
                fecha_buscada = proyecto[key]
                
    elif eleccion.lower() == 'menor':
    
        for proyecto in proyectos:
            if fecha_buscada is None:
                fecha_buscada = proyecto[key]
            elif fecha_buscada > proyecto[key]:
                fecha_buscada = proyecto[key]

    año_fecha_buscada = fecha_buscada.year

    return año_fecha_buscada



def proyectos_de_verano_menor_presupuesto(proyectos: list[dict]):
    '''
    Esta función recorre la lista de diccionarios e informa sobre los proyectos más baratos iniciados y activos en cada verano
    '''

    se_encontro_uno = False
    menor_año = mayor_menor_año_proyectos(proyectos, 'fecha_inicio', 'menor')
    mayor_año = mayor_menor_año_proyectos(proyectos, 'fecha_inicio', 'mayor')
    diferencia_de_años = mayor_año - menor_año
    inicio_verano_general = '21-12-0001'
    fin_verano_general = '20-03-0001'
    inicio_verano_iterable = datetime.strptime(inicio_verano_general, '%d-%m-%Y')
    fin_verano_iterable = datetime.strptime(fin_verano_general, '%d-%m-%Y')

    for i in range(diferencia_de_años + 1):
        proyectos_iniciados_activos = []
        inicio_verano_actual = inicio_verano_iterable.replace(year = menor_año + i)
        fin_verano_actual = fin_verano_iterable.replace(year = menor_año + i + 1)

        for proyecto in proyectos:
            if proyecto['fecha_inicio'] >= inicio_verano_actual and proyecto['fecha_inicio'] <= fin_verano_actual:
                if proyecto['estado'] == 'Activo':
                    proyectos_iniciados_activos.append(proyecto)
                    se_encontro_uno = True

        proyectos_menor_presupuesto = menor_presupuesto(proyectos_iniciados_activos)

        if proyectos_menor_presupuesto != -1:
            if len(proyectos_menor_presupuesto) == 1:
                imprimir_mensaje(f'Este es el proyecto con menor presupuesto iniciado en el verano entre {inicio_verano_actual.year} y {fin_verano_actual.year}', 'Info')
                normalizar_fechas_a_strftime(proyectos_menor_presupuesto)
                mostrar_proyecto(proyectos_menor_presupuesto[0])
                normalizar_fechas_a_strptime(proyectos_menor_presupuesto)

            elif len(proyectos_menor_presupuesto) >= 2:
                imprimir_mensaje(F'Estos son los proyectos con el menor presupuesto iniciados en el verano entre {inicio_verano_actual.year} y {fin_verano_actual.year}', 'Info')
                mostrar_todos_los_proyectos(proyectos_menor_presupuesto)

    if se_encontro_uno is False:
        imprimir_mensaje('No se encontró ningún proyecto activo e iniciado en verano', 'Error')

    return



def proyectos_durante_cuarentena(proyectos: list[dict]):
    '''
    Esta función analiza la lista de proyectos y muestra los proyectos finalizados durante la cuarentena, en caso de no haber muestra un mensaje de error
    '''
    fecha_inicio = '01-03-2020'
    fecha_fin = '31-12-2021'
    fecha_inicio_formateada = datetime.strptime(fecha_inicio, '%d-%m-%Y')
    fecha_fin_formateada = datetime.strptime(fecha_fin, '%d-%m-%Y')
    finalizados_en_cuarentena = []

    for proyecto in proyectos:
        if proyecto['estado'] == 'Finalizado':
            if proyecto['fecha_fin'] >= fecha_inicio_formateada and proyecto['fecha_fin'] <= fecha_fin_formateada:
                finalizados_en_cuarentena.append(proyecto)

    if not finalizados_en_cuarentena:
        imprimir_mensaje('No se encontraron proyectos que hayan finalizado durante la cuarentena', 'Error')
    else:
        mostrar_todos_los_proyectos(finalizados_en_cuarentena)
        imprimir_mensaje(f'Se encontraron {len(finalizados_en_cuarentena)} proyectos finalizados durante la cuarentena', 'Success')

    return