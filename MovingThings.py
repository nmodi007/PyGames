import sys
import pygame

pygame.init()  # initilize pygame modules

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hello_world = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

while True:

    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()

    screen.blit(hello_world, (0, 0))  # use blit to place objects on the screen. provide x, y corrdinates


    pygame.display.update()
