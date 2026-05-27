import dijkstra

def detectar_hub(red):
    """
    BONUS 8: Detecta la estación con mayor número de conexiones directas (grado).
    Devuelve (nombre_hub, num_conexiones).
    """
    if not red.grafo:
        print("  [!] La red está vacía.")
        return None, 0
 
    hub = max(red.grafo, key=lambda e: len(red.grafo[e]))
    num_conexiones = len(red.grafo[hub])
    return hub, num_conexiones
 
 
def exportar_informe(red, nombre_archivo):
    """
    BONUS 8 (extra): Exporta un informe .txt con estadísticas de la red.
    """
    hub, num_conexiones_hub = detectar_hub(red)
    if hub is None:
        return
 
    # Calcular número total de conexiones (sin duplicar)
    total_aristas = sum(len(v) for v in red.grafo.values()) // 2
 
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("====== INFORME DE LA RED DE TRANSPORTE ======\n\n")
            f.write(f"Número de estaciones:   {len(red.grafo)}\n")
            f.write(f"Número de conexiones:   {total_aristas}\n")
            f.write(f"Estación hub:           {hub} ({num_conexiones_hub} conexiones)\n")
        print(f"  [OK] Informe exportado en '{nombre_archivo}'.")
    except Exception as e:
        print(f"  [!] Error al exportar el informe: {e}")
 
 
def ruta_con_intermedia(red, origen, intermedia, destino):
    """
    BONUS 9: Calcula la ruta más rápida de origen a destino pasando por intermedia.
    Hace dos Dijkstra: origen->intermedia y intermedia->destino.
    Une los caminos y suma los tiempos.
    """
    print(f"\n  Calculando: {origen} -> {intermedia} -> {destino}")
 
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