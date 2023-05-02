import pygame as pg

pg.init()
pg.display.set_caption("Cloaked Crossing")
pg.display.set_icon(pg.image.load("images\\icon.jpg"))
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

        self.vel_y = 0

        self.gravity = 1
        self.isPlayerFalling = False

        self.movementSpeed = 2
        self.playerModel = playerModel
        self.playerEntity = pg.transform.scale(pg.image.load(playerModel), (30, 60))

        

    def movePlayer(self, x, y):
        self.posX = x
        self.posY = y

        if self.posX < screen.get_width()-screen.get_width():
            self.posX = screen.get_width()-screen.get_width()
        elif self.posX > screen.get_width()-30:
            self.posX = screen.get_width()-30

        screen.blit(self.playerEntity, (self.posX, self.posY))

    def renderPlayer(self):
        screen.blit(self.playerEntity, (self.posX, self.posY))

    def jump(self):

        pass

    def attackLight(self):
        print("attack")

    def attackHeavy(self):
        pass




player = Player("images\\stickFigure.png")

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    level = Level()
    level.drawFloor()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w] or keys[pg.K_SPACE]:
        ## jump
        player.jump()
        player.renderPlayer()
        pass
    if keys[pg.K_s]:
        ## crouch
        pass
    if keys[pg.K_a]:
        player.movePlayer(player.posX-player.movementSpeed, player.posY)
    if keys[pg.K_d]:
        player.movePlayer(player.posX+player.movementSpeed, player.posY)

    player.renderPlayer()


    # flip() the display to put your work on screen
    pg.display.flip()

    dt = clock.tick(144) / 1000

pg.quit()