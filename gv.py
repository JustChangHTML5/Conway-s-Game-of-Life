import pygame
pygame.init()
Game = None
GameF = None
width = 105
height = 60
#There is a smallest size
sizeFactor = 16
isRunning = None
frame = False
showGrid = True
showFPS = True
pygame.display.set_caption("Conway's Game of Life", "GOL")
Icon = pygame.image.load("Game_of_life_Icon.gif")
pygame.display.set_icon(Icon)
font = pygame.font.SysFont("comicsansms", 18)