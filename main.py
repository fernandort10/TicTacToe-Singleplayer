import pygame
from cuadricula import Cuadricula

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'


surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('CherryMataHaraka')

cuadricula = Cuadricula()


encendido = True
jugador = "Cherry"

while encendido:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            encendido = False
        if event.type == pygame.MOUSEBUTTONDOWN and not cuadricula.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cuadricula.get_mouse(pos[0] // 200, pos[1] // 200, jugador)
                if cuadricula.cambiar_jugador:
                    if jugador == "Cherry":
                        jugador = "Haraka"
                    else:
                        jugador = "Cherry"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and cuadricula.game_over:
                cuadricula.limpiar_cuadricula()
                cuadricula.game_over = False
            elif event.key == pygame.K_ESCAPE:
                encendido = False


    surface.fill((204,102,0))

    cuadricula.dibujar(surface)

    pygame.display.flip()
