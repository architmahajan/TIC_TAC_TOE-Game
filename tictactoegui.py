import random, pygame, sys
import os
import subprocess
from pygame.locals import *
import soundmixer
FPS = 30 
WINDOWWIDTH = 360
WINDOWHEIGHT = 360
BOXSIZE = 80 
GAPSIZE = 5
BOARDWIDTH = 3
BOARDHEIGHT = 3
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

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

grid=[['2','2','2'],\
     ['2','2','2'],\
     ['2','2','2']]
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
        
        boxx=int(boxx)
        boxy=int(boxy)
        if(boxx!=3 and boxy!=3 and mouseClicked):
            print(boxx,boxy)
            break
                
        pygame.display.update()
        FPSCLOCK.tick(fps)
    if(boxx==1 and boxy==2):
        executecrossesfirst()
    elif(boxx==1 and boxy==1):
        executezeroesfirst();

def getBoxAtPixeloption(x, y):
    if textRectObj1.collidepoint(x, y):
        return (1,1)
    elif textRectObj2.collidepoint(x,y):
        return (1,2)
    else:
        return (3,3)
def executecrossesfirst():
    
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    mousex=0
    mousey=0
    icon=[]
    for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                grid[boxx][boxy]=int(3)
                icon.append((boxx,boxy))
    random.shuffle(icon)
    print(icon[0])
    print(icon[0][0],icon[0][1])
    grid[icon[0][0]][icon[0][1]]=int(1);
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        
        boxx=int(boxx)
        boxy=int(boxy)
        if(boxx!=3 and boxy!=3 and mouseClicked):
            print(boxx,boxy)
            if(boxy==0):
                point=boxx+boxy+1
            elif(boxy==1):
                point=boxx+boxy+3
            elif(boxy==2):
                point=boxx+boxy+5
            print(point)
            
            if(grid[boxy][boxx]==3):
                grid[boxy][boxx]=int(0);
                print(grid[boxy][boxx])
                drawboard(grid)
                ss="";
                for boxx in range(BOARDWIDTH):
                    for boxy in range(BOARDHEIGHT):
                        ss+=str(grid[boxx][boxy]);
                print(ss);
                process = subprocess.Popen(['./a.out', ss], stdout=subprocess.PIPE)
                stdout = process.communicate()[0]
                print(stdout)
                print(len(stdout))
                mv=stdout;
                mv=int(mv);
                if mv>=99:
                    if(mv>=120):
                        mv-=120;
                        if(mv%3==0):
                            mvvy=2;
                            mvvx=mv/3-1;
                            grid[mvvx][mvvy]=int(1);
                        else:
                            mvvy=(mv%3)-1;
                            mvvx=mv/3;
                            grid[mvvx][mvvy]=int(1);
                        drawboard(grid)
                        s="Match Draw"
                    elif(mv>=102):
                        mv-=102;
                        if(mv%3==0):
                            mvvy=2;
                            mvvx=mv/3-1;
                            grid[mvvx][mvvy]=int(1);
                        else:
                            mvvy=(mv%3)-1;
                            mvvx=mv/3;
                            grid[mvvx][mvvy]=int(1);
                        drawboard(grid)
                        s="Computer Wins!!"
                    elif(mv==100):
                        s="Human Wins!!"
                    elif(mv==101):
                        s="Match Draw!!"
                    gameAnimation(s)
                    # for boxx in range(BOARDWIDTH):
                    #     for boxy in range(BOARDHEIGHT):
                    #         grid[boxx][boxy]=int(3)
                    # mouseClicked = False
                    # DISPLAYSURF.fill(BGCOLOR)
                    # random.shuffle(icon)
                    # grid[icon[0][0]][icon[0][1]]=int(1);
                    main()
                elif(mv%3==0):
                    mvvy=2;
                    mvvx=mv/3-1;
                    grid[mvvx][mvvy]=int(1);
                else:
                    mvvy=(mv%3)-1;
                    mvvx=mv/3;
                    grid[mvvx][mvvy]=int(1);
            # output = subprocess.check_output(['./a.out', ss]).decode(sys.stdout.encoding)
            # print output
        drawboard(grid)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def executezeroesfirst():
    
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    mousex=0
    mousey=0
    for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                grid[boxx][boxy]=int(3)
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        
        boxx=int(boxx)
        boxy=int(boxy)
        if(boxx!=3 and boxy!=3 and mouseClicked):
            print(boxx,boxy)
            if(boxy==0):
                point=boxx+boxy+1
            elif(boxy==1):
                point=boxx+boxy+3
            elif(boxy==2):
                point=boxx+boxy+5
            print(point)
            
            if(grid[boxy][boxx]==3):
                grid[boxy][boxx]=int(0);
                print(grid[boxy][boxx])
                drawboard(grid)
                ss="";
                for boxx in range(BOARDWIDTH):
                    for boxy in range(BOARDHEIGHT):
                        ss+=str(grid[boxx][boxy]);
                print(ss);
                process = subprocess.Popen(['./a.out', ss], stdout=subprocess.PIPE)
                stdout = process.communicate()[0]
                print(stdout)
                print(len(stdout))
                mv=stdout;
                mv=int(mv);
                if mv>=99:
                    if(mv>=120):
                        mv-=120;
                        if(mv%3==0):
                            mvvy=2;
                            mvvx=mv/3-1;
                            grid[mvvx][mvvy]=int(1);
                        else:
                            mvvy=(mv%3)-1;
                            mvvx=mv/3;
                            grid[mvvx][mvvy]=int(1);
                        drawboard(grid)
                        s="Match Draw"
                    elif(mv>=102):
                        mv-=102;
                        if(mv%3==0):
                            mvvy=2;
                            mvvx=mv/3-1;
                            grid[mvvx][mvvy]=int(1);
                        else:
                            mvvy=(mv%3)-1;
                            mvvx=mv/3;
                            grid[mvvx][mvvy]=int(1);
                        drawboard(grid)
                        s="Computer Wins!!"
                    elif(mv==100):
                        s="Human Wins!!"
                    elif(mv==101):
                        s="Match Draw!!"
                    gameAnimation(s)
                    main()
                elif(mv%3==0):
                    mvvy=2;
                    mvvx=mv/3-1;
                    grid[mvvx][mvvy]=int(1);
                else:
                    mvvy=(mv%3)-1;
                    mvvx=mv/3;
                    grid[mvvx][mvvy]=int(1);
            # output = subprocess.check_output(['./a.out', ss]).decode(sys.stdout.encoding)
            # print output
        drawboard(grid)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)
def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (3, 3)
def drawboard(grid):
    for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy) 
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                left=left+40;
                top=top+40; 
                if(grid[boxy][boxx]==0):
                    pygame.draw.circle(DISPLAYSURF,BLUE,(left,top),30,10)
                elif(grid[boxy][boxx]==1):
                    pygame.draw.line(DISPLAYSURF,RED,(left-22,top-22),(left+22,top+22),5)
                    pygame.draw.line(DISPLAYSURF,RED,(left+22,top-22),(left-22,top+22),5)
def gameAnimation(s):
    # flash the background color when the player has won
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR
    fontObj = pygame.font.Font('freesansbold.ttf', 32)

    textSurfaceObj = fontObj.render(s, True, GREEN,BLUE)

    textRectObj = textSurfaceObj.get_rect()

    textRectObj.center = (200, 350)
    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        drawboard(grid)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        pygame.time.wait(300)
if __name__ == '__main__':
    main()

