import pygame
import sys
import math
pygame.init()
Naviso = True
aviso = True
ANCHO = 900
ALTO = 900
WIN = pygame.display.set_mode((ANCHO, ALTO))
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (43, 5, 255)
VERDE = (0, 255, 0)
def dibujar_plano_cartesiano():
    pygame.draw.line(WIN, NEGRO, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 2)
    pygame.draw.line(WIN, NEGRO, (0, ALTO // 2), (ANCHO, ALTO // 2), 2)
    for x in range(-ANCHO // 2, ANCHO // 2, 20):
        pygame.draw.line(WIN, NEGRO, (ANCHO // 2 + x, ALTO // 2 - 5), (ANCHO // 2 + x, ALTO // 2 + 5))
    for y in range(-ALTO // 2, ALTO // 2, 20):
        pygame.draw.line(WIN, NEGRO, (ANCHO // 2 - 5, ALTO // 2 + y), (ANCHO // 2 + 5, ALTO // 2 + y))
def evaluar_funcion(x, coeficientes):
    resultado = 0
    for i, coeficiente in enumerate(coeficientes):
        resultado += coeficiente * (x ** i)
    return resultado
def graficar_funcion(coeficientes):
    for x in range(-ANCHO // 2, ANCHO // 2):
        valor_x = x / 10.0
        valor_y = -evaluar_funcion(valor_x, coeficientes) * 10
        pygame.draw.circle(WIN, AZUL, (ANCHO // 2 + x, ALTO // 2 + int(valor_y)), 2)
def distancia_entre_puntos(punto1, punto2):
    return math.sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)
def punto_medio(punto1, punto2):
    return ((punto1[0] + punto2[0]) // 2, (punto1[1] + punto2[1]) // 2)
def tipo_union_entre_lineas(pendiente1, pendiente2):
    if pendiente1 == pendiente2:
        return "Líneas paralelas"
    elif pendiente1 * pendiente2 == -1:
        return "Líneas perpendiculares"
    else:
        return "Líneas con otra relación"
def main():
    clock = pygame.time.Clock()
    coeficientes = []
    distancia_puntos_impreso = False
    punto_medio_impreso = False
    tipo_union_impreso = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        WIN.fill(BLANCO)
        dibujar_plano_cartesiano()
        if not coeficientes:
            try:
                entrada = input("Ingresa los coeficientes de la ecuación, separados por comas: ")
                coeficientes = [float(coeficiente) for coeficiente in entrada.split(',')]
            except ValueError:
                print("Error: Ingresa coeficientes válidos.")
        if coeficientes:
            graficar_funcion(coeficientes)
            if not distancia_puntos_impreso:
                punto_a = (100, -50)
                punto_b = (-50, 80)
                pygame.draw.circle(WIN, VERDE, punto_a, 5)
                pygame.draw.circle(WIN, VERDE, punto_b, 5)
                distancia = distancia_entre_puntos(punto_a, punto_b)
                punto_medio_coords = punto_medio(punto_a, punto_b)
                print(f"Distancia entre los puntos: {distancia}")
                print(f"Punto medio: {punto_medio_coords}")
                distancia_puntos_impreso = True
            if not tipo_union_impreso:
                punto_c = (50, 100)
                punto_d = (-30, -70)
                pygame.draw.circle(WIN, VERDE, punto_c, 5)
                pygame.draw.circle(WIN, VERDE, punto_d, 5)
                pendiente_ab = (punto_b[1] - punto_a[1]) / (punto_b[0] - punto_a[0])
                pendiente_cd = (punto_d[1] - punto_c[1]) / (punto_d[0] - punto_c[0])
                tipo_union = tipo_union_entre_lineas(pendiente_ab, pendiente_cd)
                print(f"Tipo de unión entre líneas: {tipo_union}")
                tipo_union_impreso = True
        pygame.display.flip()
        clock.tick(30)
if __name__ == "__main__":
    main()
