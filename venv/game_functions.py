import sys

import pygame


from bullet import Bullet
from alien import Alien
from time import sleep

from pygame.sprite import Group
from pygame import freetype
bunker1 = 0







alienCollidedWithBullets = False
numberOfTicks = 0
alien1 = 0;
bulletThatCollidedWithBunker = 0
bulletCollidedWithBunker = False
bullets1 = Group()
rowForBunkerPixel = 50
columnForBunkerPixel = 270
numberOfTimesIncremented = 0
numberOfTimesIncrementedForRow = 0
count = 0
count1 = 0



def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break
def ship_hit(ai_settings,screen,stats,sb, ship, aliens, bullets):

  if stats.ships_left > 0:
    stats.ships_left -=1

    sb.prep_ships()

    aliens.empty()
    bullets.empty()


    create_fleet(ai_settings, screen,ship,aliens)
    ship.center_ship()

    sleep(0.5)
  else:
      stats.game_active = False
      pygame.mouse.set_visible(True)

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)

    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)



    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship hit!!!!!")




def check_keydown_events(event,ai_settings,screen,ship,bullets,bunker):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:

        fire_bullet(ai_settings, screen, ship, bullets,bunker)

    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets,bunker):

      if len(bullets) < ai_settings.bullets_allowed:

        new_bullet = Bullet(ai_settings,screen,ship,bunker)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,bunker):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)



        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets,bunker)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):


        button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True


        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


        aliens.empty()
        bullets.empty()


        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def update_screen(ai_settings, screen,stats, sb,ship, aliens, bullets, play_button,bunker):

    screen.fill(ai_settings.bg_color)


    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    bunkerCopy = bunker
    screen.blit(bunkerCopy,(50,270))
    del bunker

    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,bunkerGroup,bunker):
    global alienCollidedWithBullets
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)



    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets,bunkerGroup,bunker)



def check_high_score(stats,sb):

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score





def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens,bullets,bunkerGroup,bunker):



        pygame.draw.rect(screen,(0,0,255),bunker.get_rect(),5)
        pygame.display.update()




        global bunker12
        global count
        global count1















        gizo = True


        global bunkerRect

        global bulletThatCollidedWithBunker
        global bulletCollidedWithBunker
        global columnForBunkerPixel
        global rowForBunkerPixel
        global numberOfTimesIncremented
        global numberOfTimesIncrementedForRow

        rect5 = pygame.Rect((0,0),(500,500))


        temp = bunker





        bunker12 = bunker.copy()
        bunker12.scroll(50,270)








        print("bunker get parent")







        count1 = count1 + 1





        print("This is the location of the color pixel")

        print(bunker12.get_at((499,503)))







        try:









          if bulletCollidedWithBunker and numberOfTimesIncremented !=3:
              if(bunker12.get_at(((int)(bulletThatCollidedWithBunker.x-1), (int)(bulletThatCollidedWithBunker.y-1))) == (118,255,3)):
               bunker.set_at(((int)(bulletThatCollidedWithBunker.x - rowForBunkerPixel), (int)(bulletThatCollidedWithBunker.y - columnForBunkerPixel)), (255, 255, 255))
               columnForBunkerPixel = columnForBunkerPixel + 1
               numberOfTimesIncremented = numberOfTimesIncremented + 1
               print("column for bunker pixel")
               print(columnForBunkerPixel)


          if numberOfTimesIncremented == 3:
              numberOfTimesIncrementedForRow = numberOfTimesIncrementedForRow + 1
              columnForBunkerPixel = 270
              numberOfTimesIncremented = 0
              rowForBunkerPixel = rowForBunkerPixel + 1


          if numberOfTimesIncrementedForRow == 3:
              bulletCollidedWithBunker = False
              rowForBunkerPixel = 50
              columnForBunkerPixel = 270
              numberOfTimesIncrementedForRow = 0
              numberOfTimesIncremented = 0













          for bullet12 in bullets:

                print("bullet value")

                print((int)(bullet12.x), (int)(bullet12.y))
                print("color value")


                pygame.display.update()



                if(bunker12.get_at(((int)(bullet12.x), (int)(bullet12.y))) == (118,255,3) and bullet12.y >= 497  ):


                  bulletCollidedWithBunker = True



                  bulletThatCollidedWithBunker = bullet12






                  print("collided with the best bunker in the world")



                  bunker12 .set_at(((int)(bullet12.x-50), (int)(bullet12.y-270)),(255,255,255))




                  print("bunker's pixel color at location")








                  print("collided with bunker")

                  bullet12.kill()















        except IndexError:
            print("out of range")










        global alienCollidedWithBullets
        global numberOfTicks
        global alien1


        for alien in aliens:



           if(alien.collided_with(bullets)):
              alienCollidedWithBullets = True
              print("in here")
              alien1 = alien

        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


        for aliens in collisions.values():
          stats.score += ai_settings.alien_points * len(aliens)
          sb.prep_score()
          check_high_score(stats, sb)




        if (alienCollidedWithBullets):
                part1OfCollision = pygame.image.load("images/enemy1Explosionp1.png")
                part2OfCollision = pygame.image.load("images/enemy1Explosionp2.png")
                part3OfCollision = pygame.image.load("images/enemy1Explosionp3.png")
                if numberOfTicks != 50:
                    screen.blit(part1OfCollision, alien1.rect)
                    pygame.display.update()

                if numberOfTicks >= 10 and numberOfTicks <= 20:
                    screen.blit(part2OfCollision, alien1.rect)
                    pygame.display.update()

                if numberOfTicks >= 20 and numberOfTicks <= 30:
                    screen.blit(part3OfCollision, alien1.rect)
                    pygame.display.update()

                if (numberOfTicks == 30):
                 numberOfTicks = 0
                 alienCollidedWithBullets = False

                else:
                 numberOfTicks = numberOfTicks + 1











        if len(aliens) == 0:
                 bullets.empty()
                 ai_settings.increase_speed()

                 stats.level += 1
                 sb.prep_level()
                 create_fleet(ai_settings,screen,ship,aliens)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / ( 2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings,alien_width):
        available_space_x = ai_settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number, row_number, image):
        alien = Alien(ai_settings, screen ,image)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)




def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen, "images/blueAlien.bmp.png")
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)


    for row_number in range(number_rows):
     for alien_number in range(number_aliens_x):
        if row_number == 0:
         create_alien(ai_settings,screen,aliens,alien_number, row_number,"images/blueAlien.bmp.png")

        if row_number == 1:

                create_alien(ai_settings, screen, aliens, alien_number, row_number, "images/greenAlien.png")

        if row_number == 2:
            create_alien(ai_settings, screen, aliens, alien_number, row_number, "images/pinkAlien.png")



