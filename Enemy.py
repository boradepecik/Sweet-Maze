import pygame
import math
width = 64*18
height = 64*12
charsize = 64
img1 = pygame.transform.scale(pygame.image.load("cupcake1.png"),(64,64))
img2 = pygame.transform.scale(pygame.image.load("cupcake2.png"),(64,64))
img3 = pygame.transform.scale(pygame.image.load("cupcake3.png"),(64,64))

icecreamimg1 = pygame.transform.scale(pygame.image.load("icecream1.png"),(64,64))
icecreamimg2 = pygame.transform.scale(pygame.image.load("icecream2.png"),(64,64))
icecreamimg3 = pygame.transform.scale(pygame.image.load("icecream3.png"),(64,64))
icecreamimg4 = pygame.transform.scale(pygame.image.load("icecream4.png"),(64,64))
icecreams = [icecreamimg1,icecreamimg2,icecreamimg3,icecreamimg4]
cupcakes = [img1,img2,img3]
muffin = pygame.transform.scale(pygame.image.load('cupcake.png'),(64,64))
icecreambullet = pygame.transform.scale(pygame.image.load('iceprojectile.png'),(48,48))
class Enemy():
    def __init__(self, x, y, screen, enemyType,xspeed,yspeed):
        self.enemyType = enemyType
        self.screen = screen
        self.x=x
        self.y=y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.a = 0
    def draw(self,xscroll,yscroll):
        if 0 < self.x + xscroll < width or height > self.y + yscroll > 0:
            if self.enemyType == "muffin":
                self.screen.blit(cupcakes[int(self.a%30*0.1)],(self.x+xscroll,self.y+yscroll))
            if self.enemyType == "icecream":
                self.screen.blit(icecreams[int(self.a%30*0.1)],(self.x+xscroll,self.y+yscroll))
        self.x += self.xspeed
        self.y += self.yspeed
        self.a += 1
        if self.a >= 120: #patrol time
            self.xspeed = -self.xspeed
            self.yspeed = -self.yspeed
            self.a = 0
    def encounter(self,xscroll,yscroll):
        return math.hypot(self.x+xscroll + 32-width/2,self.y+yscroll+32-height/2) < 120



class Bullet:
    def __init__(self,x,y,xspeed,yspeed,screen,type):
        self.x=x
        self.y=y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.screen= screen
        self.type = type
    def draw(self,xscroll,yscroll):
        if self.type == "muffin":
            bulletrect = self.screen.blit(muffin,(self.x+xscroll,self.y+yscroll))
        if self.type == "icecream":
            bulletrect = self.screen.blit(icecreambullet, (self.x + xscroll, self.y + yscroll))
        self.x += self.xspeed
        self.y += self.yspeed
        return bulletrect

