class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1]."""
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        """Busca un elemento en una lista y devuelve su índice (o -1 si no existe)."""
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        resultado = []
        seen = set()

        for item in lista:
            # La clave en el set debe incluir tanto el valor como su tipo para diferenciarlos
            clave = (item, type(item))
            if clave not in seen:
                resultado.append(item)
                seen.add(clave)

        return resultado


    
    def merge_ordenado(self, lista1, lista2):
        """Combina dos listas ordenadas en una sola lista ordenada."""
        i, j = 0, 0
        lista_ordenada = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                lista_ordenada.append(lista1[i])
                i += 1
            else:
                lista_ordenada.append(lista2[j])
                j += 1
        lista_ordenada.extend(lista1[i:])
        lista_ordenada.extend(lista2[j:])
        return lista_ordenada
    
    def rotar_lista(self, lista, k):
        if not lista:  # Si la lista está vacía, devolverla directamente
            return []
        k = k % len(lista)  # Asegurar que no haya rotaciones innecesarias
        return lista[-k:] + lista[:-k]

    
    def encuentra_numero_faltante(self, lista):
        """Encuentra el número faltante en una lista de enteros del 1 al n."""
        n = len(lista) + 1  # El tamaño esperado
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """Verifica si conjunto1 es subconjunto de conjunto2 sin usar set."""
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """Implementa una estructura de datos tipo pila (stack) usando listas."""
        pila = []
        return {
            'push': lambda x: pila.append(x),
            'pop': lambda: pila.pop() if pila else None,
            'peek': lambda: pila[-1] if pila else None,
            'is_empty': lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        """Implementa una estructura de datos tipo cola (queue) usando listas."""
        cola = []
        return {
            'enqueue': lambda x: cola.append(x),
            'dequeue': lambda: cola.pop(0) if cola else None,
            'peek': lambda: cola[0] if cola else None,
            'is_empty': lambda: len(cola) == 0
        }
    
    def matriz_transpuesta(self, matriz):
        """Calcula la transpuesta de una matriz."""
        if not matriz or not matriz[0]:  # Si la matriz está vacía o tiene listas vacías
            return []
    
        filas = len(matriz)
        columnas = len(matriz[0])
    
        return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]