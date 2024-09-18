from os.path import join
import pygame
from random import randint, uniform

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

all_sprites = pygame.sprite.Group()
meteor_sprite = pygame.sprite.Group()
laser_sprite = pygame.sprite.Group()



class Player(pygame.sprite.Sprite):
    def __init__(self, groups, laser_surf):
        super().__init__(groups)
        self.original_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.image = self.original_surf
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 500
        
        # laser settings
        
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.laser_cooldown = 400
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
            Laser(self.laser_surf, self.rect.midtop, (all_sprites, laser_sprite))
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
        if self.rect.bottom < 0:
            self.kill()
            

class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf, pos,groups):
        self.rotation = 0
        super().__init__(groups)
        self.original_surf = surf
        self.image = self.original_surf
        self.rect = self.image.get_frect(center= pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform( -0.5,0.5),1)
        self.speed = 400
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        self.rotation += randint(1,200) * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.rect = self.image.get_frect(center= self.rect.center)


class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self,frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()


def display_score(display_surface):
    current_time = pygame.time.get_ticks()
    font = pygame.font.Font(join('images','Oxanium-Bold.ttf'), 20)
    
    text_surf = font.render(str(current_time), True,'black') 
    text_rect = text_surf.get_frect(midbottom= (WINDOW_WIDTH/2,WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)  
    pygame.draw.rect(display_surface,'white',text_rect.inflate(20,20).move(0,-5),1,10)


def collisions(player, explosion_frames):
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprite, True, pygame.sprite.collide_mask)
    
    for laser in laser_sprite:
         collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprite, True)
         if collided_sprites:
            laser.kill()
            AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)
         
