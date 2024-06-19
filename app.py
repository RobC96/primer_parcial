import re
from biblioteca import *


def proyectos_app(proyectos: list[dict]) -> None:

    while True:

        bandera = limite_de_proyectos(50, proyectos)

        menu =\
        """
        1  - Ingresar proyecto.
        2  - Modificar proyecto.
        3  - Cancelar proyecto.
        4  - Comprobar proyecto.
        5  - Mostrar todos.
        6  - Calcular presupuesto promedio.
        7  - Buscar proyecto por nombre.
        8  - Ordenar proyectos.
        9  - Retomar proyecto.
        10 - Calcular el/los proyectos activos con menor presupuesto iniciados en verano. En caso de que no haya indicar error.
        11 - Mostrar todos los proyectos terminados en medio de la cuarentena del COVID 19 (Marzo de 2020 hasta el fin del 2021 por ejemplo). En caso de que no haya indicar error.
        12 - Salir.
        """

        opcion = 0
        opcion_str = input(f'{menu}Su opcion: ')
        if re.match('^[0-9]{1,2}$', opcion_str):
            opcion = int(opcion_str)

        match opcion:
            case 1:
                agregar_proyecto_memoria(proyectos, bandera)
            case 2:
                modificar_proyecto(proyectos, bandera)
            case 3:
                cancelar_proyecto(proyectos)
            case 4:
                comprobar_fecha_fin(proyectos)
            case 5:
                mostrar_todos_los_proyectos(proyectos)
            case 6:
                calcular_presupuesto_promedio(proyectos)
            case 7:
                buscar_proyecto_por_nombre(proyectos)
            case 8:
                ordenar_proyectos(proyectos)
            case 9:
                retomar_proyecto(proyectos, bandera)
            case 10:
                proyectos_de_verano_menor_presupuesto(proyectos)
            case 11:
                proyectos_durante_cuarentena(proyectos)
            case 12:
                agregar_proyectos_csv(proyectos)
                guardar_proyectos_finalizados(proyectos)
                break
            case _:
                imprimir_mensaje(f'La opcion {opcion} es incorrecta!', 'error')
        limpiar_consola()