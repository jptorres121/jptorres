import re

class Strings:
    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo ignorando espacios y mayúsculas."""
        texto_limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        """Invierte una cadena."""
        return texto[::-1]

    def contar_vocales(self, texto):
        """Cuenta la cantidad de vocales en una cadena."""
        vocales = "aeiouAEIOU"
        return sum(1 for letra in texto if letra in vocales)

    def contar_consonantes(self, texto):
        """Cuenta la cantidad de consonantes en una cadena."""
        vocales = "aeiouAEIOU"
        consonantes = [letra for letra in texto if letra.isalpha() and letra not in vocales]
        print(f"Consonantes encontradas en '{texto}': {consonantes}")
        return len(consonantes) 

    def es_anagrama(self, palabra1, palabra2):
        """Verifica si dos palabras son anagramas."""
        palabra1_limpia = sorted(re.sub(r'\s+', '', palabra1.lower()))
        palabra2_limpia = sorted(re.sub(r'\s+', '', palabra2.lower()))
        return palabra1_limpia == palabra2_limpia

    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        palabras = texto.strip().split()
        return len(palabras)

    def palabras_mayus(self, texto):
        """Convierte cada palabra en la cadena a mayúscula inicial."""
        return texto.title()

    def eliminar_espacios_duplicados(self, texto):
        """Elimina los espacios duplicados en una cadena."""
        return re.sub(r'\s+', ' ', texto)

    def es_numero_entero(self, texto):
        """Verifica si un string representa un número entero."""
        return texto.lstrip('-').isdigit()
