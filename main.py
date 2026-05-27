#Lamamos a todas las funciones necesarias para el funcionamiento del programa, y a la función principal que lanza el menú interactivo.
import os
from RedTransporte import RedTransporte
from persistencia import cargar_desde_archivo, guardar_en_archivo
from dijkstra import dijkstra
from BFS import estan_conectadas
from bonus import detectar_hub, exportar_informe, ruta_con_intermedia


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n" + "=" * 45)
    print("   PLANIFICADOR DE RUTAS - RED DE TRANSPORTE")
    print("=" * 45)
    print("  1. Cargar red desde archivo")
    print("  2. Añadir estación")
    print("  3. Añadir conexión")
    print("  4. Ver estaciones y conexiones")
    print("  5. Ruta más rápida entre dos estaciones")
    print("  6. ¿Están conectadas dos estaciones?")
    print("  7. Guardar y salir")
    print("  --- BONUS ---")
    print("  8. Detectar estación hub y exportar informe")
    print("  9. Ruta pasando por estación intermedia")
    print("=" * 45)
 
 
def menu_ver_estaciones(red):
    """Submenú para ver estaciones o conexiones de una concreta."""
    red.mostrar_estaciones()
    print("\n  ¿Quieres ver las conexiones de una estación concreta?")
    opcion = input("  Escribe el nombre (o Enter para saltar): ").strip()
    if opcion:
        red.mostrar_conexiones(opcion)
 
 
def ejecutar_menu(red, archivo_por_defecto):
    """Bucle principal del menú interactivo."""
    while True:
        mostrar_menu()
 
        try:
            opcion = int(input("  Elige una opción: ").strip())
        except ValueError:
            print("  [!] Debes introducir un número del 1 al 9.")
            continue
 
        # --- Opción 1: Cargar desde archivo ---
        if opcion == 1:
            archivo = input(f"  Nombre del archivo [{archivo_por_defecto}]: ").strip()
            if not archivo:
                archivo = archivo_por_defecto
            cargar_desde_archivo(red, archivo)
 
        # --- Opción 2: Añadir estación ---
        elif opcion == 2:
            nombre = input("  Nombre de la nueva estación: ").strip()
            if nombre:
                red.añadir_estacion(nombre)
            else:
                print("  [!] El nombre no puede estar vacío.")
 
        # --- Opción 3: Añadir conexión ---
        elif opcion == 3:
            origen = input("  Estación origen: ").strip()
            destino = input("  Estación destino: ").strip()
            try:
                minutos = float(input("  Tiempo en minutos: ").strip())
            except ValueError:
                print("  [!] El tiempo debe ser un número.")
                continue
            red.añadir_conexion(origen, destino, minutos)
 
        # --- Opción 4: Ver estaciones y conexiones ---
        elif opcion == 4:
            menu_ver_estaciones(red)
 
        # --- Opción 5: Ruta más rápida (Dijkstra) ---
        elif opcion == 5:
            origen = input("  Estación origen: ").strip()
            destino = input("  Estación destino: ").strip()
            camino, tiempo = dijkstra(red, origen, destino)
            if camino is not None:
                print(f"\n  Ruta más rápida: {' -> '.join(camino)}")
                print(f"  Tiempo total: {tiempo} min")
            else:
                print(f"  No existe camino de '{origen}' a '{destino}'.")
 
        # --- Opción 6: ¿Están conectadas? (BFS) ---
        elif opcion == 6:
            origen = input("  Estación origen: ").strip()
            destino = input("  Estación destino: ").strip()
            if estan_conectadas(red, origen, destino):
                print(f"  [SÍ] '{origen}' y '{destino}' están conectadas.")
            else:
                print(f"  [NO] '{origen}' y '{destino}' NO están conectadas.")
 
        # --- Opción 7: Guardar y salir ---
        elif opcion == 7:
            archivo = input(f"  Nombre del archivo [{archivo_por_defecto}]: ").strip()
            if not archivo:
                archivo = archivo_por_defecto
            guardar_en_archivo(red, archivo)
            print("  ¡Hasta luego!")
            break  # Salir del bucle
 
        # --- Opción 8 (BONUS): Hub e informe ---
        elif opcion == 8:
            hub, num = detectar_hub(red)
            if hub:
                print(f"\n  Estación hub: '{hub}' con {num} conexiones directas.")
                exportar = input("  ¿Exportar informe? (s/n): ").strip().lower()
                if exportar == "s":
                    nombre_inf = input("  Nombre del archivo de informe [informe.txt]: ").strip()
                    if not nombre_inf:
                        nombre_inf = "informe.txt"
                    exportar_informe(red, nombre_inf)
 
        # --- Opción 9 (BONUS): Ruta con intermedia ---
        elif opcion == 9:
            origen = input("  Estación origen: ").strip()
            intermedia = input("  Estación intermedia (obligatoria): ").strip()
            destino = input("  Estación destino: ").strip()
            ruta_con_intermedia(red, origen, intermedia, destino)
 
        # --- Opción inválida ---
        else:
            print("  [!] Opción no válida. Elige entre 1 y 9.")
 
if __name__ == "__main__":
    ARCHIVO_POR_DEFECTO = "red_transporte.txt"
 
    # Crear la red vacía
    red = RedTransporte()
 
    # Preguntar si cargar automáticamente al inicio
    if os.path.exists(ARCHIVO_POR_DEFECTO):
        print(f"\n  Se encontró el archivo '{ARCHIVO_POR_DEFECTO}'.")
        respuesta = input("  ¿Cargar la red automáticamente? (s/n): ").strip().lower()
        if respuesta == "s":
            cargar_desde_archivo(red, ARCHIVO_POR_DEFECTO)
 
    # Lanzar el menú
    ejecutar_menu(red, ARCHIVO_POR_DEFECTO)