class Strings:
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
        return texto == texto[::-1]

    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida  # Agregar cada caracter al inicio de la nueva cadena
        return invertida

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)

    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in texto if char in consonantes)

    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        return " ".join([palabra.capitalize() for palabra in texto.split()])

    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())

    def es_numero_entero(self, texto):
        if texto.startswith("-"):
            texto = texto[1:]
        return all(char in "0123456789" for char in texto) and bool(texto)

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
