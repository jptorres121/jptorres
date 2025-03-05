class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def es_numero_perfecto(self, n):
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    def triangulo_pascal(self, filas):
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
    
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
        return sum(d ** len(digitos) for d in digitos) == n
    
    def es_cuadrado_magico(self, matriz):
        size = len(matriz)
        suma_ref = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_ref:
                return False
        
        for col in range(size):
            if sum(matriz[f][col] for f in range(size)) != suma_ref:
                return False
        
        if sum(matriz[i][i] for i in range(size)) != suma_ref:
            return False
        
        if sum(matriz[i][size - i - 1] for i in range(size)) != suma_ref:
            return False
        
        return True
