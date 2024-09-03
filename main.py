import sys
from os.path import join
from random import randint
import sprites
import pygame



# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter DX")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# Load images


meteorite_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()


# Create rectangles
meteorite_rect = meteorite_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_rect = laser_surf.get_rect(center=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))

# Generate star positions
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
    sprites.stars(all_sprites,star_surf)
player = sprites.Player(all_sprites, laser_surf)

# custom event --> metorite event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)

while True:
    dt= clock.tick(144) / 1000 # clock.tick() gives us delta time in milliseconds so we divide by 1000 to get it in seconds for actual use

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            print("create meteor")
    # Draw the screen
    display.fill((169, 169, 169))  # darkgray
    



    display.blit(meteorite_surf, meteorite_rect)
    display.blit(laser_surf, laser_rect)
    all_sprites.draw(display)
    all_sprites.update(dt)
    pygame.display.update()
