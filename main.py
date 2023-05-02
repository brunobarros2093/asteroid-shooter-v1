import pygame
import sys

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Shooter")
# game init end

# importing images
ship_surface = pygame.image.load('./graphics/ship.png').convert_alpha()
background_surface = pygame.image.load('./graphics/background.png').convert()
laser_surface = pygame.image.load('./graphics/laser.png').convert_alpha()

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'White')

# rectangules
ship_rect = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
laser_rect = laser_surface.get_rect(midbottom=ship_rect.midtop)

while True:
    # input -> event loop (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limiter
    clock.tick(120)
    # mouse inputs
    ship_rect.center = pygame.mouse.get_pos()
    # updates  ----------------------x--y
    laser_rect.y += 5
    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))
    display_surface.blit(text_surf, text_rect)
    display_surface.blit(laser_surface, laser_rect)
    
    # tests draw
    pygame.draw.rect(display_surface, 'White', text_rect.inflate(30, 30), width=8, border_radius=5)
    # end draw native rectangules

    display_surface.blit(ship_surface, ship_rect)
    # show frames to player - final frame
    pygame.display.update()
