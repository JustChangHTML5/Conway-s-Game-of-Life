import pygame
import gv
import sys
import math
from lifeMatrix import *

mixer = pygame.mixer
mixer.init()
pygame.init()

size = (gv.width * gv.sizeFactor, gv.height * gv.sizeFactor)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (98, 159, 134)
color2 = (157, 96, 121)

gv.Game = Matrix()
gv.GameF = Matrix()
gv.Game.build(gv.width, gv.height)
gv.GameF.build(gv.width, gv.height)
gv.Game.NodesData = gv.GameF.NodesData
gv.isRunning = False

def check(node):
    neighbors = 0
    if gv.Game.get(node.Xm - 1, node.Ym + 1).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm, node.Ym + 1).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym + 1).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm - 1, node.Ym).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm - 1, node.Ym - 1).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm, node.Ym - 1).key == 1:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym - 1).key == 1:
        neighbors += 1

    return neighbors


def update():
    gv.Game.transmit(gv.GameF)
    for node in gv.GameF.Nodes:
        neighbors = check(gv.Game.get(node.Xm, node.Ym))
        if neighbors < 2:
            node.key = 0

        elif neighbors > 3:
            node.key = 0

        if neighbors == 3:
            node.key = 1

    gv.Game.transmit(gv.GameF)
    gv.frame = False

def keyUpdate():
    Mx, My = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (Mx, My) = pygame.mouse.get_pos()
            Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
            if gv.GameF.get(Nx, Ny).key == 1:
                gv.GameF.get(Nx, Ny).key = 0

            else:
                gv.GameF.get(Nx, Ny).key = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gv.isRunning == False:
                    gv.isRunning = True

                else:
                    gv.isRunning = False

            if event.key == pygame.K_f:
                gv.frame = True
                gv.isRunning = False

            if event.key == pygame.K_c:
                nodes = gv.GameF.find(1)
                for node in nodes:
                    node.key = 0

            if event.key == pygame.K_g:
                if gv.showGrid:
                    gv.showGrid = False

                else:
                    gv.showGrid = True

            if event.key == pygame.K_F1:
                if gv.showFPS:
                    gv.showFPS = False

                else:
                    gv.showFPS = True

            if event.key == pygame.K_ESCAPE:
                pygame.display.quit(), sys.exit()

        elif event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

def draw():
    for x in range(0, gv.width):
        for y in range(0, gv.height):
            if gv.GameF.get(x + 1, y + 1).key == 1:
                pygame.draw.rect(screen, color2, (x * gv.sizeFactor, y * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

    if gv.showGrid:
        for column in range(1, gv.width):
            pygame.draw.line(screen, "black", (column * gv.sizeFactor, 0), (column * gv.sizeFactor, gv.height * gv.sizeFactor))

        for row in range(1, gv.height):
            pygame.draw.line(screen, "black", (0, row * gv.sizeFactor), (gv.width * gv.sizeFactor, row * gv.sizeFactor))

    if gv.showFPS:
        fps = str(int(clock.get_fps()))
        if int(fps) < 20:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("red"))

        elif int(fps) >= 40:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("green"))

        else:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("yellow"))

        screen.blit(fpsDisplay, (5, 0))

mixer.music.load("ConwaysMusecore.mp3")

mixer.music.set_volume(0.03)

mixer.music.play(-1)

def main():
    while True:
        clock.tick(120)
        screen.fill(color)
        if gv.isRunning or gv.frame:
            update()

        draw()
        keyUpdate()
        pygame.display.flip()

if __name__ == '__main__':
    main()


