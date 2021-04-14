import pygame
import gv
import sys
import math
from lifeMatrix import *

mixer = pygame.mixer
mixer.init()
pygame.init()

size = (gv.width * gv.sizeFactor, gv.height * gv.sizeFactor)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
gv.resize = [size[0], size[1]]
clock = pygame.time.Clock()
#color = (150, 150, 150)
#color2 = (230, 230, 0)
#color = (98, 159, 134)
#color2 = (157, 96, 121)
color = (255, 255, 255)
color2 = (0, 0, 0)
color3 = (0, 128, 128)

gv.Game = Matrix()
gv.GameF = Matrix()
gv.Game.build(gv.width, gv.height)
gv.GameF.build(gv.width, gv.height)
gv.Game.NodesData = gv.GameF.NodesData
gv.isRunning = False

def blit_text(surface, text, pos, font, color=pygame.Color('Purple')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def check(node):
    neighbors = 0
    if gv.Game.get(node.Xm - 1, node.Ym + 1).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm, node.Ym + 1).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym + 1).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm - 1, node.Ym).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm - 1, node.Ym - 1).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm, node.Ym - 1).key > 0:
        neighbors += 1

    if gv.Game.get(node.Xm + 1, node.Ym - 1).key > 0:
        neighbors += 1

    return neighbors


def update():
    gv.Game.transmit(gv.GameF)
    for node in gv.GameF.Nodes:
        if node.key != 2:
            neighbors = check(gv.Game.get(node.Xm, node.Ym))
            if neighbors < 2:
                node.key = 0

            elif neighbors > 3:
                node.key = 0

            if neighbors == 3:
                node.key = 1

    gv.Game.transmit(gv.GameF)
    gv.generations += 1
    gv.frame = False

def keyUpdate():
    global screen, size, color, color2
    Mx, My = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                gv.sizeFactor *= gv.scroll
                Mx, My = pygame.mouse.get_pos()
                gv.ssx, gv.ssy = (Mx - (gv.width * gv.sizeFactor / 2)), (My - (gv.height * gv.sizeFactor / 2))
                #correct this

            if event.button == 5:
                gv.sizeFactor /= gv.scroll
                Mx, My = pygame.mouse.get_pos()
                gv.ssx, gv.ssy = (Mx - (gv.width * gv.sizeFactor / 2)), (My - (gv.height * gv.sizeFactor / 2))

            if event.button == 1:
                if gv.mobile == True:
                    if pygame.mouse.get_pos() >= (size[0] - 100, 0) and pygame.mouse.get_pos() <= (size[0], 50):
                        if gv.isRunning:
                            gv.isRunning = False

                        else:
                            gv.isRunning = True

                    else:
                        (Mx, My) = pygame.mouse.get_pos()
                        Mx, My = Mx - gv.ssx, My - gv.ssy
                        Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                        if gv.GameF.get(Nx, Ny).key == 1:
                            gv.GameF.get(Nx, Ny).key = 0

                        else:
                            gv.GameF.get(Nx, Ny).key = 1

                else:
                    (Mx, My) = pygame.mouse.get_pos()
                    Mx, My = Mx - gv.ssx, My - gv.ssy
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    if gv.GameF.get(Nx, Ny).key == 1:
                        gv.GameF.get(Nx, Ny).key = 0

                    else:
                        gv.GameF.get(Nx, Ny).key = 1

            if event.button == 3:
                if gv.mobile == True:
                    if pygame.mouse.get_pos() >= (size[0] - 100, 0) and pygame.mouse.get_pos() <= (size[0], 50):
                        if gv.isRunning:
                            gv.isRunning = False

                        else:
                            gv.isRunning = True

                    else:
                        (Mx, My) = pygame.mouse.get_pos()
                        Mx, My = Mx - gv.ssx, My - gv.ssy
                        Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                        if gv.GameF.get(Nx, Ny).key == 2:
                            gv.GameF.get(Nx, Ny).key = 0

                        else:
                            gv.GameF.get(Nx, Ny).key = 2

                else:
                    (Mx, My) = pygame.mouse.get_pos()
                    Mx, My = Mx - gv.ssx, My - gv.ssy
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    if gv.GameF.get(Nx, Ny).key == 2:
                        gv.GameF.get(Nx, Ny).key = 0

                    else:
                        gv.GameF.get(Nx, Ny).key = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gv.isRunning == False:
                    gv.isRunning = True

                else:
                    gv.isRunning = False

            if event.key == pygame.K_r:
                gv.ssx, gv.ssy, gv.sizeFactor = (screen.get_width() - (16 * gv.width)) / 2, (screen.get_height() - (16 * gv.height)) / 2, 16

            if event.key == pygame.K_f:
                gv.frame = True
                gv.isRunning = False

            if event.key == pygame.K_c:
                gv.generations = 0
                nodes = gv.GameF.find(1)
                for node in nodes:
                    node.key = 0

                nodes = gv.GameF.find(2)
                for node in nodes:
                    node.key = 0

            if event.key == pygame.K_g:
                if gv.showGrid:
                    gv.showGrid = False

                else:
                    gv.showGrid = True

            if event.key == pygame.K_e:
                if gv.showGenerations:
                    gv.showGenerations = False

                else:
                    gv.showGenerations = True

            if event.key == pygame.K_i:
                if color == (0, 0, 0):
                    color = (255, 255, 255)

                else:
                    color = (0, 0, 0)

                if color2 == (0, 0, 0):
                    color2 = (255, 255, 255)

                else:
                    color2 = (0, 0, 0)

            if event.key == pygame.K_h:
                if gv.showInstructions:
                    gv.showInstructions = False

                else:
                    gv.showInstructions = True

            if event.key == pygame.K_m:
                if gv.mobile:
                    gv.mobile = False

                else:
                    gv.mobile = True

            if event.key == pygame.K_s:
                gv.GameF.save("ConwaysGameOfLife")
                gv.GameF.save("ConwaysGameOfLifeBackup")

            if event.key == pygame.K_n:
                mixer.music.stop()

            if event.key == pygame.K_p:
                mixer.music.play(-1)

            if event.key == pygame.K_l:
                try:
                    gv.GameF = gv.GameF.load("ConwaysGameOfLife")

                except:
                    gv.GameF = gv.GameF.load("ConwaysGameOfLifeBackup")
                gv.Game.transmit(gv.GameF)
                gv.Game.NodesData = gv.GameF.NodesData
                gv.Game.sizeX, gv.Game.sizeY, gv.Game.size = gv.GameF.sizeX, gv.GameF.sizeY, gv.GameF.size
                gv.width = gv.GameF.sizeX
                gv.height = gv.GameF.sizeY
                gv.generations = 0

            if event.key == pygame.K_F1:
                if gv.showFPS:
                    gv.showFPS = False

                else:
                    gv.showFPS = True

            if event.key == pygame.K_F2:
                nodes = gv.GameF.find(2)
                for node in nodes:
                    node.key = 0

            if event.key == pygame.K_F3:
                nodes = gv.GameF.find(1)
                for node in nodes:
                    node.key = 0

            if event.key == pygame.K_ESCAPE:
                pygame.display.quit(), sys.exit()

        elif event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

    if gv.resize != list(screen.get_size()):
        gv.ssx, gv.ssy, gv.sizeFactor = (screen.get_width() - (16 * gv.width)) / 2, (screen.get_height() - (16 * gv.height)) / 2, 16
        gv.resize = list(screen.get_size())

    """(Mx, My) = pygame.mouse.get_pos()
    changex, changey = (gv.ssx / gv.sizeFactor - math.floor(gv.ssx / gv.sizeFactor)) * gv.sizeFactor - gv.sizeFactor, (gv.ssy / gv.sizeFactor - math.floor(gv.ssy / gv.sizeFactor)) * gv.sizeFactor
    Mx, My = math.floor(Mx / gv.sizeFactor) * gv.sizeFactor + changex, math.floor(My / gv.sizeFactor) * gv.sizeFactor + changey
    pointer = pygame.Surface((gv.sizeFactor + 1, gv.sizeFactor + 1), pygame.SRCALPHA)
    pointer.fill((0, 0, 255, 128))
    screen.blit(pointer, (Mx, My ))"""

def draw():
    """
    for x in range(0, gv.width):
        for y in range(0, gv.height):
            if gv.GameF.get(x + 1, y + 1).key == 1:
                pygame.draw.rect(screen, color2, (x * gv.sizeFactor, y * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))
    """
    for node in gv.GameF.Nodes:
        if gv.GameF.get(node.Xm, node.Ym).key == 1:
            pygame.draw.rect(screen, color2, ((node.Xm - 1) * gv.sizeFactor + gv.ssx, (node.Ym - 1) * gv.sizeFactor + gv.ssy, gv.sizeFactor + 1, gv.sizeFactor + 1))

        if gv.GameF.get(node.Xm, node.Ym).key == 2:
            pygame.draw.rect(screen, color3, ((node.Xm - 1) * gv.sizeFactor + gv.ssx, (node.Ym - 1) * gv.sizeFactor + gv.ssy, gv.sizeFactor + 1, gv.sizeFactor + 1))

    if gv.showGrid:
        for column in range(1, gv.width):
            pygame.draw.line(screen, "gray", (column * gv.sizeFactor + gv.ssx, 0 + gv.ssy), (column * gv.sizeFactor + gv.ssx, gv.height * gv.sizeFactor + gv.ssy))

        for row in range(1, gv.height):
            pygame.draw.line(screen, "gray", (0 + gv.ssx, row * gv.sizeFactor + gv.ssy), (gv.width * gv.sizeFactor + gv.ssx, row * gv.sizeFactor + gv.ssy))

    pygame.draw.line(screen, "gray", (0 + gv.ssx, 0 + gv.ssy), (0 + gv.ssx, gv.height * gv.sizeFactor + gv.ssy))
    pygame.draw.line(screen, "gray", (gv.width * gv.sizeFactor + gv.ssx, 0 + gv.ssy), (gv.width * gv.sizeFactor + gv.ssx, gv.height * gv.sizeFactor + gv.ssy))
    pygame.draw.line(screen, "gray", (0 + gv.ssx, 0 + gv.ssy), (gv.width * gv.sizeFactor + gv.ssx, 0 + gv.ssy))
    pygame.draw.line(screen, "gray", (0 + gv.ssx, gv.height * gv.sizeFactor + gv.ssy), (gv.width * gv.sizeFactor + gv.ssx, gv.height * gv.sizeFactor + gv.ssy))

    if gv.showFPS:
        fps = str(int(clock.get_fps()))
        if int(fps) < 20:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("red"))

        elif int(fps) >= 40:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("green"))

        else:
            fpsDisplay = gv.font.render(fps + " FPS", 1, pygame.Color("yellow"))

        screen.blit(fpsDisplay, (5, 0))

    if gv.showGenerations:
        generationDisplay = gv.font2.render(str(gv.generations) + " Generations", 1, pygame.Color("gray"))
        screen.blit(generationDisplay, (size[0] / 2 - 50, 0))

    if gv.showInstructions:
        Instructions = " Escape to close,\n Left click to place a cell or destroy a cell,\n right click to place god cell or destroy a god cell,\n Spacebar to start the game,\n f to go frame by frame,\n s to save,\n l to load,\n hit c to clear all cells,\n hit f2 and f3 to clear god cells and cells respectivly,\n hit e, g, or f1 to toggle the generation display, grid or frames per second, hit n to stop the music, hit p to start the music again, hit i to invert the color scheme,\n scroll to zoom,\n hit r to reset zoom scale,\n hit m to stop being in mobile mode,\n hit the blue button to start or stop,\n and finally, hit h to toggle the instructions."
        blit_text(screen, Instructions, (gv.width - 100, 20), gv.font)

    if gv.mobile == True:
        pygame.draw.rect(screen, (0, 50, 230), (size[0] - 100, 0, 100, 50))

mixer.music.load("ConwaysMusecore.mp3")

mixer.music.set_volume(0.1)

mixer.music.play(-1)

def main():
    while True:
        clock.tick(70)
        screen.fill(color)
        if gv.isRunning or gv.frame:
            update()

        draw()
        keyUpdate()
        pygame.display.flip()

if __name__ == '__main__':
    main()


