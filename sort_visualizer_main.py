from re import I
from typing import Collection
import pygame
import pygamegui
import random
from bar import bar
from pygame.locals import *
from copy import deepcopy
pygame.init()

#FPS
clock = pygame.time.Clock()

#colours
WHITE = (0, 0, 0)

#define display
size = (1500,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sort Visualizer")

#Variables for Sort
numtosort = 600
rangen_range = [1,601]

#Generate list of values to sort
unsortlist = random.sample(range(rangen_range[0],rangen_range[1]), numtosort)
workinglist = unsortlist.copy()
presortlist = unsortlist.copy()

#Rectangle properties
rectwidth = 1400//numtosort
areawidth = numtosort * rectwidth
rectcolours = []
temp = ["","",""]

for i in range(numtosort):
    temp = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    rectcolours.append(temp) 

Xcoordlist = range(50,areawidth+50,rectwidth)
print(rectcolours[1])

# Insertion sort algo
i = 1
while i < len(presortlist):
    j = i
    while j > 0 and presortlist[j-1] > presortlist[j]:
       presortlist[j-1], presortlist[j] = presortlist[j],presortlist[j-1]
       j = j-1
    i = i + 1

#Assign gradient of colours
numperblock = 254//numtosort + 1
colourdict = {}
k=244
reversecol = False
for i in range(len(presortlist)):
    if reversecol:
        k = k-10
    else:
        k=k + 10

    if k < 20:
        reversecol = False

    if k < 244:
        colourdict[presortlist[i]] = (0,0,k)
    else:
        reversecol = True
        colourdict[presortlist[i]] = (0,0,k)

game_active = True
sorted = False


while game_active:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              game_active = False # Flag that we are done so we exit this loop



    #Loop until sort is finished
        #Draw set of rectangles based off lists
        #Do one sort algo iteration
        #Update lists

    if not sorted:
        #Insertion sort algo
        i = 1
        while i < len(workinglist):
            screen.fill(WHITE)
            for k in range(0,len(workinglist)-1):
                if k == i or k == j:
                    pygame.draw.line(screen,(255,0,0),(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
            pygame.display.flip()

            
            j = i
            while j > 0 and workinglist[j-1] > workinglist[j]:
                workinglist[j-1], workinglist[j] = workinglist[j],workinglist[j-1]
                j = j-1
            i = i + 1
            clock.tick(100)
        sorted = True
        screen.fill(WHITE)
        for k in range(0,len(workinglist)-1):
                    pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
        pygame.display.flip()

pygame.quit()