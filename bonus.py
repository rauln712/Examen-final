from dijkstra import dijkstra
 
def ruta_con_intermedia(red, origen, intermedia, destino):
    """
    BONUS 8: Calcula la ruta más rápida de origen a destino pasando por intermedia.
    Hace dos Dijkstra: origen->intermedia y intermedia->destino.
    Une los caminos y suma los tiempos.
    """
    print(f"\n  Calculando: {origen} -> {intermedia} -> {destino}")
#Validacion de que no sea repetidos
    if origen == intermedia:
        print("  [!] El origen y la estación intermedia no pueden ser la misma.")
        return
    if intermedia == destino:
        print("  [!] La estación intermedia y el destino no pueden ser la misma.")
        return
    if origen == destino:
        print("  [!] El origen y el destino no pueden ser la misma estación.")
        return
    # Primer tramo: origen -> intermedia
    camino1, tiempo1 = dijkstra(red, origen, intermedia)
    if camino1 is None:
        print(f"  [!] No hay camino de '{origen}' a '{intermedia}'.")
        return
 
    # Segundo tramo: intermedia -> destino
    camino2, tiempo2 = dijkstra(red, intermedia, destino)
    if camino2 is None:
        print(f"  [!] No hay camino de '{intermedia}' a '{destino}'.")
        return
 
    # Unir caminos (evitar duplicar la estación intermedia)
    camino_total = camino1 + camino2[1:]
    tiempo_total = tiempo1 + tiempo2
 
    print(f"\n  Ruta: {' -> '.join(camino_total)}")
    print(f"  Tiempo total: {tiempo_total} min")
    print(f"    Tramo 1 ({origen} -> {intermedia}): {tiempo1} min")
    print(f"    Tramo 2 ({intermedia} -> {destino}): {tiempo2} min")