import pygame
from pygame.sprite import Sprite




class Bullet(Sprite):



    def __init__(self,ai_settings,screen,ship,bunker):

        super(Bullet, self).__init__()
        self.screen = screen


        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top



        self.y = self.rect.y
        self.x = self.rect.x


        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):


        self.y -= self.speed_factor

        self.rect.y = self.y


    def check_for_bunker_collisions(self,bunkers):
        return pygame.sprite.spritecollide(self,bunkers)

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color,self.rect)


    def delete_bullet(self):
        self.kill()