import sys
from os.path import join
from random import randint

import pygame


# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter DX")

clock = pygame.time.Clock()

# Load images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
meteorite_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()

# Create rectangles
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 500
meteorite_rect = meteorite_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_rect = laser_surf.get_rect(center=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))

# Generate star positions
star_positions = [(randint(0, WINDOW_WIDTH - star_surf.get_width()), randint(0, WINDOW_HEIGHT - star_surf.get_height())) for _ in range(20)]

while True:
    dt= clock.tick(144) / 1000 # clock.tick() gives us delta time in milliseconds so we divide by 1000 to get it in seconds for actual use

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.:
            print("file laser")
    # Draw the screen
    display.fill((169, 169, 169))  # darkgray
    
    for pos in star_positions:
        display.blit(star_surf, pos)

    keys = pygame.key.get_pressed()

    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    #
    player_rect.center += player_speed * player_direction * dt
    if player_direction.length() != 0:
        player_direction.normalize_ip()



    display.blit(player_surf, player_rect)
    display.blit(meteorite_surf, meteorite_rect)
    display.blit(laser_surf, laser_rect)
    
    pygame.display.update()
