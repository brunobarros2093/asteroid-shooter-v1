import sys

import pygame


def laser_update(laser_list: list, speed: int = 300) -> None:
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)


def display_score() -> None:
    score_text = f'Score:{pygame.time.get_ticks()} '
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'White', text_rect.inflate(30, 30), width=8, border_radius=5)


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

# ship_surface_rotated = pygame.transform.rotate(ship_surface, 45)

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)

# rectangules
ship_rect = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser_rect = laser_surface.get_rect(midbottom=ship_rect.midtop)
laser_list = []
while True:
    # input -> event loop (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surface.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

    # framerate limiter
    dt = clock.tick(120) / 1000  # 1000ms in 1s

    # mouse inputs
    ship_rect.center = pygame.mouse.get_pos()

    laser_update(laser_list)
    pygame.time.get_ticks()
    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))

    display_score()

    for rect in laser_list:
        display_surface.blit(laser_surface, rect)

    display_surface.blit(ship_surface, ship_rect)
    # show frames to player - final frame
    pygame.display.update()
