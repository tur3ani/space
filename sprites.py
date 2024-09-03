from os.path import join
import pygame
from random import  randint


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
class Player(pygame.sprite.Sprite):
    def __init__(self, groups, laser_surf):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 500
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.laser_cooldown = 1000
        self.laser_surf = laser_surf
    def laser_shoot(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.laser_cooldown:
                self.can_shoot = True


    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        if self.direction.length() != 0:
            self.direction.normalize_ip()

        self.rect.center += self.direction * self.speed * dt
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(self.laser_surf, self.rect.midtop, self.groups())
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        self.laser_shoot()



class stars(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect =  self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    def update(self,dt):
        self.rect.centery -= 400 * dt


