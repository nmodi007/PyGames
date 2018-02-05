import pygame
import sys
from GameObject import GameObject

# Initialize Pygame
pygame.init()
pygame.mixer.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.mouse.set_visible(False)

# Load resources
logo_image = pygame.image.load("PS circle.png")
sound = pygame.mixer.Sound("Pluralsight.wav")
myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
intersectText = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

# Prepare logo
logo_image_size = logo_image.get_size()
logo_image.fill((0, 0, 0), None, pygame.BLEND_RGBA_MAX)  # put a hit-box around the circle logo image.

x, y = 0, 0
clock = pygame.time.Clock()
directionX, directionY = 1, 1


def playSound():
    sound.stop()
    sound.play()


rectangle = GameObject(100, 100, 400, 400)
logo = GameObject(0, 0, logo_image_size[0], logo_image_size[1])

while True:
    clock.tick(30)

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()

    mousePosition = pygame.mouse.get_pos()

    x = mousePosition[0]
    y = mousePosition[1]

    logo.set_position(x, y)

    if logo.intersects(rectangle):
        screen.blit(intersectText, (10, 10))
        playSound()

    if x + logo_image_size[0] > 800:
        x = 800 - logo_image_size[0]

    if y + logo_image_size[1] > 600:
        y = 600 - logo_image_size[1]

    if y <= 0:
        y = 0
    if x <= 0:
        x = 0

    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 400, 400), 1)

    screen.blit(logo_image, (x, y))

    pygame.display.update()
