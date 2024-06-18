from app import proyectos_app
from biblioteca import cargar_csv_en_memoria, PATH

if __name__ == '__main__':
    proyectos = cargar_csv_en_memoria(PATH)
    proyectos_app(proyectos)