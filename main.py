import sys
from random import randint, uniform

import pygame


def laser_update(laser_list: list, speed: int = 300) -> None:
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)


def meteor_update(meteor_list: list, speed: int = 300) -> None:
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt

        if meteor_rect.top > WINDOW_HEIGHT:
            # a lista contem tuples
            meteor_list.remove(meteor_tuple)


def display_score() -> None:
    score_text = f'Score:{pygame.time.get_ticks() // 1000} '
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'White', text_rect.inflate(30, 30), width=8, border_radius=5)


def laser_timer(can_shoot: bool, duration: int = 500) -> bool:
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot


# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Shooter")
# game init end

can_shoot = True
shoot_time = None
# importing images
ship_surface = pygame.image.load('./graphics/ship.png').convert_alpha()
background_surface = pygame.image.load('./graphics/background.png').convert()
laser_surface = pygame.image.load('./graphics/laser.png').convert_alpha()
meteor_surface = pygame.image.load('./graphics/meteor.png').convert_alpha()

# ship_surface_rotated = pygame.transform.rotate(ship_surface, 45)

# import text
font = pygame.font.Font('./graphics/subatomic.ttf', 50)

# rectangules
ship_rect = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# meteor timer - custom event
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)  # call every 500ms

# laser_rect = laser_surface.get_rect(midbottom=ship_rect.midtop)
laser_list = []
meteor_list = []
while True:
    # input -> event loop (click, movement, buttons, controls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            # laser
            laser_rect = laser_surface.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

            # timer logic
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor_surface.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            # tupla meteor
            meteor_list.append((meteor_rect, direction))
    # framerate limiter
    dt = clock.tick(120) / 1000  # 1000ms in 1s

    # mouse inputs
    ship_rect.center = pygame.mouse.get_pos()

    laser_update(laser_list)
    meteor_update(meteor_list)
    # laser timer
    can_shoot = laser_timer(can_shoot, duration=400)
    pygame.time.get_ticks()
    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))

    display_score()

    for rect in laser_list:
        display_surface.blit(laser_surface, rect)

    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surface, meteor_tuple[0])

    display_surface.blit(ship_surface, ship_rect)
    # show frames to player - final frame
    pygame.display.update()
