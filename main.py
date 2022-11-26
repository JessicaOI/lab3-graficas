# lab3 graficas
# Jessica Ortiz 20192
import pygame
from OpenGL.GL import *
import numpy as np
import copy
import random


pygame.init()
# escala de los pixeles
scale = 8

# pantalla
w = 64
h = 64
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

#el como que explota
pixels[21][21] = 1
pixels[22][22] = 1
pixels[22][23] = 1
pixels[21][23] = 1
pixels[20][23] = 1

pixels[31][41] = 1
pixels[32][42] = 1
pixels[32][43] = 1
pixels[31][43] = 1
pixels[30][43] = 1

pixels[20][10] = 1
pixels[20][11] = 1
pixels[20][12] = 1

#hace pequeño circulo
pixels[15][10] = 1
pixels[14][11] = 1
pixels[13][13] = 1
pixels[12][13] = 1
pixels[11][13] = 1

pixels[31][51] = 1
pixels[32][52] = 1
pixels[32][53] = 1
pixels[31][53] = 1
pixels[30][53] = 1

#estrellita pequeña
pixels[5][3] = 1
pixels[5][4] = 1
pixels[5][5] = 1
#estrellita pequeña
pixels[5][3] = 1
pixels[5][4] = 1
pixels[5][5] = 1

pixels[10][40] = 1
pixels[11][41] = 1
pixels[12][43] = 1
pixels[11][43] = 1
pixels[10][43] = 1

#parte del que se mueve
pixels[30][30] = 1
pixels[32][32] = 1
pixels[32][33] = 1
pixels[31][33] = 1
pixels[30][33] = 1

pixels[21][21] = 1
pixels[22][22] = 1
pixels[22][23] = 1
pixels[21][23] = 1
pixels[20][23] = 1

#estrellita pequeña
pixels[30][5] = 1
pixels[30][6] = 1
pixels[30][7] = 1

#estrellita pequeña
pixels[40][5] = 1
pixels[40][6] = 1
pixels[40][7] = 1

#el como que explota
pixels[31][21] = 1
pixels[32][22] = 1
pixels[32][23] = 1
pixels[31][23] = 1
pixels[30][23] = 1

pixels[41][41] = 1
pixels[42][42] = 1
pixels[42][43] = 1
pixels[41][43] = 1
pixels[40][43] = 1
#cuando termina aqui hace la estrella mediana
pixels[43][43] = 1
pixels[38][35] = 1
pixels[17][17] = 1
pixels[17][21] = 1
pixels[40][43] = 1
#hace pequeño circulo
pixels[25][10] = 1
pixels[24][11] = 1
pixels[23][13] = 1
pixels[22][13] = 1
pixels[21][13] = 1

pixels[41][61] = 1
pixels[42][62] = 1
pixels[42][63] = 1
pixels[41][63] = 1
pixels[40][63] = 1


#ray casting
running = True
while running:
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # dibujar
    update()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False