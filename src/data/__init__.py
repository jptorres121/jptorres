from data import Data

def main():
    data = Data()
    
    # Pruebas de los métodos
    lista = [1, 2, 3, 4, 5]
    print("Lista invertida:", data.invertir_lista(lista))
    
    print("Índice del elemento 3:", data.buscar_elemento(lista, 3))
    
    lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
    print("Lista sin duplicados:", data.eliminar_duplicados(lista_con_duplicados))
    
    lista1 = [1, 3, 5]
    lista2 = [2, 4, 6]
    print("Lista combinada ordenada:", data.merge_ordenado(lista1, lista2))
    
    print("Lista rotada 2 posiciones:", data.rotar_lista(lista, 2))
    
    lista_faltante = [1, 2, 4, 5]
    print("Número faltante:", data.encuentra_numero_faltante(lista_faltante))
    
    print("¿[1, 2] es subconjunto de [1, 2, 3, 4]?:", data.es_subconjunto([1, 2], [1, 2, 3, 4]))
    
    pila = data.implementar_pila()
    pila["push"](10)
    pila 
    print("Elemento en la cima de la pila:", pila["peek"]())
    print("Elemento removido de la pila:", pila["pop"]())
    
    cola = data.implementar_cola()
    cola["enqueue"](30)
    cola 
    print("Elemento en el frente de la cola:", cola["peek"]())
    print("Elemento removido de la cola:", cola["dequeue"]())
    
    matriz = [[1, 2, 3], [4, 5, 6]]
    print("Matriz transpuesta:", data.matriz_transpuesta(matriz))

if __name__ == "__main__":
    main()