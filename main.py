import pygame, random, sys
pygame.init()

WW = 800
WH = 600


screen = pygame.display.set_mode((WW, WH))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))        
        self.speed = 0
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))
class Colona:
    def __init__(self, x, img_path):
        r = random.randint(WH / 2, WH - 50)

        

        #x = WW+50
        self.rect_bot = pygame.Rect(x, r, 50, 400)
        self.rect_top = pygame.Rect(x, r - 150 - 400, 50, 400)

        self.img_bot = pygame.transform.scale(pygame.image.load(img_path), (50, 400))
        self.img_top = pygame.transform.scale(pygame.image.load(img_path), (50, 400))

    def draw(self):
        pygame.draw.rect(screen, (100,255,100), self.rect_bot)
        pygame.draw.rect(screen, (100,255,100), self.rect_top)


Colona_nag = [0]*5
for i in range(5):
    Colona_nag[i] = Colona(WW + 200 * i,  'трубы.png')

player = Player(50,WH/2,50,50,"птичка.png")


w = 5

while True:
    screen.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                player.speed -= 13
    if player.speed < 0:
        player.speed += 1
    if Colona_nag[0].rect_bot.x <= -50:
        for i in range(4):
            Colona_nag[i] = Colona_nag[i+1]
        Colona_nag[4] = Colona(950, 'трубы.png')

    for i in range(5):
        Colona_nag[i].rect_bot.x -= 3
        Colona_nag[i].rect_top.x -= 3
    for i in range(5):
        Colona_nag[i].draw()
    player.rect.y += w + player.speed
    player.draw()
    pygame.display.update()
    clock.tick(60)
