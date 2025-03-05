import math
class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        return base * altura
    
    def perimetro_rectangulo(self, base, altura):
        return 2 * (base+altura)
    
    def area_circulo(self, radio):
        return math.pi * radio
    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio
    def area_triangulo(self, base, altura):
        return (base*altura)/2
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    def es_triangulo_valido(self, lado1, lado2, lado3):
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura)/2
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor)/2
    def area_pentagono_regular(self, lado, apotema):
        
    def perimetro_pentagono_regular(self, lado):
        
    def area_hexagono_regular(self, lado, apotema):
        
    def perimetro_hexagono_regular(self, lado):
        
    def volumen_cubo(self, lado):
        
    def area_superficie_cubo(self, lado):
        
    def volumen_esfera(self, radio):
        
    def area_superficie_esfera(self, radio):
        
    def volumen_cilindro(self, radio, altura):
        
    def area_superficie_cilindro(self, radio, altura):
        
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        
    def punto_medio(self, x1, y1, x2, y2):
        
    def pendiente_recta(self, x1, y1, x2, y2):
        
    def ecuacion_recta(self, x1, y1, x2, y2):
        
    def area_poligono_regular(self, num_lados, lado, apotema):
        
    def perimetro_poligono_regular(self, num_lados, lado):
