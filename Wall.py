import math

import pygame
width = 64*18
height = 64*12
charsize = 64

yellowjello = pygame.transform.scale(pygame.image.load('yellojello_tile_.png'),(64,64)) #2
redjello = pygame.transform.scale(pygame.image.load('redjello_tile.png'),(64,64)) #3
greenjello = pygame.transform.scale(pygame.image.load('greenjello_tile_.png'),(64,64)) #4
collisionsize = 5
class Wall:
    def __init__(self,x,y,material,screen):
        self.x = x
        self.y = y
        self.material = material
        self.screen = screen
        self.w = self.screen.blit([yellowjello,redjello,greenjello][self.material-2],(self.x,self.y))
    def draw(self,xscroll,yscroll):
        if 0 < self.x + xscroll < width or height > self.y + yscroll > 0:
            self.w = self.screen.blit([yellowjello,redjello,greenjello][self.material-2],(self.x+xscroll,self.y+yscroll))


    def collide(self,xscrolling,yscrolling,facing,xscroll,yscroll,player):
        #if (((width/2+charsize/2)>=self.x+xscroll>=(width/2-3*charsize/2))&((height/2-charsize)<=self.y+yscroll<=(height/2-charsize/2))):
        #RIGHT COLLISION
        if (476<=self.x+xscroll<=480)&(352-64<=self.y+yscroll<=416):
            xscroll -= collisionsize
        #LEFT COLLISION
        if (604<=self.x+xscroll<=612)&(352-64<=self.y+yscroll<=416):
            xscroll += collisionsize
        #DOWN COLLISION
        if (476<=self.x+xscroll<=604)&(416<=self.y+yscroll<=420):
            yscroll += collisionsize
        #UP COLLISION
        if (476<=self.x+xscroll<=604)&(288<=self.y+yscroll<=292):
            yscroll -= collisionsize

        return xscroll,yscroll

        #width/2 - charsize/2


"""
        if pygame.Rect.colliderect(player,self.w):
            return True
            if facing == 0:
                xscroll += collisionsize
            if facing == 1:
                xscroll -= collisionsize
            if facing == 2:
                yscroll -= collisionsize
            if facing == 3:
                yscroll += collisionsize
            if facing == 4:
                xscroll += collisionsize/math.sqrt(2)
                yscroll -= collisionsize/math.sqrt(2)
            if facing == 5:
                xscroll -= collisionsize/math.sqrt(2)
                yscroll -= collisionsize/math.sqrt(2)
            if facing == 6:
                xscroll += collisionsize/math.sqrt(2)
                yscroll += collisionsize/math.sqrt(2)
            if facing == 7:
                xscroll -= collisionsize/math.sqrt(2)
                yscroll += collisionsize/math.sqrt(2)
        else:
            return False

    """

