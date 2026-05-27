import os

def cargar_desde_archivo(red, nombre_archivo):
    """
    Carga la red desde un archivo CSV con formato:
        origen,destino,minutos
    Construye el grafo añadiendo estaciones y conexiones.
    """
    if not os.path.exists(nombre_archivo):
        print(f"  [!] El archivo '{nombre_archivo}' no existe.")
        return
 
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
 
        cargadas = 0
        for num_linea, linea in enumerate(lineas, start=1):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue  # Ignorar líneas vacías o comentarios
 
            partes = linea.split(",")
            if len(partes) != 3:
                print(f"  [!] Línea {num_linea} inválida (formato incorrecto): '{linea}'")
                continue
 
            origen, destino, tiempo_str = partes[0].strip(), partes[1].strip(), partes[2].strip()
 
            try:
                minutos = float(tiempo_str)
            except ValueError:
                print(f"  [!] Línea {num_linea}: el tiempo '{tiempo_str}' no es un número.")
                continue
 
            # Añadir estaciones si no existen (silenciosamente)
            if origen not in red.grafo:
                red.grafo[origen] = []
            if destino not in red.grafo:
                red.grafo[destino] = []
 
            # Añadir conexión (usando el método con validaciones)
            # Comprobamos duplicado antes de llamar al método para no mostrar mensajes
            ya_existe = any(v == destino for v, _ in red.grafo[origen])
            if not ya_existe and minutos > 0:
                red.grafo[origen].append((destino, minutos))
                red.grafo[destino].append((origen, minutos))
                cargadas += 1
 
        print(f"  [OK] Red cargada desde '{nombre_archivo}' ({cargadas} conexiones).")
 
    except Exception as e:
        print(f"  [!] Error al leer el archivo: {e}")
 
 
def guardar_en_archivo(red, nombre_archivo):
    """
    Guarda la red en un archivo CSV con formato:
        origen,destino,minutos
    Evita guardar duplicados (para cada conexión bidireccional, solo guarda una dirección).
    """
    try:
        guardadas = set()  # Para evitar duplicados
 
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for origen in red.grafo:
                for destino, tiempo in red.grafo[origen]:
                    # Ordenar el par para evitar guardar A,B y B,A
                    par = tuple(sorted([origen, destino]))
                    if par not in guardadas:
                        guardadas.add(par)
                        f.write(f"{origen},{destino},{tiempo}\n")
 
        print(f"  [OK] Red guardada en '{nombre_archivo}'.")
 
    except Exception as e:
        print(f"  [!] Error al guardar el archivo: {e}")
 