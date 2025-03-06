from strings import Strings

def main():
    s = Strings()
    texto = "Anita lava la tina"
    print(f"¿Es palíndromo?: {s.es_palindromo(texto)}")
    print(f"Texto invertido: {s.invertir_cadena(texto)}")
    print(f"Número de vocales: {s.contar_vocales(texto)}")
    print(f"Número de consonantes: {s.contar_consonantes(texto)}")
    print(f"¿Es anagrama?: {s.es_anagrama('amor', 'roma')}")
    print(f"Número de palabras: {s.contar_palabras(texto)}")
    print(f"Texto con mayúsculas: {s.palabras_mayus(texto)}")
    print(f"Texto sin espacios duplicados: {s.eliminar_espacios_duplicados('Hola   mundo  python')}")
    print(f"¿Es número entero?: {s.es_numero_entero('-12345')}")
    print(f"Texto cifrado César (desplazamiento 3): {s.cifrar_cesar('Hola Mundo', 3)}")
    print(f"Texto descifrado César (desplazamiento 3): {s.descifrar_cesar('Krod Pxqgr', 3)}")
    print(f"Posiciones de 'la' en el texto: {s.encontrar_subcadena(texto, 'la')}")

if __name__ == "__main__":
    main()
