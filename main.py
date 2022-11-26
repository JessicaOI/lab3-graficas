# lab3 graficas
# Jessica Ortiz 20192
import pygame
from OpenGL.GL import *
import copy
import random


pygame.init()
# escala de los pixeles
scale = 10

# pantalla
w = 80
h = 80
screen = pygame.display.set_mode((w*scale, h*scale),pygame.OPENGL | pygame.DOUBLEBUF)

# colores
pixelsColor = (1, 1, 1)
background = (0, 0, 0)

# creamos un array para almacenar los pixeles que se tienen con un for
pixels = []
for x in range(1, w+1):
    temp = []
    for y in range(1, h+1):
        xy = 0
        temp.append(xy)
        # print(xy)
        y = +1
    pixels.append(temp)
    x = +1

# funcion la cual define la logica del Juego de la vida
# utilizando el array de pixeles
def logicaJDLV(x, y, pixels):
    count = 0
    if x > 0 and x < 50 and y > 0 and y < 50:
        if pixels[x-1][y+1] == 1:
            count += 1
        if pixels[x][y+1] == 1:
            count += 1
        if pixels[x+1][y+1] == 1:
            count += 1
        if pixels[x-1][y] == 1:
            count += 1
        if pixels[x+1][y] == 1:
            count += 1
        if pixels[x-1][y-1] == 1:
            count += 1
        if pixels[x][y-1] == 1:
            count += 1
        if pixels[x+1][y-1] == 1:
            count += 1

    return count

# funcion de los pixeles
def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x*scale, y*scale, 1*scale, 1*scale)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


# funcion dibujar para los pixles
def draw():
    for x in range(len(pixels)):
        for y in range(len(pixels)):
            if pixels[x][y] == 1:
                pixel(x, y, pixelsColor)
            else:
                pixel(x, y, background)

# funcion de Update para dar la logica al juego y poder mostrar los diferentes cambios
def update():
    # Toma la ultima captura de los pixeles
    last_pixels = copy.deepcopy(pixels)
    for x in range(w):
        for y in range(h):
            if pixels[x][y] == 1:
                # underpopulation
                if logicaJDLV(x, y, last_pixels) < 2:
                    pixels[x][y] = 0
                # survival
                if logicaJDLV(x, y, last_pixels) > 3:
                    pixels[x][y] = 0
                # overpopulation
                if logicaJDLV(x, y, last_pixels) == 2 or logicaJDLV(x, y, last_pixels) == 3:
                    pixels[x][y] = 1

            else:
                # reproduction
                if logicaJDLV(x, y, last_pixels) == 3:
                    pixels[x][y] = 1
    draw()

# retorna el size de la pantalla
size = (w * h)/3
x = w
y = h

# Generacion de pixeles
pixels[15][2] = 1
pixels[15][5] = 1
pixels[15][5] = 1 
pixels[15][1] = 1
pixels[15][3] = 1

pixels[25][1] = 1
pixels[25][2] = 1
pixels[25][3] = 1
pixels[25][2] = 1



#ray casting
running = True
while running:
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # dibujar
    update()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False