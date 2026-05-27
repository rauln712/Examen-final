from collections import deque

def estan_conectadas(red, origen, destino):
    """
    Comprueba si existe algún camino entre origen y destino usando BFS.
    Usa una cola (deque) y un conjunto de visitados.
 
    Devuelve True si están conectadas, False en caso contrario.
    """
    if origen not in red.grafo:
        print(f"  [!] La estación '{origen}' no existe.")
        return False
    if destino not in red.grafo:
        print(f"  [!] La estación '{destino}' no existe.")
        return False
    if origen == destino:
        return True
 
    visitados = set()       # Nodos ya visitados
    cola = deque([origen])  # Cola BFS
    visitados.add(origen)
 
    while cola:
        actual = cola.popleft()
 
        for vecino, _ in red.grafo[actual]:
            if vecino == destino:
                return True  # Encontramos el destino
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
 
    return False  # No se encontró camino