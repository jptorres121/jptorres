from magic import Magic

if __name__ == "__main__":
    m = Magic()
    
    print("Fibonacci de 10:", m.fibonacci(10))
    print("Secuencia Fibonacci (10 primeros):", m.secuencia_fibonacci(10))
    print("Es 17 primo?", m.es_primo(17))
    print("Primos hasta 50:", m.generar_primos(50))
    print("Es 28 un número perfecto?", m.es_numero_perfecto(28))
    print("Triángulo de Pascal (5 filas):", m.triangulo_pascal(5))
    print("Factorial de 5:", m.factorial(5))
    print("MCD de 48 y 18:", m.mcd(48, 18))
    print("MCM de 48 y 18:", m.mcm(48, 18))
    print("Suma de dígitos de 1234:", m.suma_digitos(1234))
    print("Es 153 un número de Armstrong?", m.es_numero_armstrong(153))
    
    cuadrado = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    print("Es cuadrado mágico?", m.es_cuadrado_magico(cuadrado))
