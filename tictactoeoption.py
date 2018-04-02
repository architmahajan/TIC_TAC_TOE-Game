import random, pygame, sys
import os
import subprocess
from pygame.locals import *
import soundmixer
fps=30
ww=int(500)
wh=int(500)
boxw=120
boxh=60
gs=50
bw=2
bh=1
xm = int((ww - (bw * (boxw + gs))) / 2)
ym = int((wh - (bh * (boxh + gs))) / 2)

GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

fontObj11 = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj11 = fontObj11.render("You want to play first ?", True, GREEN,BLUE)
textRectObj11 = textSurfaceObj11.get_rect()
textRectObj11.center = (250, 100)
fontObj1 = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj1 = fontObj1.render("YES", True, RED,WHITE)
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (150, 150)
fontObj2 = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj2 = fontObj2.render("NO", True, RED,WHITE)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (350, 150)
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((ww, wh))
    pygame.display.set_caption('TIC TAC TOE')
    mousex=0
    mousey=0
    while True:
    	mouseClicked=False
    	DISPLAYSURF.fill(BGCOLOR)
    	DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)
    	DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
    	DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
    	
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = getBoxAtPixeloption(mousex, mousey)
        print(boxx,boxy)
        boxx=int(boxx)
        boxy=int(boxy)
        if(boxx!=3 and boxy!=3 and mouseClicked):
        	break
        		
        pygame.display.update()
    	FPSCLOCK.tick(fps)

def getBoxAtPixeloption(x, y):
    if textRectObj1.collidepoint(x, y):
        return (1,1)
    elif textRectObj2.collidepoint(x,y):
        return (1,2)
    else:
    	return (3,3)
if __name__ == '__main__':
    main()


