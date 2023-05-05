import pygame as pg

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

    if keys[pg.K_SPACE] or keys[pg.K_w]:
        player.jump()
    if player.isJumping:
        player.jumpContinue()

    if keys[pg.K_s]:
        player.crouch()
        pass
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