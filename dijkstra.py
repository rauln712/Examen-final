import heapq

def dijkstra(red, origen, destino):
    """
    Calcula la ruta más rápida entre origen y destino usando el algoritmo de Dijkstra.
    Usa heapq como cola de prioridad.
 
    Devuelve:
        (camino, tiempo_total) si existe ruta.
        (None, None) si no existe ruta o las estaciones no existen.
 
    Estructura del heap: (tiempo_acumulado, estacion_actual, camino_hasta_aqui)
    """
    if origen not in red.grafo:
        print(f"  [!] La estación origen '{origen}' no existe.")
        return None, None
    if destino not in red.grafo:
        print(f"  [!] La estación destino '{destino}' no existe.")
        return None, None
    if origen == destino:
        print(f"  [!] Origen y destino son la misma estación.")
        return [origen], 0
 
    # Cola de prioridad: (tiempo_acumulado, estacion_actual, camino)
    cola = [(0, origen, [origen])]
    visitados = set()  # Estaciones ya procesadas definitivamente
 
    while cola:
        tiempo_actual, estacion_actual, camino_actual = heapq.heappop(cola)
 
        # Si ya procesamos esta estación con menor coste, la ignoramos
        if estacion_actual in visitados:
            continue
        visitados.add(estacion_actual)
 
        # Si llegamos al destino, devolvemos el resultado
        if estacion_actual == destino:
            return camino_actual, tiempo_actual
 
        # Explorar vecinos
        for vecino, tiempo_arista in red.grafo[estacion_actual]:
            if vecino not in visitados:
                nuevo_tiempo = tiempo_actual + tiempo_arista
                nuevo_camino = camino_actual + [vecino]
                heapq.heappush(cola, (nuevo_tiempo, vecino, nuevo_camino))
 
    # Si salimos del bucle sin llegar al destino, no hay camino
    return None, None