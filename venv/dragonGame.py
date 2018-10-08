
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from timeit import default_timer as timer

from pygame.sprite import Sprite
from pygame import Surface
alien1 = 0
bunker = 0
bulletCollidedWithBunker = False
bunkerGroup = Group()
bunkerRect = 0
rowForBunkerPixel = 50
columnForBunkerPixel = 270





class Bunker1(Surface):
    def __init__(self,image):

        self.image = image
        self.rect = image.get_rect(center=(50,300))

        self.rect.x = 50
        self.rect.y = 300










class Bunker(Sprite):
 def __init__(self,image,screen):


  self.image = image
  self.rect = self.image.get_rect()
  self.rect.x = 50
  self.rect.y = 300












def run_game():
    seconds = 0
    pygame.init()
    bulletCollidedWithBunker = False
    alienCollidedWithBullet = False
    ai_settings = Settings()
    bunkerRect = 0

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    numberOfTicks = 0








    bunker = pygame.image.load("images/bunker1.png")
    bunkerCopy = bunker
    del bunker


    print("bunker clipping area")
















    print("bunker's size")





































    gf.create_fleet(ai_settings, screen,ship, aliens)

    bg_color = (230, 230, 230)

    while True:








        pygame.display.update()


































        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,bunkerCopy)



        gf.update_screen(ai_settings, screen,stats,sb, ship, aliens, bullets, play_button,bunkerCopy)








        if stats.game_active:

          pygame.draw.circle(screen,(0,0,255),(130,242 ),5,5)

          pygame.display.update()

          ship.update()


          if bulletCollidedWithBunker == False:
           gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,bunkerGroup,bunkerCopy)
           gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens, bullets)



        if bulletCollidedWithBunker == False:
          bullets.update()




         #118,255,3,255


        for bunker12 in bunkerGroup:







































         for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                 bullets.remove(bullet)

















run_game()
