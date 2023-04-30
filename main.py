import pygame, sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Meteor Shooter")

test_surf = pygame.Surface((400, 100))

while True:
    # input -> events (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updates
    display_surface.blit(test_surf, (0, 0))
    test_surf.fill((15, 140, 122))
    # show frames to player
    pygame.display.update()
