import time
import pygame,sys
from pygame.locals import*
from pygame import mixer
import os


StartUp=pygame.image.load('StartUp.png')
Homebttn=pygame.image.load('HOME.png')

x=778
y=157
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)
w = 365
h = 767
screen = pygame.display.set_mode([w, h])
x = y = 0
running = True

pygame.init()

screen.blit(StartUp,(0,0))
screen.blit(Homebttn,(166,686))
pygame.display.flip()
time.sleep(3)

WHITE=(255,255,255)
blue=(0,0,255)

X= pygame.mouse.get_pos()

pygame.draw.rect(screen,blue,(48,164,58,58))
i=0

while running:

        
    import LatestFile.py
