import pygame
import Wall
import math
import Enemy
import time
import random
pygame.init()
clock = pygame.time.Clock()
tilesize = 64
width = tilesize*18
height = tilesize*12
screen = pygame.display.set_mode((width,height))
#tileIMG = pygame.image.load('tile.jpg')
font = pygame.font.Font("frankknows.ttf", 48)
font2 = pygame.font.Font('spooky.ttf', 32)
charsize = 64
pumpkin = pygame.transform.scale(pygame.image.load('pumpkin.png'),(48,48))
charright = [pygame.transform.scale(pygame.image.load('Hansside1.png'),(charsize,charsize)),
            pygame.transform.scale(pygame.image.load('Hansside2.png'),(charsize,charsize)),
             pygame.transform.scale(pygame.image.load('Hansside1.png'),(charsize,charsize))]
charleft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('Hansside1.png'),(charsize,charsize)),1,0),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load('Hansside2.png'),(charsize,charsize)),1,0),
            pygame.transform.flip(pygame.transform.scale(pygame.image.load('Hansside1.png'),(charsize,charsize)),1,0)]
chardown = [pygame.transform.scale(pygame.image.load('Hans1.png'),(charsize,charsize)),
            pygame.transform.scale(pygame.image.load('Hans2.png'),(charsize,charsize)),
            pygame.transform.scale(pygame.image.load('Hans3.png'),(charsize,charsize))]
charup = [pygame.transform.scale(pygame.image.load('Hansback1.png'),(charsize,charsize)),
            pygame.transform.scale(pygame.image.load('Hansback2.png'),(charsize,charsize)),
            pygame.transform.scale(pygame.image.load('Hansback3.png'),(charsize,charsize))]

img1 = pygame.transform.scale(pygame.image.load("cupcake1.png"),(64,64))

icedeathimg = pygame.transform.scale(pygame.image.load('icedeath.png'),(320,320))
witchimg = pygame.transform.scale(pygame.image.load('deathscreen.png'),(320,320))
muffindeath = pygame.transform.scale(pygame.image.load('cupcakedeath.png'),(320,320))
bg = pygame.transform.scale(pygame.image.load('mainmenubg.png'),(width,height))
creditsbg = pygame.transform.scale(pygame.image.load('creditsbg.png'),(width,height))
heart = pygame.image.load('heart3.png')
heart2 = pygame.image.load('heart2.png')
heart3 = pygame.image.load('heart.png')
blacktile = pygame.image.load('blacktile.png') #0
candytile = pygame.transform.scale(pygame.image.load('candy_tile.png'),(64,64)) #1
yellowjello = pygame.transform.scale(pygame.image.load('yellojello_tile_.png'),(64,64)) #2
redjello = pygame.transform.scale(pygame.image.load('redjello_tile.png'),(64,64)) #3
greenjello = pygame.transform.scale(pygame.image.load('greenjello_tile_.png'),(64,64)) #4
gingertile = pygame.transform.scale(pygame.image.load('Biscuit_tile.png'),(64,64)) #5
caketile = pygame.transform.scale(pygame.image.load('cake_tile.png'),(64,64)) #6
carpettile = pygame.transform.scale(pygame.image.load('carpet.png'),(charsize,charsize)) #7
icecreamimg = pygame.transform.scale(pygame.image.load("icecream1.png"),(64,64))
breadIMG = pygame.transform.scale(pygame.image.load("breadcrumb.png"),(48,48))
charIMGs = [charright,charleft,charup,chardown,charup,charup,chardown,chardown]
breadx = -99999
bready = -99999
breadcount = 3
xscroll = 0
yscroll = 0
xscrolling = 0
yscrolling = 0
facing = 0 #0 right , 1 left , 2 up , 3 down, 4 right+up , 5 left+up,6 right+down,7 left + down
tilemap1 = [[2,3,4,2,3,4,3,3,2,3,3,4,4,3,3,2,3,2,2,4,2,2,3,3,4],
            [4,5,5,5,5,5,5,5,4,5,5,3,5,5,5,5,5,5,5,5,5,5,5,5,2],
            [4,5,5,5,5,5,5,5,3,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,2],
            [3,5,5,5,5,5,5,5,2,5,5,4,3,2,2,4,3,5,5,5,5,5,5,5,3],
            [2,5,5,5,5,5,5,5,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3],
            [3,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
            [4,5,5,5,5,4,3,2,3,4,2,3,5,5,5,3,4,3,2,2,5,5,5,5,4],
            [3,5,5,5,5,3,1,5,5,3,5,5,4,5,5,5,5,5,5,2,5,5,5,5,4],
            [3,5,5,5,5,3,5,5,5,2,5,5,5,5,5,5,5,5,5,3,5,5,5,5,3],
            [2,3,5,5,5,2,4,5,5,3,5,5,5,5,4,3,5,5,5,4,5,5,5,5,2],
            [2,5,4,3,4,4,3,5,5,4,2,4,4,3,3,4,2,5,5,3,3,5,5,5,3],
            [2,5,5,5,5,3,3,5,5,3,5,5,5,5,2,2,4,5,5,2,2,5,5,5,2],
            [4,5,5,5,5,2,4,5,5,2,5,5,5,5,5,5,5,5,5,3,4,3,5,5,3],
            [3,2,5,5,5,3,2,5,5,2,5,5,5,5,5,5,5,5,5,4,5,4,5,5,3],
            [4,5,5,5,5,5,5,5,5,3,4,3,2,3,3,5,5,2,3,4,5,4,5,5,4],
            [2,4,5,5,5,5,5,5,5,3,5,5,5,2,5,5,5,3,5,5,5,3,5,5,4],
            [2,5,2,5,5,5,3,5,5,4,5,5,5,3,2,5,5,4,2,2,3,4,3,3,4],
            [4,5,2,3,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,2],
            [3,4,4,3,4,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,3],
            [2,5,5,2,5,5,3,3,4,3,2,3,4,4,2,3,4,3,4,3,4,5,5,3,2],
            [2,5,5,4,5,5,2,3,4,3,4,3,3,2,2,2,3,4,3,5,2,5,5,2,2],
            [4,5,5,2,5,5,3,4,5,5,5,5,5,5,5,3,5,5,2,5,5,5,5,5,4],
            [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3],
            [3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
            [3,2,2,3,4,2,3,2,4,3,2,4,2,3,2,2,3,4,3,4,3,3,2,2,2]]

tilemap2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #0 = normal tile, 1 = blank tile,2 = wall
           [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
           [1,2,5,5,5,5,5,5,5,5,5,5,5,5,5,2,1],
           [1,2,5,5,5,5,5,5,5,5,5,5,5,5,5,2,1],
           [1,2,5,5,2,2,2,2,2,2,2,5,5,5,5,2,1],
           [1,2,5,5,2,5,5,5,5,5,2,2,5,5,5,2,1],
           [1,2,5,5,2,5,5,5,5,5,5,2,5,5,5,2,1],
           [1,2,5,5,2,5,5,5,5,5,5,2,2,5,5,2,1],
           [1,2,5,5,2,5,5,5,5,5,5,5,5,5,5,2,1],
           [1,2,5,1,2,5,5,5,5,5,5,5,5,5,5,2,1],
           [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

enemymap =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,4,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]#0 = empty 1 = horizontal_muffin 2 = vertical_muffin 3 = horizontal ice_cream 4 = vertical ice_cream
enemymap2 =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
            [0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
encountermap =  [[2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4],
            [3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
            [4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,3],
            [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
            [3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
            [4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,3],
            [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
            [3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
            [4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,3],
            [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
            [3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2],
            [4,2,3,4,2,3,4,2,3,4,2,3,4,2,3,4,2,3]]

startpointx = 3.5 #first tile x-loc
startpointy = 7 #first tile y-loc
startpointx2 = 0
startpointy2 = 0
menux = 200 #menustartloc
menuy = 490
charspeed = 0 #menuscrollspeed
walls = []
wallsstorage = []
xscrollstorage = 0
yscrollstorage = 0
levelone = False
leveltwo = False
level = 0
menu = True
player = screen.blit(charIMGs[facing][0], (544, 352))
flash = pygame.transform.scale(pygame.image.load('flashsmall.png'),(width,height)) #flashlight effect
enemies = [] #enemy list in maze
encounterstarted = False #to run encounter()
credits = False #to run credits()
facingcounter = 0
wonbool = False

pygame.mixer.init(channels = 4)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

menuselectsound = pygame.mixer.Sound('menuselect.mp3')
encountermusic = pygame.mixer.Sound('Alfs_Ship.mp3')
muffinhit = pygame.mixer.Sound('muffin_hit.mp3')
mazemusic = pygame.mixer.Sound('spookii_master2.mp3')
winencountersound = pygame.mixer.Sound('win_encounter.mp3')
deathsound = pygame.mixer.Sound('death_sound_v1.mp3')
pumpkinsound = pygame.mixer.Sound('taking_pumpkin.mp3')
foundencounter = pygame.mixer.Sound('found_encounter.mp3')
encountertimer = 0
def creditsf():
    global run, credits, menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                channel2.play(menuselectsound)
                credits = False
                menu = True
    screen.blit(creditsbg,(0,0))
    text = font2.render("CREDITS",True,((0,40,70)))
    screen.blit(text,(width/2-40,120))
    for i in range(4):
        text = font2.render(["Arinc Demir","Bora Depecik","Burcu Kilic","Uygar Apan"][i], True, (0,0,0))
        screen.blit(text, (width / 2 - 60, 195+i*90))
    text = font2.render("Press Esc to go back",True,(195,200,210))
    screen.blit(text,(450,height-100))


def levelstart(tilemap,breadcountp,enemymapp):
    global menu,level,levelone,walls,enemies,xscroll,yscroll,encountertimer, breadcount, leveltwo
    breadcount = breadcountp #to reset breadcount
    encountertimer = 0 #encounter invincibility for 1-2 sec
    channel1.play(mazemusic,loops=-1)
    xscroll = 0
    yscroll = 0
    if breadx > -90000: #if bread is placed
        xscroll = breadxscrollstorage
        yscroll = breadyscrollstorage
    enemies = []
    walls = []
    y = 0
    menu = False
    if tilemap == tilemap1:
        level = 1
        levelone = True
    if tilemap == tilemap2:
        level = 2
        leveltwo = True
    for i in tilemap: #set up walls
        x = 0
        for j in i :
            if j == 2 or j == 3 or j ==4:
                if level == 1:
                    walls.append(Wall.Wall(tilesize*x - (startpointx * tilesize) ,tilesize*y -(startpointy*tilesize),j,screen))
                if level == 2:
                    walls.append(Wall.Wall(tilesize * x - (startpointx2 * tilesize),tilesize * y - (startpointy2 * tilesize), j, screen))
            x+=1
        y+=1
    y = 0
    for i in enemymapp: #set up enemies
        x = 0
        for j in i:
            if level == 1:
                if j == 1:
                    enemies.append(Enemy.Enemy(tilesize*x - (startpointx * tilesize),tilesize*y-(startpointy*tilesize),screen,"muffin",-3,0))
                if j == 2:
                    enemies.append(Enemy.Enemy(tilesize * x -(startpointx * tilesize), tilesize * y -(startpointy*tilesize), screen, "muffin", 0, 3))
                if j == 3:
                    enemies.append(Enemy.Enemy(tilesize*x - (startpointx * tilesize),tilesize*y -(startpointy*tilesize),screen,"icecream",-3,0))
                if j == 4:
                    enemies.append(Enemy.Enemy(tilesize * x - (startpointx * tilesize), tilesize * y -(startpointy*tilesize), screen, "icecream", 0, 3))
            if level == 2:
                if j == 1:
                    enemies.append(Enemy.Enemy(tilesize * x - (startpointx2 * tilesize),tilesize * y - (startpointy2 * tilesize), screen, "muffin", -3, 0))
                if j == 2:
                    enemies.append(Enemy.Enemy(tilesize * x - (startpointx2 * tilesize),tilesize * y - (startpointy2 * tilesize), screen, "muffin", 0, 3))
                if j == 3:
                    enemies.append(Enemy.Enemy(tilesize * x - (startpointx2 * tilesize),tilesize * y - (startpointy2 * tilesize), screen, "icecream", -3, 0))
                if j == 4:
                    enemies.append(Enemy.Enemy(tilesize * x - (startpointx2 * tilesize),tilesize * y - (startpointy2 * tilesize), screen, "icecream", 0, 3))
            x+=1
        y+=1




def levelcontinue(enemiesp,wallsp,tilemap,xscrollp,yscrollp):
    global levelone,xscroll,yscroll,walls,enemies,leveltwo
    channel1.play(mazemusic, loops=-1)
    if tilemap == tilemap1:
        levelone = True
    if tilemap == tilemap2:
        leveltwo = True
    xscroll = xscrollp
    yscroll = yscrollp
    walls = wallsp
    enemies = enemiesp


def startEncounter(enemy):
    global encounterstarted,leveltwo, levelone,icecreamhp,xscroll,yscroll, walls, encountermap, icecreambullets, muffinbullets, hp, pumpkins, muffinhp,wallsstorage,yscrollstorage,xscrollstorage
    channel1.play(encountermusic,loops=-1)
    wallsstorage = walls
    xscrollstorage = xscroll
    yscrollstorage = yscroll
    hp = 3
    encounterstarted = True
    levelone = False
    leveltwo = False
    xscroll,yscroll = 0,0
    walls = []
    xscroll = 300
    y = 0
    if enemy.enemyType == "muffin":
        muffinbullets = []
        muffinhp = 10
    if enemy.enemyType == "icecream":
        icecreambullets = []
        icecreamhp = 6

    pumpkins = []

    for i in encountermap: #set up walls
        x = 0
        for j in i:
            if j == 2 or j == 3 or j == 4:
                walls.append(Wall.Wall(tilesize * x , tilesize * y , j, screen))
            x += 1
        y += 1
    return enemy

global c
c = 0
def Encounter(current_enemy):
    global facingcounter, player, icecreamhp,encounterseconds ,run, facing, xscrolling, yscrolling, xscroll, yscroll,c,hp,muffinhp,encounterstarted, enemies,breadcount
    screen.fill((0, 0, 0))
    encounterseconds -= 1/60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                xscrolling = 4
                if yscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 1
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                xscrolling = -4
                if yscrolling > 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 0
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                yscrolling = 4
                if xscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 2
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                yscrolling = -4
                if xscrolling > 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 3
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                if xscrolling > 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling > 0:
                    facing = 2
                elif yscrolling < 0:
                    facing = 3
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                if xscrolling < 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling > 0:
                    facing = 2
                elif yscrolling < 0:
                    facing = 3
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                if yscrolling > 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                if yscrolling < 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
    for wall in walls: #check collision
        xscroll, yscroll = wall.collide(xscrolling, yscrolling, facing, xscroll, yscroll, player)
    for wall in walls: #draw walls
        wall.draw(xscroll, yscroll)
    y = 0
    for tile in encountermap: #draw tiles
        x = 0
        for tiles in tile:
            if tiles == 0:
                screen.blit(blacktile, (tilesize * x + xscroll , tilesize * y + yscroll))
            if tiles == 1:
                screen.blit(candytile, (tilesize * x + xscroll, tilesize * y + yscroll))
            if tiles == 5:
                screen.blit(gingertile, (tilesize * x + xscroll , tilesize * y + yscroll))
            if tiles == 6:
                screen.blit(caketile, (tilesize * x + xscroll , tilesize * y + yscroll))
            if tiles == 7:
                screen.blit(carpettile, (tilesize * x + xscroll , tilesize * y + yscroll))
            x += 1
        y += 1
    if current_enemy.enemyType == "icecream":
        c+=1
        if c%75==0:
            t = random.randint(0,45)
            for angle in range(0+t,360+t,45):
                icecreambullets.append(Enemy.Bullet(width / 2 - 16, height / 2 - 16, 6 * math.cos(angle / 57.3),-6 * math.sin(angle / 57.3), screen,"icecream"))
        for bullet in icecreambullets:
            bulletrect = bullet.draw(xscroll, yscroll)
            if bulletrect.colliderect(player):
                channel2.play(muffinhit)
                icecreambullets.remove(bullet)
                hp -= 1
            if (bullet.x + xscroll <= 0) or (bullet.x + xscroll >= width) or (bullet.y + yscroll <= 0) or (bullet.y + yscroll >= height):
                icecreambullets.remove(bullet)
        text = font2.render("Ice Cream's HP", True, (210, 140, 190))
        screen.blit(text, (850, 65))
    if current_enemy.enemyType == "muffin":
        c+=1 #bullet timer
        if c%35==0:
            playerangle = 57.3*math.atan(-1*((height/2-16-(height/2-charsize/2+yscroll))/(width/2-16-(width/2-charsize/2+xscroll))))
            if xscroll > 0 :
                playerangle += 180
            angle = random.randint(int(playerangle-100),int(playerangle+100))
            muffinbullets.append(Enemy.Bullet(width/2-16 ,height/2-16 ,6*math.cos(angle/57.3),-6*math.sin(angle/57.3),screen,"muffin"))
        for bullet in muffinbullets:
            bulletrect = bullet.draw(xscroll, yscroll)
            if bulletrect.colliderect(player):
                channel2.play(muffinhit)
                muffinbullets.remove(bullet)
                hp -= 1
            if (bullet.x + xscroll <= 0) or (bullet.x + xscroll >= width) or (bullet.y + yscroll <= 0) or (
                    bullet.y + yscroll >= height):
                muffinbullets.remove(bullet)
        text = font2.render("Muffin's HP", True, (210, 140, 190))
        screen.blit(text, (850, 65))

    text = font2.render("Time : {:.2f}".format(encounterseconds), True, (240,250,255))
    screen.blit(text, (width/2-150, 20))

    if encounterseconds <= 0:
        hp = 0

    if random.randint(0,130)==1: #pumpkin spawn chance
        pumpkins.append([random.randint(64,width-128),random.randint(64,height-128),300])
    for pump in pumpkins:
        p = screen.blit(pumpkin, (pump[0] + xscroll, pump[1] + yscroll))
        pump[2] -= random.randint(0,3) #pumpkin hp remove
        if pump[2] <= 0 :
            pumpkins.remove(pump)
        if p.colliderect(player) and pump[2]>0:
            channel3.play(pumpkinsound)
            pumpkins.remove(pump)
            if current_enemy.enemyType == "muffin":
                muffinhp-=1
            if current_enemy.enemyType == "icecream":
                icecreamhp-=1




    text = font2.render("Your HP", True, (230,80,5))
    screen.blit(text,(50,65))
    for i in range(1,hp+1):
        screen.blit(heart,(200+i*50,65))
    for i in range(1,4-hp):
        screen.blit(heart3,(400-50*i,65))

    if current_enemy.enemyType == "muffin":
        if (muffinhp % 2) == 0:
            for i in range(1,(muffinhp//2)+1):
                screen.blit(heart,(520+50*i,65))
            for i in range(1,6-(muffinhp//2)):
                screen.blit(heart3,(820-50*i,65))
        else:
            for i in range(1,(muffinhp//2)+1):
                screen.blit(heart,(520+50*i,65))
            screen.blit(heart2,(520+50*((muffinhp//2)+1),65))
            for i in range(1,(6-((muffinhp+1)//2))):
                screen.blit(heart3,(820-50*i,65))
        if muffinhp == 0:
            if hp != 0:
                channel1.play(winencountersound)
                time.sleep(1)
                screen.fill((0,0,0))
                screen.blit(muffindeath,(width/2-160,100))
                text = font2.render("YOU WON THE ENCOUNTER",True,(155,12,12))
                screen.blit(text,(width/2-250,480))
                pygame.display.update()
                time.sleep(2.2)
                encounterstarted = False
                enemies.remove(current_enemy)
                if level == 1:
                    levelcontinue(enemies, wallsstorage, tilemap1, xscrollstorage, yscrollstorage)
                if level == 2:
                    levelcontinue(enemies, wallsstorage, tilemap2, xscrollstorage, yscrollstorage)
    if current_enemy.enemyType == "icecream":
        if (icecreamhp % 2) == 0:
            for i in range(1,(icecreamhp//2)+1):
                screen.blit(heart,(620+50*i,65))
            for i in range(1,4-(icecreamhp//2)):
                screen.blit(heart3,(820-50*i,65))
        else:
            for i in range(1,(icecreamhp//2)+1):
                screen.blit(heart,(620+50*i,65))
            screen.blit(heart2,(620+50*((icecreamhp//2)+1),65))
            for i in range(1,(4-((icecreamhp+1)//2))):
                screen.blit(heart3,(820-50*i,65))
        if icecreamhp == 0:
            if hp != 0:
                channel1.play(winencountersound)
                time.sleep(1)
                screen.fill((0,0,0))
                screen.blit(icedeathimg,(width/2-160,100))
                text = font2.render("YOU WON THE ENCOUNTER",True,(155,12,12))
                screen.blit(text,(width/2-250,480))
                pygame.display.update()
                time.sleep(2.2)
                encounterstarted = False
                enemies.remove(current_enemy)
                if level == 1:
                    levelcontinue(enemies, wallsstorage, tilemap1, xscrollstorage, yscrollstorage)
                if level == 2:
                    levelcontinue(enemies, wallsstorage, tilemap2, xscrollstorage, yscrollstorage)
    if hp == 0 : #death
        if current_enemy.enemyType == "muffin" and muffinhp !=0 or current_enemy.enemyType == "icecream" and icecreamhp != 0:
            channel1.play(deathsound)
            time.sleep(1)
            screen.fill((0,0,0))
            screen.blit(witchimg,(width/2-160,100))
            text = font2.render("YOU WERE TURNED INTO CANDY BY THE WITCH",True,(155,12,12))
            screen.blit(text,(width/2-400,480))
            pygame.display.update()
            time.sleep(4)
            if level == 1:
                levelstart(tilemap1,breadcount,enemymap)
            if level == 2:
                levelstart(tilemap2,breadcount,enemymap2)
            encounterstarted = False

    if (xscrolling==0) & (yscrolling==0):
        screen.blit(charIMGs[facing][0], (width/2 - charsize/2, height/2 - charsize/2))
    else:
        facingcounter+=1
        player = screen.blit(charIMGs[facing][int(facingcounter%30*0.1)], (width/2 - charsize/2, height/2 - charsize/2))

    facingcounter +=1
    if current_enemy.enemyType == "muffin":
        screen.blit(img1,(width/2 + xscroll-32,height/2 + yscroll-32))
    if current_enemy.enemyType == "icecream":
        screen.blit(icecreamimg,(width/2 + xscroll-32,height/2 + yscroll-32))
    xscroll += xscrolling
    yscroll += yscrolling


def mainmenu():
    global run,charspeed,menux, levelone, menu, credits,enemymap
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                charspeed = -5
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                charspeed = 5
            if (event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE):
                if menux > 200 and menux < 400:
                    channel2.play(menuselectsound)
                    levelstart(tilemap1,3,enemymap)
                if 700 > menux > 500:
                    channel2.play(menuselectsound)
                    credits = True
                    menu = False
                if menux > 800 and menux < 1000:
                    channel2.play(menuselectsound)
                    run = False

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                if charspeed < 0:
                    charspeed = 0
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                if charspeed > 0:
                    charspeed = 0
    fcounter = 0
    if charspeed > 0 :
        screen.blit(charright[int(facingcounter%30*0.1)],(menux,menuy))
    elif charspeed < 0 :
        screen.blit(charleft[int(facingcounter%30*0.1)],(menux,menuy))
    else:
        screen.blit(chardown[0], (menux, menuy))
    fcounter += 1
    menux += charspeed
    if menux + 128 > width:
        menux = width-128
    if menux < 0:
        menux = 0
    if menux > 200 and menux < 400:
        pygame.draw.rect(screen,(80,120,150),(200,400,200,60),border_radius=20)
    else:
        pygame.draw.rect(screen,(10,50,80),(200,400,200,60),border_radius=20)
    if menux > 500 and menux < 700:
        pygame.draw.rect(screen,(80,120,150),(500,400,200,60),border_radius=20)
    else:
        pygame.draw.rect(screen,(10,50,80),(500,400,200,60),border_radius=20)
    if menux > 800 and menux < 1000:
        pygame.draw.rect(screen,(80,120,150),(800,400,200,60),border_radius=20)
    else:
        pygame.draw.rect(screen,(10,50,80),(800,400,200,60),border_radius=20)

    text = font.render("Play",True,(195,200,220))
    screen.blit(text,(260,400))
    text = font.render("Credits", True, (195, 200, 220))
    screen.blit(text, (530, 400))
    text = font.render("Quit", True, (195, 200, 220))
    screen.blit(text, (860, 400))


def level1():
    global menu,facingcounter, levelone, player,encountertimer,encounterseconds,run,facing,xscrolling,yscrolling,xscroll,yscroll,collidecd,colliding,breadcount,breadx,bready,bread,breadxscrollstorage,breadyscrollstorage
    encountertimer += 1
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                channel1.stop()
                menu = True
                levelone = False
                breadx = -99999
                bready = -99999
            if event.key == pygame.K_SPACE:
                if breadcount>0:
                    breadx = width/2 - charsize/2 - xscroll
                    bready = height/2 - charsize/2 - yscroll
                    breadxscrollstorage = xscroll
                    breadyscrollstorage = yscroll
                    breadcount -=1
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                xscrolling = 4
                if yscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 1
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                xscrolling = -4
                if yscrolling > 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 0
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                yscrolling = 4
                if xscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 2
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                yscrolling = -4
                if xscrolling > 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 3
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                if xscrolling > 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling>0:
                    facing = 2
                elif yscrolling<0:
                    facing = 3
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                if xscrolling < 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling>0:
                    facing = 2
                elif yscrolling<0:
                    facing = 3
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                if yscrolling > 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                if yscrolling < 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
    for wall in walls:
        xscroll,yscroll = wall.collide(xscrolling, yscrolling, facing, xscroll, yscroll, player)
    for wall in walls:
        wall.draw(xscroll,yscroll)
    y=0
    for tile in tilemap1: #draw tiles only if they are in screen
        x = 0
        for tiles in tile:
            if 0 < (tilesize*x+xscroll-(startpointx*tilesize))< width or height > (tilesize*y+yscroll) > 0:

                if tiles == 0:
                    screen.blit(blacktile, (tilesize * x + xscroll - (startpointx * tilesize), tilesize * y + yscroll - (startpointy * tilesize)))
                if tiles == 1:
                    door = screen.blit(candytile, (tilesize * x + xscroll - (startpointx * tilesize), tilesize * y + yscroll - (startpointy * tilesize)))
                    if door.colliderect(player):
                        levelone = False
                        breadx = -99999
                        bready = -99999
                        levelstart(tilemap2,3,enemymap2)
                if tiles == 5:
                    screen.blit(gingertile, (tilesize * x + xscroll - (startpointx * tilesize), tilesize * y + yscroll - (startpointy * tilesize)))
                if tiles == 6:
                    screen.blit(caketile, (tilesize * x + xscroll - (startpointx * tilesize), tilesize * y + yscroll - (startpointy * tilesize)))
                if tiles == 7:
                    screen.blit(carpettile, (tilesize * x + xscroll - (startpointx * tilesize), tilesize * y + yscroll - (startpointy * tilesize)))
            x += 1
        y += 1
    if (xscrolling==0) & (yscrolling==0):
        screen.blit(charIMGs[facing][0], (width/2 - charsize/2, height/2 - charsize/2))
    else:
        facingcounter+=1
        player = screen.blit(charIMGs[facing][int(facingcounter%30*0.1)], (width/2 - charsize/2, height/2 - charsize/2))
    bread = screen.blit(breadIMG,(breadx+xscroll,bready+yscroll))
    for enemy in enemies:
        enemy.draw(xscroll,yscroll)
        if enemy.encounter(xscroll,yscroll) and encountertimer > 80: #encounter
            encounterseconds = [100,60][["muffin","icecream"].index(enemy.enemyType)]
            channel2.play(foundencounter)
            global encountered_enemy
            screen.fill((0,0,0))
            time.sleep(1)
            text = font2.render("DODGE THE "+["MUFFINS","ICE CREAMS"][["muffin","icecream"].index(enemy.enemyType)],True,(230,80,5))
            screen.blit(text,(width/2-180-35*(enemy.enemyType=="icecream"),height/2-100))
            text = font2.render("COLLECT THE PUMPKINS", True, (230, 80, 5))
            screen.blit(text, (width / 2 - 220, height / 2 +50))
            pygame.display.update()
            time.sleep(2)
            encountered_enemy = startEncounter(enemy)
            break

    screen.blit(flash,(0,0))
    text = font2.render("Bread : "+str(breadcount),True,(200,210,215))
    screen.blit(text,(50,height-50))
    text = font2.render("Level : 1", True, (200, 210, 215))
    screen.blit(text, (900, height - 50))
    xscroll += xscrolling
    yscroll += yscrolling


def level2():
    global menu, leveltwo, wonbool,level, facingcounter, levelone, player, encountertimer, encounterseconds, run, facing, xscrolling, yscrolling, xscroll, yscroll, collidecd, colliding, breadcount, breadx, bready, bread, breadxscrollstorage, breadyscrollstorage
    encountertimer += 1
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                channel1.stop()
                menu = True
                leveltwo = False
                breadx = -99999
                bready = -99999
                level = 0
            if event.key == pygame.K_SPACE:
                if breadcount > 0:
                    breadx = width / 2 - charsize / 2 - xscroll
                    bready = height / 2 - charsize / 2 - yscroll
                    breadxscrollstorage = xscroll
                    breadyscrollstorage = yscroll
                    breadcount -= 1
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                xscrolling = 4
                if yscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 1
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                xscrolling = -4
                if yscrolling > 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif yscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 0
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                yscrolling = 4
                if xscrolling > 0:
                    facing = 5
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 4
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 2
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                yscrolling = -4
                if xscrolling > 0:
                    facing = 7
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                elif xscrolling < 0:
                    facing = 6
                    xscrolling = xscrolling / math.sqrt(2)
                    yscrolling = yscrolling / math.sqrt(2)
                else:
                    facing = 3
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                if xscrolling > 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling > 0:
                    facing = 2
                elif yscrolling < 0:
                    facing = 3
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                if xscrolling < 0:
                    xscrolling = 0
                yscrolling *= math.sqrt(2)
                if yscrolling > 0:
                    facing = 2
                elif yscrolling < 0:
                    facing = 3
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                if yscrolling > 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
            if (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                if yscrolling < 0:
                    yscrolling = 0
                xscrolling *= math.sqrt(2)
                if xscrolling > 0:
                    facing = 1
                elif xscrolling < 0:
                    facing = 0
    for wall in walls:
        xscroll, yscroll = wall.collide(xscrolling, yscrolling, facing, xscroll, yscroll, player)
    for wall in walls:
        wall.draw(xscroll, yscroll)
    y = 0
    for tile in tilemap2:  # draw tiles only if they are in screen
        x = 0
        for tiles in tile:
            if 0 < (tilesize * x + xscroll - (startpointx2 * tilesize)) < width or height > (tilesize * y + yscroll - (startpointy2 * tilesize)) > 0:

                if tiles == 0:
                    screen.blit(blacktile, (tilesize * x + xscroll - (startpointx2 * tilesize), tilesize * y + yscroll - (startpointy2 * tilesize)))
                if tiles == 1:
                    door = screen.blit(candytile,(tilesize * x + xscroll - (startpointx2 * tilesize), tilesize * y + yscroll - (startpointy2 * tilesize)))
                    if door.colliderect(player):
                        leveltwo = False
                        wonbool = True
                if tiles == 5:
                    screen.blit(gingertile, (tilesize * x + xscroll - (startpointx2 * tilesize), tilesize * y + yscroll - (startpointy2 * tilesize)))
                if tiles == 6:
                    screen.blit(caketile, (tilesize * x + xscroll - (startpointx2 * tilesize), tilesize * y + yscroll - (startpointy2 * tilesize)))
                if tiles == 7:
                    screen.blit(carpettile, (tilesize * x + xscroll - (startpointx2 * tilesize), tilesize * y + yscroll - (startpointy2 * tilesize)))
            x += 1
        y += 1
    if (xscrolling == 0) & (yscrolling == 0):
        screen.blit(charIMGs[facing][0], (width / 2 - charsize / 2, height / 2 - charsize / 2))
    else:
        facingcounter += 1
        player = screen.blit(charIMGs[facing][int(facingcounter % 30 * 0.1)],
                             (width / 2 - charsize / 2, height / 2 - charsize / 2))
    bread = screen.blit(breadIMG, (breadx + xscroll, bready + yscroll))
    for enemy in enemies:
        enemy.draw(xscroll, yscroll)
        if enemy.encounter(xscroll, yscroll) and encountertimer > 80:  # encounter
            encounterseconds = [100, 60][["muffin", "icecream"].index(enemy.enemyType)]
            channel2.play(foundencounter)
            global encountered_enemy
            screen.fill((0, 0, 0))
            time.sleep(1)
            text = font2.render("DODGE THE " + ["MUFFINS", "ICE CREAMS"][["muffin", "icecream"].index(enemy.enemyType)],
                                True, (230, 80, 5))
            screen.blit(text, (width / 2 - 180 - 35 * (enemy.enemyType == "icecream"), height / 2 - 100))
            text = font2.render("COLLECT THE PUMPKINS", True, (230, 80, 5))
            screen.blit(text, (width / 2 - 220, height / 2 + 50))
            pygame.display.update()
            time.sleep(2)
            encountered_enemy = startEncounter(enemy)
            break

    screen.blit(flash, (0,0))
    text = font2.render("Bread : " + str(breadcount), True, (200, 210, 215))
    screen.blit(text, (50, height - 50))
    text = font2.render("Level : 2", True, (200, 210, 215))
    screen.blit(text, (900, height - 50))
    xscroll += xscrolling
    yscroll += yscrolling

def won():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    screen.blit(creditsbg,(0,0))
    text = font2.render("YOU ESCAPED THE WITCH'S HOUSE!",True,(140,27,10))
    screen.blit(text,(width/2-350,60))

run = True
while run:
    if wonbool:
        won()
    if menu:
        mainmenu()
    if levelone:
        level1()
    if leveltwo:
        level2()
    if encounterstarted:
        global encountered_enemy
        Encounter(encountered_enemy)
    if credits:
        creditsf()
    clock.tick(60)
    pygame.display.update()

pygame.quit()