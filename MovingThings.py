import sys
import pygame

pygame.init()  # initialize pygame modules

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hello_world = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

hello_world_size = hello_world.get_size()

x = 0
y = 0

clock = pygame.time.Clock()

directionX = 1
directionY = 1

image_obj = pygame.image.load("cool_image.png")
image_obj_size = image_obj.get_size()

pygame.mouse.set_visible(False)  # hide the mouse pointer

while True:

    clock.tick(40)  # this game loop will run 40 times per second.

    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()

    screen.fill((250, 255, 195))

    mouse_position = pygame.mouse.get_pos()

    x, y = mouse_position

    if x + hello_world_size[0] > 800:
        x = 800 - hello_world_size[0]

    if y + hello_world_size[1] > 600:
        y = 600 - hello_world_size[1]

    if x + image_obj_size[0] > 800:
        x = 800 - image_obj_size[0]

    if y + image_obj_size[1] > 600:
        y = 600 - image_obj_size[1]

    screen.blit(image_obj, (x, y))  # use blit to place objects on the screen. provide x, y coordinates

    pygame.display.update()
