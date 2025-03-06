class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [i for i in range(2, n+1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        return n == sum([i for i in range(1, n) if n % i == 0])
    
    def triangulo_pascal(self, filas):
        resultado = [[1]]
        for _ in range(filas - 1):
            nueva_fila = [1] + [resultado[-1][i] + resultado[-1][i + 1] for i in range(len(resultado[-1]) - 1)] + [1]
            resultado.append(nueva_fila)
        return resultado
    
    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(n))
    
    def es_numero_armstrong(self, n):
        digitos = list(map(int, str(n)))
        return n == sum(d ** len(digitos) for d in digitos)
    
    def es_cuadrado_magico(self, matriz):
        if not all(len(fila) == len(matriz) for fila in matriz):
            return False
        suma_ref = sum(matriz[0])
        return all(sum(fila) == suma_ref for fila in matriz) and \
               all(sum(matriz[j][i] for j in range(len(matriz))) == suma_ref for i in range(len(matriz))) and \
               sum(matriz[i][i] for i in range(len(matriz))) == suma_ref and \
               sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))) == suma_ref
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n