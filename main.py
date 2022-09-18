import pygame as pg
import neat
import os.path
import sys
import queue
import random

from Player import *
from BackGround import *
from Obstacle import *

class Game():
    def __init__(self, genomes, config):
        pg.init()
        pg.font.init()

        self.Clock = pg.time.Clock()
        self.width = 1280
        self.height = 720
        self.running = True

        self.window = pg.display.set_mode((self.width, self.height))

        self.Reset(genomes, config)

    def Reset(self, genomes, config):

        self.obs_index = 0

        self.nets = []
        self.ge = []
        self.dinos = []

        self.bg = BackGround()
        self.bgGroup = pg.sprite.Group()
        self.bgGroup.add(self.bg)

        self.DinoGroup = pg.sprite.Group()

        for n, g in genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
            self.nets.append(net)

            dino = Dino()
            self.dinos.append(dino)
            self.DinoGroup.add(dino)

            g.fitness = 0
            self.ge.append(g)

        self.obstacleGroup = pg.sprite.Group()
        self.obstacleQueue = queue.Queue()
        self.obstacleArr = []

        self.detailGroup = pg.sprite.Group()
        self.detailQueue = queue.Queue()

        self.loadSprites()

        self.score = 0
        self.running = True

        self.run()

    def loadSprites(self):
        self.obsArr = []
        self.cloudArr = []
        for i in range(0,2):
            self.obsArr.append(pg.image.load("Sprites/Obstacle/"+  str(i+1) + ".png" ))
        for i in range (0,3):
            self.cloudArr.append(pg.image.load("Sprites/Clouds/"+  str(i+1) + ".png" ))

        self.fnt = pg.font.Font("Sprites/PixelFont.ttf",24 )

    def gameOver(self):
        while True:
            self.draw()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.Reset()

    def genCloud(self):
        sprite = self.cloudArr[random.randint(0, 2)]
        self.dist = random.randint(400, 600)
        y = random.randint(0, 200) + random.randint(-50, 50) + random.randint(50, 50)
        detail = Obstacle(self.width, y, sprite, 1, 1)
        if (self.detailQueue.empty()):
            self.detailGroup.add(detail)
            self.detailQueue.put(detail)
            return

        if (self.detailQueue.queue[-1].rect.topleft[0] < self.width - self.dist):
            self.detailGroup.add(detail)
            self.detailQueue.put(detail)

        if (self.detailQueue.queue[0].rect.topright[0] < 0):
            tempObj = self.detailQueue.get()
            tempObj.kill()

    def genObstacle(self):
        num = random.randint(0,1)
        sprite = self.obsArr[num]
        self.dist = 800
        obstacle = Obstacle(self.width, 330, sprite, num)

        if(self.obstacleQueue.empty()):
            self.obstacleGroup.add(obstacle)
            self.obstacleQueue.put(obstacle)
            self.obstacleArr.append(obstacle)
            return

        if(self.obstacleQueue.queue[-1].rect.topleft[0]< self.width - self.dist):
            self.obstacleGroup.add(obstacle)
            self.obstacleQueue.put(obstacle)
            self.obstacleArr.append(obstacle)

        if(self.obstacleQueue.queue[0].rect.topright[0] < 150):
            tempObj = self.obstacleQueue.get(0)
            self.obs_index += 1
            tempObj.kill()

    def getInput(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()

    def draw(self):
        self.window.fill((255,255,255))
        self.bgGroup.draw(self.window)
        self.obstacleGroup.draw(self.window)
        self.DinoGroup.draw(self.window)
        self.detailGroup.draw(self.window)
        self.drawScore()
        pg.display.flip()

    def drawScore(self):
        surf_text = self.fnt.render( str( int(self.ge[0].fitness) ) , True, "black")
        self.window.blit(surf_text, (1100, 50))

    def update(self):
        self.bgGroup.update()
        self.obstacleGroup.update()
        self.DinoGroup.update()
        self.genObstacle()
        self.genCloud()
        self.detailGroup.update()
        self.checkCollision()
        for x, dino in enumerate(self.dinos):
            self.ge[x].fitness += 0.1
            output = self.nets[x].activate((dino.x, self.obstacleQueue.queue[0].rect.x, dino.canJump))
            if output[0]> 0.5:
                if dino.canJump:
                    dino.jump()

    def checkCollision(self):
        for sprite in self.obstacleGroup:
            for rectbox in sprite.rectarray:
                for x, dino in enumerate(self.dinos):
                    if rectbox.colliderect(dino.rect):
                        self.ge[x].fitness -= 10
                        self.dinos.pop(x)
                        self.nets.pop(x)
                        self.DinoGroup.remove(dino)

    def run(self):
        while self.running and len( self.dinos ) > 0:
            self.Clock.tick(144)

            self.getInput()
            self.update()

            self.draw()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(Game, 5)
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)

