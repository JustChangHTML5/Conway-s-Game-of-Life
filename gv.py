import pygame
pygame.init()
Game = None
GameF = None
width = 105
height = 60
ssx = 0
ssy = 0
#screen shift x and screen shift y
#There is a smallest size
sizeFactor = 16
scroll = 1.05
isRunning = None
frame = False
showGrid = True
showFPS = True
generations = 0
showGenerations = True
showInstructions = True
pygame.display.set_caption("Conway's Game of Life", "GOL")
Icon = pygame.image.load("Game_of_life_Icon.gif")
pygame.display.set_icon(Icon)
font = pygame.font.SysFont("comicsansms", 17)
font2 = pygame.font.SysFont("Ariel", 34)