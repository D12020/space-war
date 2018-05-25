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

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Images
player = pygame.image.load('images/burger.png')
laser = pygame.image.load('images/laser.png')
enemy = pygame.image.load('images/mouth.png')
bomb_img = pygame.image.load('images/enemy-laser.png')
background = pygame.image.load('images/restaurant.png')

# Sound Effects
pygame.mixer.music.load("sounds/backgroundmusic.ogg")
pew = pygame.mixer.Sound("sounds/laser.ogg")
EXPLOSION = pygame.mixer.Sound("sounds/ouch.ogg")
OOF = pygame.mixer.Sound("sounds/hit.ogg")
die = pygame.mixer.Sound("sounds/stink.ogg")


# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
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
        
    def move_right(self):
        self.rect.x += self.speed

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
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
            
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

        self.shield =  5
        
    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            EXPLOSION.play()
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            EXPLOSION.play()
            self.kill()
            
class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 15
    

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 60
        self.speed = 5
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
                m.rect.y += 32

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

    
# Make game objects
ship = Ship(384, 830, player)
lasers = []
mob1 = Mob(128, 30, enemy)
mob2 = Mob(256, 30, enemy)
mob3 = Mob(384, 30, enemy)
mob4 = Mob(512, 30, enemy)
mob5 = Mob(630, 30, enemy)
mob6 = Mob(128, 130, enemy)
mob7 = Mob(256, 130, enemy)
mob8 = Mob(384, 130, enemy)
mob9 = Mob(512, 130, enemy)
mob10 = Mob(630, 130, enemy)


# Make sprite groups
player = pygame.sprite.Group()
player.add(ship)

lasers = pygame.sprite.Group()

mobs = pygame.sprite.Group()
mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10)

bombs = pygame.sprite.Group()

# Make fleet
fleet = Fleet(mobs)

# Game loop
pygame.mixer.music.play(-1)
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
                
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        ship.move_left()
    elif pressed[pygame.K_RIGHT]:
        ship.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
    player.update(bombs)
    lasers.update()
    bombs.update()
    mobs.update(lasers)
    fleet.update()
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(background, [0,0])
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
