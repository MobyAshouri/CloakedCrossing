import pygame as pg
import math

pg.init()
pg.display.set_caption("Cloaked Crossing")
pg.display.set_icon(pg.image.load("images/icon.jpg"))

screenWidth = 1280
screenHeight = 720

screen = pg.display.set_mode((screenWidth, screenHeight))
clock = pg.time.Clock()
dt = 0


class Level:

    def __init__(self) -> None:
        self.floorY = 600
        self.pastMenu = True
        self.running = True
        

    def drawFloor(self):
        pg.draw.rect(screen, "black", pg.Rect(0, self.floorY, 1280, 120))

    def drawMenu(self):
        startButtonWidth = 450
        startButtonHeight = 180
        startButton = pg.image.load("images/menu/assets/startButton.png")
        startButton = pg.transform.scale(startButton, (startButtonWidth, startButtonHeight))
        screen.blit(startButton, (((screenWidth/2)-(startButtonWidth/2)), 200))

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            if (468 <= mouse[0]<=816 and 218 <= mouse[1] <= 365):
                self.pastMenu = True
                self.running = False
                level.fadeOut()

    def fadeOut(self):
        fade = pg.Surface((screenWidth, screenHeight))
        fade.fill((0,0,0))
        fade.set_alpha(0)
        for alpha in range(0,255):
            fade.set_alpha(alpha)          #kind of works
            screen.blit(fade, (0,0))
            pg.display.update()
            pg.time.delay(5)




class Player:

    def __init__(self, playerModel) -> None:
        self.posX = 100
        self.posY = 540
        self.playerHeight = 60
        self.playerWidth = 30

        self.jumpHeight = 22
        self.jumpCounter = self.jumpHeight
        self.isJumping = False
        self.gravity = 1

        self.isSprinting = False
        self.sprintSpeed = 5      # speed added to base movement speed for sprint

        self.movementSpeed = 5
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
        self.isJumping = True

    def jumpContinue(self):
        if self.jumpCounter >= -self.jumpHeight:
            self.posY -= .05 * (self.jumpCounter*abs(self.jumpCounter))         # ax^2
            self.jumpCounter-=1
        else:
            self.jumpCounter = self.jumpHeight
            self.isJumping = False

    def crouch(self):
        if not self.isJumping:
            print("crouch")

    def sprint(self):
        self.isSprinting = True

    def sprintContinue(self):
        if keys[pg.K_d]:
            self.posX+=self.sprintSpeed
        elif keys[pg.K_a]:
            self.posX-=self.sprintSpeed
        else:
            self.isSprinting = False


    def attackLight(self):
        print("attack")

    def attackHeavy(self):
        pass


player = Player("images/stickFigure.png")
level = Level()

while level.running:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            level.running = False
            level.pastMenu = False
    screen.fill("white")
    level.drawMenu()

    pg.display.flip()
    dt = clock.tick(144) / 1000


while level.pastMenu:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            level.pastMenu = False

    screen.fill("white")
    level.drawFloor()

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] or keys[pg.K_w]:
        player.jump()
    if player.isJumping:
        player.jumpContinue()

    if keys[pg.K_s]:
        player.crouch()
    if keys[pg.K_a]:
        player.movePlayer(player.posX-player.movementSpeed, player.posY)
    if keys[pg.K_d]:
        player.movePlayer(player.posX+player.movementSpeed, player.posY)

    if keys[pg.K_LSHIFT]:
        player.sprint()
    if player.isSprinting:
        player.sprintContinue()

    player.posY += player.gravity

    if player.posX < screen.get_width()-screen.get_width():
        player.posX = screen.get_width()-screen.get_width()
    elif player.posX > screen.get_width()-30:
        player.posX = screen.get_width()-30

    if player.posY > level.floorY-60:
        player.posY = level.floorY-60


    player.renderPlayer()

    # flip() the display to put your work on screen
    pg.display.flip()

    player.spriteCounter+=1
    dt = clock.tick(144) / 1000

pg.quit()