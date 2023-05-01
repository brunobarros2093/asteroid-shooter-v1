import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Shooter")

# importing images
ship_surface = pygame.image.load('./graphics/ship.png').convert_alpha()
background_surface = pygame.image.load('./graphics/background.png').convert()

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'White')

ship_y_pos = 500
while True:
    # input -> events (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # framerate limiter
    clock.tick(120)
    # updates  ----------------------x--y
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))
    ship_y_pos -= 1
    display_surface.blit(text_surf, (500, 200))
    display_surface.blit(ship_surface, (300, ship_y_pos))
    # show frames to player
    pygame.display.update()
