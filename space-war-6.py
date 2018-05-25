# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# colors
WHITE = (255, 255, 255)

# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/Gianna.ttf", 96)

# Images
startscreen = pygame.image.load('images/splashscreen1.png').convert()
ship_img = pygame.image.load('images/burger.png')
blood = pygame.image.load('images/burger2.png')
laser = pygame.image.load('images/laser.png')
enemy = pygame.image.load('images/mouth.png')
bonus = pygame.image.load('images/bonus.png')
enemy2 = pygame.image.load('images/mouth2.png')
enemy11 = pygame.image.load('images/mouth11.png')
enemy22 = pygame.image.load('images/mouth22.png')
enemy111 = pygame.image.load('images/mouth111.png')
enemy222 = pygame.image.load('images/mouth222.png')
bomb_img = pygame.image.load('images/enemy-laser.png')
bombx_img = pygame.image.load('images/enemy-laser.png')
background = pygame.image.load('images/restaurant.png')
end = pygame.image.load('images/restaurant2.png')
win = pygame.image.load('images/winscreen.png')

# stages
START = 0
PLAYING = 1
END = 2

# Sound Effects
pew = pygame.mixer.Sound("sounds/laser.ogg")
EXPLOSION = pygame.mixer.Sound("sounds/ouch.ogg")
OOF = pygame.mixer.Sound("sounds/hit.ogg")
die = pygame.mixer.Sound("sounds/stink.ogg")


def setup():
    global ship, lasers, mobs, player, bombs, fleet, mobsx, bombsx, fleetx, stage, time_remaining, ticks
    
    ship = Ship(460, 830, ship_img, blood)
    lasers = []
    mob1 = Mob(10, 30, enemy2)
    mob2 = Mob(70, 30, enemy)
    mob3 = Mob(138, 30, enemy2)
    mob4 = Mob(198, 30, enemy)
    mob5 = Mob(266, 30, enemy2)
    mob6 = Mob(326, 30, enemy)
    mob7 = Mob(394, 30, enemy2)
    mob8 = Mob(454, 30, enemy)
    mob9 = Mob(522, 30, enemy2)
    mob10 = Mob(582, 30, enemy)
    mob11 = Mob(640, 30, enemy2)
    mob12 = Mob(700, 30, enemy)
    mob13 = Mob(768, 30, enemy2)
    mob14 = Mob(828, 30, enemy)
    mob15 = Mob(896, 30, enemy2)
    mob16 = Mob(956, 30, enemy)
    mob17 = Mob(10, 60, enemy2)
    mob18 = Mob(70, 60, enemy)
    mob19 = Mob(138, 60, enemy2)
    mob20 = Mob(198, 60, enemy)
    mob21 = Mob(266, 60, enemy2)
    mob22 = Mob(326, 60, enemy)
    mob23 = Mob(394, 60, enemy2)
    mob24 = Mob(454, 60, enemy)
    mob25 = Mob(522, 60, enemy2)
    mob26 = Mob(582, 60, enemy)
    mob27 = Mob(640, 60, enemy2)
    mob28 = Mob(700, 60, enemy)
    mob29 = Mob(768, 60, enemy2)
    mob30 = Mob(828, 60, enemy)
    mob31 = Mob(896, 60, enemy2)
    mob32 = Mob(956, 60, enemy)
    mob33 = Mob(10, 90, enemy2)
    mob34 = Mob(70, 90, enemy)
    mob35 = Mob(138, 90, enemy2)
    mob36 = Mob(198, 90, enemy)
    mob37 = Mob(266, 90, enemy2)
    mob38 = Mob(326, 90, enemy)
    mob39 = Mob(394, 90, enemy2)
    mob40 = Mob(454, 90, enemy)
    mob41 = Mob(522, 90, enemy2)
    mob42 = Mob(582, 90, enemy)
    mob43 = Mob(640, 90, enemy2)
    mob44 = Mob(700, 90, enemy)
    mob45 = Mob(768, 90, enemy2)
    mob46 = Mob(828, 90, enemy)
    mob47 = Mob(896, 90, enemy2)
    mob48 = Mob(956, 90, enemy)
    mob49 = Mob(10, 120, enemy2)
    mob50 = Mob(70, 120, enemy)
    mob51 = Mob(138, 120, enemy2)
    mob52 = Mob(198, 120, enemy)
    mob53 = Mob(266, 120, enemy2)
    mob54 = Mob(326, 120, enemy)
    mob55 = Mob(394, 120, enemy2)
    mob56 = Mob(454, 120, enemy)
    mob57 = Mob(522, 120, enemy2)
    mob58 = Mob(582, 120, enemy)
    mob59 = Mob(640, 120, enemy2)
    mob60 = Mob(700, 120, enemy)
    mob61 = Mob(768, 120, enemy2)
    mob62 = Mob(828, 120, enemy)
    mob63 = Mob(896, 120, enemy2)
    mob64 = Mob(956, 120, enemy)

    mobx1 = MobX(10, 150, bonus)
    mobx2 = MobX(70, 150, bonus)
    mobx3 = MobX(138, 150, bonus)
    mobx4 = MobX(198, 150, bonus)
    mobx5 = MobX(266, 150, bonus)
    mobx6 = MobX(326, 150, bonus)
    mobx7 = MobX(394, 150, bonus)


    # Make sprite groups
    player = pygame.sprite.Group()
    player.add(ship)
    player.score = 0
    player.shield = 5

    lasers = pygame.sprite.Group()

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11,
             mob12, mob13, mob14, mob15, mob16, mob17, mob18, mob19, mob20, mob21,
             mob22, mob23, mob24, mob25, mob26, mob27, mob28, mob29, mob30, mob31,
             mob32, mob33, mob34, mob35, mob36, mob37, mob38, mob39, mob40, mob41,
             mob42, mob43, mob44, mob45, mob46, mob47, mob48, mob49, mob50, mob51,
             mob52, mob53, mob54, mob55, mob56, mob57, mob58, mob59, mob60, mob61,
             mob62, mob63, mob64)


    mobsx = pygame.sprite.Group()
    mobsx.add(mobx1, mobx2, mobx3, mobx4, mobx5, mobx6, mobx7)


    bombs = pygame.sprite.Group()
    bombsx = pygame.sprite.Group()

    fleet = Fleet(mobs)
    fleetx = FleetX(mobsx)

    # set stage
    stage = START
    time_remaining = 40
    ticks = 0

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image, blood):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.w = 32
        self.h = 32
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 10
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            
    def move_right(self):
        self.rect.x += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH - 0
            
    def shoot(self):
        las = Laser(laser)
        
        las.rect.centerx = self.rect.centerx
        las.rect.centery = self.rect.top
        
        lasers.add(las)
        pew.play()

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            OOF.play()
            self.image = blood
            self.shield -= 1
            player.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
            stage == END

  
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 8
        
    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

        
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 3

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, players):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        
        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 1
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
                

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 10
        

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 20
        self.speed = 3
        self.moving_right = True
    

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobs:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
            for m in mobs:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse:
            self.moving_right = not self.moving_right
            for m in mobs:
                #m.rect.y += 20
                pass


    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()




class MobX(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 3

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, players):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)
        
        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 10
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
                
    
    
class FleetX:

    def __init__(self, mobsx):
        self.mobsx = mobsx
        self.bombx_rate = 20
        self.speed = 10
        self.moving_right = True
    

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobsx:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
            for m in mobsx:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse:
            self.moving_right = not self.moving_right
            for m in mobsx:
                m.rect.y += 20


    def choose_bomber(self):
        rand = random.randrange(0, self.bombx_rate)
        all_mobsx = mobsx.sprites()
        
        if len(all_mobsx) > 0 and rand == 0:
            return random.choice(all_mobsx)
        else:
            return None
    
    def update(self):
        self.move()

        bomberx = self.choose_bomber()
        if bomberx != None:
            bomberx.drop_bomb()



# Game helper functions
def show_title_screen():
    screen.blit(startscreen, (0, 0))
    title_text = FONT_XL.render("Don't Eat Me!", 1, WHITE)
    extra_text = FONT_MD.render("Press SPACE to play", 1, WHITE)
    screen.blit(title_text, [260, 430])
    screen.blit(extra_text, [350, 600])
    

def show_stats(player):
    score_text = FONT_MD.render("Score: " + str(player.score), 1, WHITE)
    screen.blit(score_text, [0, 0])

    shield_text = FONT_MD.render("Shield: " + str(player.shield), 1, WHITE)
    screen.blit(shield_text, [0, 20])

def show_end():
    if len(mobs) == 0:
          screen.blit(win, [0,0])
    if len(player) == 0: 
          screen.blit(end, [0,0])

# Global Variables
def start_music(stage):
     if stage == START:
          pygame.mixer.music.load("sounds/intro.ogg")
          pygame.mixer.music.play(-1) 

     if stage == PLAYING:
          pygame.mixer.music.load("sounds/backgroundmusic.ogg")
          pygame.mixer.music.play(-1)
          
     if stage == END:
          pygame.mixer.music.load("sounds/outro.ogg")
          pygame.mixer.music.play(-1)

    
# Game loop
setup()
start_music(stage)
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    start_music(PLAYING)
                    
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    start_music(END)
                    setup()
                    

    if stage == PLAYING:            
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()

        

            
                        
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        player.update(bombs)
        lasers.update()
        bombs.update()
        mobs.update(lasers, player)
        fleet.update()
        mobsx.update(lasers, player)
        fleetx.update()


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(background, [0,0])
    lasers.draw(screen)
    bombs.draw(screen)
    bombsx.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    mobsx.draw(screen)
    show_stats(player)

    if stage == START:
        show_title_screen()


    elif stage == PLAYING:
        timer_text = FONT_MD.render(str(time_remaining), True, WHITE)
        screen.blit(timer_text, [490, 0])

        if time_remaining == 0:
            stage = END
            start_music(END)

        elif len(player) == 0:
            stage = END

        elif len(mobs) == 0:
            stage = END

    if stage == END:
        show_end()
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
