import math

class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def __init__(self):
        self.menu()
    
    def menu(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Calcular área")
            print("2. Calcular perímetro")
            print("3. Cálculos de geometría analítica")
            print("4. Salir")
            opcion = input("Ingrese el número de su opción: ")
            
            if opcion == "1":
                self.menu_areas()
            elif opcion == "2":
                self.menu_perimetros()
            elif opcion == "3":
                self.menu_geometria_analitica()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    
    def menu_areas(self):
        print("\nSeleccione la figura para calcular el área:")
        figuras = ["Rectángulo", "Círculo", "Triángulo", "Trapecio", "Rombo", "Pentágono Regular", "Hexágono Regular", "Cubo", "Esfera", "Cilindro", "Polígono Regular"]
        for i, figura in enumerate(figuras, start=1):
            print(f"{i}. {figura}")
        
        opcion = input("Ingrese el número de su opción: ")
        
        try:
            opcion = int(opcion)
            if opcion == 1:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Área del rectángulo:", self.area_rectangulo(base, altura))
            elif opcion == 2:
                radio = float(input("Ingrese el radio: "))
                print("Área del círculo:", self.area_circulo(radio))
            elif opcion == 3:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Área del triángulo:", self.area_triangulo(base, altura))
            elif opcion == 11:
                num_lados = int(input("Ingrese el número de lados: "))
                lado = float(input("Ingrese el tamaño de cada lado: "))
                apotema = float(input("Ingrese la apotema: "))
                print("Área del polígono regular:", self.area_poligono_regular(num_lados, lado, apotema))
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    
    def menu_perimetros(self):
        print("\nSeleccione la figura para calcular el perímetro:")
        figuras = ["Rectángulo", "Círculo", "Triángulo", "Pentágono Regular", "Hexágono Regular", "Polígono Regular"]
        for i, figura in enumerate(figuras, start=1):
            print(f"{i}. {figura}")
        
        opcion = input("Ingrese el número de su opción: ")
        
        try:
            opcion = int(opcion)
            if opcion == 1:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Perímetro del rectángulo:", self.perimetro_rectangulo(base, altura))
            elif opcion == 2:
                radio = float(input("Ingrese el radio: "))
                print("Perímetro del círculo:", self.perimetro_circulo(radio))
            elif opcion == 3:
                lado1 = float(input("Ingrese el primer lado: "))
                lado2 = float(input("Ingrese el segundo lado: "))
                lado3 = float(input("Ingrese el tercer lado: "))
                print("Perímetro del triángulo:", self.perimetro_triangulo(lado1, lado2, lado3))
            elif opcion == 6:
                num_lados = int(input("Ingrese el número de lados: "))
                lado = float(input("Ingrese el tamaño de cada lado: "))
                print("Perímetro del polígono regular:", self.perimetro_poligono_regular(num_lados, lado))
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    
    def menu_geometria_analitica(self):
        print("\nSeleccione la opción de cálculo:")
        opciones = ["Distancia entre dos puntos", "Punto medio", "Pendiente de la recta", "Ecuación de la recta"]
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")
        
        opcion = input("Ingrese el número de su opción: ")
        
        try:
            opcion = int(opcion)
            x1 = float(input("Ingrese x1: "))
            y1 = float(input("Ingrese y1: "))
            x2 = float(input("Ingrese x2: "))
            y2 = float(input("Ingrese y2: "))
            
            if opcion == 1:
                print("Distancia entre puntos:", self.distancia_entre_puntos(x1, y1, x2, y2))
            elif opcion == 2:
                print("Punto medio:", self.punto_medio(x1, y1, x2, y2))
            elif opcion == 3:
                print("Pendiente de la recta:", self.pendiente_recta(x1, y1, x2, y2))
            elif opcion == 4:
                print("Ecuación de la recta:", self.ecuacion_recta(x1, y1, x2, y2))
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            raise ValueError("La pendiente es indefinida para una línea vertical.")
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            return (1, 0, -x1) 
        m = self.pendiente_recta(x1, y1, x2, y2)
        b = y1 - m * x1
        return (-m, 1, -b)

if __name__ == "__main__":
    Geometria()
