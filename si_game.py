import pygame

pygame.init()

win = pygame.display.set_mode((750 ,750))

pygame.display.set_caption('Space Invaders')

black =(0,0,0)
white = (255 ,255 ,255)
green =(0 , 200 ,0)
red = (255 , 0 ,0)


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.Surface([50 ,25])
        self.image.fill(green)
        self.rect =self.image.get_rect()
        self.live = 5

    def draw(self):
        win.blit(self.image , (self.rect.x , self.rect.y))

        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25 ,25])
        self.image.fill(white)
        self.rect = self.image.get_rect()

class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8 ,8])
        self.image.fill(green)
        self.rect = self.image.get_rect()

ship = Ship()
ship.rect.x = 375
ship.rect.y = 650
        
enemy_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()


for row in range(1,6):
    for col in range(1,11):
        enemy = Enemy()
        enemy.rect.x =80 +(50 * col)
        enemy.rect.y =25 +(50 * row)
        enemy_list.add(enemy)

for bunk in range(3):
    for row in range(5):
        for col in range(10):
            bunker = Bunker()
            bunker.rect.x = (50 +(275 * bunk))+(10 * col)
            bunker.rect.y = 500 + (10 * row)
            bunker_list.add(bunker)
            
def redraw():
    win.fill(black)
    ship.draw()
    enemy_list.draw(win)
    bunker_list.draw(win)
    pygame.display.update()



run =True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        ship.rect.x += -10
    if key[pygame.K_RIGHT]:
        ship.rect.x += 10
    redraw()

pygame.quit()
