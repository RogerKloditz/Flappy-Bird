import pygame, sys
from random import randint

pygame.init()

win = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

B_COL = (67,197,57)
P_COL = (197,66,47)
BG_COL = (220,220,220)
T_COL = (255,0,0)

class Player():

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0

    def draw(self,win):
        pygame.draw.rect(win,B_COL,(self.x,self.y,self.width,self.height),3)

class Pillar():

    def __init__(self):
        self.width = 10
        self.vel = 2
        self.x = win.get_width() - self.width
        self.hole_height = 100
        self.upper_start = -10
        self.lower_end = win.get_height() + 10
        self.upper_end = randint(20,self.lower_end - self.hole_height - 20)
        self.lower_start = self.upper_end + self.hole_height

    def draw(self,win):
        pygame.draw.rect(win,P_COL,(self.x,self.upper_start,self.width,self.upper_end),3)
        pygame.draw.rect(win,P_COL,(self.x,self.lower_start,self.width,self.lower_end),3)

def redrawGameWindow():
    win.fill(BG_COL)
    bird.draw(win)
    for pillar in pillars:
        pillar.draw(win)
    pygame.display.update()

def birdFall():
    if bird.y + bird.height < 390:
        bird.y -= bird.vel
    else:
        return loseMessage()
    
    if bird.vel > -10:
        bird.vel -= 1

def birdFly():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.vel = 5

def pillarsMove(pillars):
    if pillars:
        if pillars[-1].x == 600:
            pillars.append(Pillar())

        for pillar in pillars:
            pillar.x -= pillar.vel
        if pillars[0].x < 0:
            pillars.pop(0)

    else:
        pillars.append(Pillar())

    return pillars

def birdHit(pillar):
    hitLeft = (bird.x + bird.width) > (pillar.x)
    hitRight = (bird.x) < (pillar.x + pillar.width)
    hitUp = (bird.y) < (pillar.upper_end)
    hitBottom = (bird.y + bird.height) > (pillar.lower_start)

    if hitLeft and hitRight and (hitUp or hitBottom):
        return loseMessage()

def loseMessage():
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render('You Lost',1,T_COL)
    win.blit(text,((win.get_width() - text.get_width()) / 2,50))
    pygame.display.update()
    pygame.time.wait(1000)

    return True

bird = Player(30,30,30,30)
pillars = []

while True:

    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    birdFly()
    pillars = pillarsMove(pillars)
    fallen = birdFall()
    hit = birdHit(pillars[0])
    if fallen or hit:
        break
    
    redrawGameWindow()




pygame.quit()
sys.exit()