import sys
from os.path import join
from random import randint
import sprites
import pygame
from sprites import Player ,all_sprites,meteor_sprite,laser_sprite, display_score, collisions


# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter DX")
clock = pygame.time.Clock()


# load sprites


# Load images


meteorite_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
explosion_frames = [pygame.image.load(join('images','explosion',f'{i}.png')) for i in range(21) ]
player = Player(all_sprites, laser_surf)


# Generate star positions

for i in range(20):
    sprites.stars(all_sprites,star_surf)


# custom event --> metorite event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)





# main game loop

while True:
    dt= clock.tick(144) / 1000 # clock.tick() gives us delta time in milliseconds so we divide by 1000 to get it in seconds for actual use

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            x , y = randint(0,WINDOW_WIDTH), randint(-200, -100)
            sprites.Meteor(meteorite_surf, (x,y), (all_sprites, meteor_sprite))
    # Draw the screen
    display.fill((169, 169, 169))  # darkgray
    
    collisions(player, explosion_frames)    
    display_score(display)

    all_sprites.draw(display)
    all_sprites.update(dt)
    pygame.display.update()
