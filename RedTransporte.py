class RedTransporte:
    """
    Modela una red de transporte como un grafo ponderado no dirigido.
    El grafo se almacena como un diccionario de listas de adyacencia:
        self.grafo = {
            "A": [("B", 10), ("C", 15)],
            "B": [("A", 10)],
            ...
        }
    """
 
    def __init__(self):
        self.grafo = {}  # Diccionario de adyacencia: {estacion: [(vecino, tiempo), ...]}
 
    # ---------- AÑADIR ESTACIÓN ----------
 
    def añadir_estacion(self, estacion):
        """Añade una estación al grafo si no existe ya."""
        estacion = estacion.strip()
        if estacion in self.grafo:
            print(f"  [!] La estación '{estacion}' ya existe.")
        else:
            self.grafo[estacion] = []
            print(f"  [OK] Estación '{estacion}' añadida.")
 
    # ---------- AÑADIR CONEXIÓN ----------
 
    def añadir_conexion(self, origen, destino, minutos):
        """
        Añade una conexión bidireccional entre origen y destino con el tiempo dado.
        Valida que las estaciones existan, que el tiempo sea positivo
        y que la conexión no sea duplicada.
        """
        # Validar existencia de estaciones
        if origen not in self.grafo:
            print(f"  [!] La estación origen '{origen}' no existe.")
            return
        if destino not in self.grafo:
            print(f"  [!] La estación destino '{destino}' no existe.")
            return
 
        # Validar tiempo positivo
        if minutos <= 0:
            print("  [!] El tiempo debe ser un número positivo.")
            return
 
        # Comprobar duplicado (sentido origen -> destino)
        for vecino, _ in self.grafo[origen]:
            if vecino == destino:
                print(f"  [!] Ya existe una conexión entre '{origen}' y '{destino}'.")
                return
 
        # Añadir en ambas direcciones (grafo bidireccional)
        self.grafo[origen].append((destino, minutos))
        self.grafo[destino].append((origen, minutos))
        print(f"  [OK] Conexión añadida: {origen} <-> {destino} ({minutos} min).")
 
    # ---------- MOSTRAR ESTACIONES ----------
 
    def mostrar_estaciones(self):
        """Muestra todas las estaciones de la red."""
        if not self.grafo:
            print("  [!] La red está vacía.")
            return
        print(f"\n  Estaciones ({len(self.grafo)} en total):")
        for estacion in sorted(self.grafo.keys()):
            print(f"    - {estacion}")
 
    # ---------- MOSTRAR CONEXIONES DE UNA ESTACIÓN ----------
 
    def mostrar_conexiones(self, estacion):
        """Muestra las conexiones directas de una estación concreta."""
        if estacion not in self.grafo:
            print(f"  [!] La estación '{estacion}' no existe.")
            return
        conexiones = self.grafo[estacion]
        if not conexiones:
            print(f"  La estación '{estacion}' no tiene conexiones.")
        else:
            print(f"  Conexiones de '{estacion}':")
            for vecino, tiempo in conexiones:
                print(f"    -> {vecino} ({tiempo} min)")