import pygame as pg
import math

pg.init()
pg.display.set_caption("Cloaked Crossing")
pg.display.set_icon(pg.image.load("images/icon.jpg"))
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
dt = 0



class Level:

    def __init__(self) -> None:
        self.floorY = 600

    def drawFloor(self):
        pg.draw.rect(screen, "black", pg.Rect(0, self.floorY, 1280, 120))




class Player:

    def __init__(self, playerModel) -> None:
        self.posX = 100
        self.posY = 540
        self.playerHeight = 60
        self.playerWidth = 30

        self.jumpVelocity = 1
        self.currentJumpHeight = 0
        self.maxJumpHeight = 25

        self.gravity = 4
        self.isFalling = False
        self.isGrounded = True

        self.movementSpeed = 3
        self.playerModel = playerModel
        self.playerEntity = pg.transform.scale(pg.image.load(self.playerModel), (self.playerWidth, self.playerHeight))

        self.spriteCounter = 0

        self.idleSprites = [
            "images/idle/idle1.png",
            "images/idle/idle2.png",
            "images/idle/idle3.png",
            "images/idle/idle4.png",
        ]
        self.runRightSprites = [
            "images/runRight/runRight1.png",
            "images/runRight/runRight2.png",
            "images/runRight/runRight3.png",
            "images/runRight/runRight4.png",
            "images/runRight/runRight5.png",
            "images/runRight/runRight6.png",
        ]

        

    def movePlayer(self, x, y):
        self.posX = x
        self.posY = y

    def renderPlayer(self):
        self.playerEntity = pg.transform.scale(pg.image.load(self.playerModel), (self.playerWidth, self.playerHeight))
        screen.blit(self.playerEntity, (self.posX, self.posY))

    def jump(self):
        if self.currentJumpHeight < self.maxJumpHeight:     ## check to see if current JH is at 0 instead
            self.isGrounded = False
            self.currentJumpHeight += self.jumpVelocity
            self.posY -= self.currentJumpHeight

        elif self.currentJumpHeight >= self.maxJumpHeight and self.isGrounded:
            self.currentJumpHeight = 0

        print(self.currentJumpHeight)

    def crouch(self):
        if self.isGrounded:
            print("crouch")


    def attackLight(self):
        print("attack")

    def attackHeavy(self):
        pass




player = Player("images/stickFigure.png")

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    player.spriteCounter+=1

    level = Level()
    level.drawFloor()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w] or keys[pg.K_SPACE]:
        ## jump
        player.jump()        
        pass
    if keys[pg.K_s]:
        player.crouch()
        pass
    if keys[pg.K_a]:
        player.movePlayer(player.posX-player.movementSpeed, player.posY)
    if keys[pg.K_d]:
        player.movePlayer(player.posX+player.movementSpeed, player.posY)

    player.posY += player.gravity

    if player.posX < screen.get_width()-screen.get_width():
        player.posX = screen.get_width()-screen.get_width()
    elif player.posX > screen.get_width()-30:
        player.posX = screen.get_width()-30

    if player.posY > level.floorY-60:
        player.isGrounded = True
        player.posY = level.floorY-60

    if not(player.isGrounded):
        player.movementSpeed = 5
    elif player.isGrounded:
        player.movementSpeed = 5

    player.renderPlayer()

    # flip() the display to put your work on screen
    pg.display.flip()

    player.spriteCounter+=1
    dt = clock.tick(144) / 1000

pg.quit()