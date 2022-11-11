import pygame
import pygame_menu
import random
from pygame.locals import *
from copy import deepcopy

pygame.init() 

#FPS
clock = pygame.time.Clock()

#colours
BLACK = (0, 0, 0)

#define display
size = (1500,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sort Visualizer")

#Variables for Sort
numtosort = 50
rangen_range = [1,601]
algonum = 1
speed = 80
col_option = 1
global count1
count1 = 0

def start_the_game():
    numtosort = numtosortselect.get_value()
    col_option = col_optionselect.get_value()[0][1]
    algonum = algonumselect.get_value()[0][1]

    if speedselect.get_value()[0][1] == 1:
        speed = 500
    if speedselect.get_value()[0][1] == 2:
        speed = 80
    if speedselect.get_value()[0][1] == 3:
        speed = 30


    #Generate list of values to sort
    unsortlist = random.sample(range(rangen_range[0],rangen_range[1]), numtosort)
    workinglist = unsortlist.copy()
    presortlist = unsortlist.copy()

    #Rectangle properties
    rectwidth = 1400//numtosort
    areawidth = numtosort * rectwidth
    Xcoordlist = range(50,areawidth+50,rectwidth)

    # Pre sort insertion algo
    i = 1
    while i < len(presortlist):
        j = i
        while j > 0 and presortlist[j-1] > presortlist[j]:
            presortlist[j-1], presortlist[j] = presortlist[j],presortlist[j-1]
            j = j-1
        i = i + 1

    #Rect colour options
    #Assign Multicolour rectangles
    colourdict = {}
    VIBGYOR = [(148, 0, 211),(75, 0, 130),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 127, 0),(255, 0 , 0)]
    count = 0
    sectioncount = 0
    if col_option == 1:
        for i in range(len(presortlist)):

            if count == 6:
                reverse = True
            if count == 0:
                reverse = False

            colourdict[presortlist[i]] = VIBGYOR[count]
            if sectioncount == 20:
                if reverse == True:
                    count = count - 1
                else:
                    count = count + 1
                sectioncount = 0
            else:
                sectioncount = sectioncount + 1

    if col_option == 2:
        #Assign red gradient
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
                colourdict[presortlist[i]] = (k,0,0)
            else:
                reversecol = True
                colourdict[presortlist[i]] = (k,0,0)

    if col_option == 3:
        #Assign green gradient
        numperblock = 254//numtosort + 1
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
                colourdict[presortlist[i]] = (0,k,0)
            else:
                reversecol = True
                colourdict[presortlist[i]] = (0,k,0)

    if col_option == 4:
        #Assign blue gradient
        numperblock = 254//numtosort + 1
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

    #Insertion Sort
    if algonum == 1:
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
                    screen.fill(BLACK)
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
                    clock.tick(speed)
                sorted = True
                screen.fill(BLACK)
                for k in range(0,len(workinglist)-1):
                            pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                pygame.display.flip()
    
    #Merge sort
    def mergesort(arr, left, right):
        if left < right:
            m = (left+right)//2
            mergesort(arr, left, m)
            mergesort(arr, m+1, right)
    
            j = m+1
            # if m+1 == len(arr):
            #     return
            if arr[m] <= arr[m+1]:
                return
    
            while left <= m and j <= right:
                screen.fill(BLACK)
                for k in range(0,len(arr)-1):
                    pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                pygame.display.flip()
                clock.tick(speed)
                if arr[left] <= arr[j]:
                    left += 1
                else:
                    screen.fill(BLACK)
                    for k in range(0,len(arr)-1):
                        pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                    pygame.display.flip()
                    clock.tick(speed)
                    
                    # array of colours where only the focused bars
                    # are displayed red since left >arr[j]
                    temp = arr[j]
                    
                    # storing the smaller element in temp variable
                    i = j
                    while i != left:
                        arr[i] = arr[i-1]
                        screen.fill(BLACK)
                        for k in range(0,len(arr)-1):
                            pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                        pygame.display.flip()

                        i -= 1
                    
                    # this while loop will shift all the elements one step
                    # to right to make the place empty for the temp variable
                    # upon reaching the desired location i.e. left, the
                    # temp value will be inserted into that location.
                    # this process is much like insertion sort
                    arr[left] = temp
                    screen.fill(BLACK)
                    for k in range(0,len(arr)-1):
                        pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                    pygame.display.flip()
                    left += 1
                    m += 1
                    j += 1
                    k += 1
    if algonum == 2:
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            #Loop until sort is finished
                #Draw set of rectangles based off lists
                #Do one sort algo iteration
                #Update lists

            mergesort(workinglist,0,len(workinglist)-1)

    #Count Sort
    def countsort(array):
        size = len(array)
        maxsize= max(array)
        output = [0] * size

        # Initialize count array
        count = [0] * (maxsize+1)

        # Store the count of each elements in count array
        for i in range(0, size):
            count[array[i]] += 1

        # Store the cummulative count
        for i in range(1, maxsize+1):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            array[i] = output[i]
            screen.fill(BLACK)
            for k in range(0,len(array)-1):
                pygame.draw.line(screen,colourdict[array[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)
    if algonum == 3:
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            #Loop until sort is finished
                #Draw set of rectangles based off lists
                #Do one sort algo iteration
                #Update lists

            countsort(workinglist)   

    #Quick sort
    def partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # return the position from where partition is done
        return i + 1
    def quickSort(array, low, high):
            if low < high:
                screen.fill(BLACK)
                for k in range(0,len(array)-1):
                    pygame.draw.line(screen,colourdict[array[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
                pygame.display.flip()
                clock.tick(speed)

                # find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = partition(array, low, high)

                # recursive call on the left of pivot
                quickSort(array, low, pi - 1)

                # recursive call on the right of pivot
                quickSort(array, pi + 1, high)
    if algonum == 4:
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            #Loop until sort is finished
                #Draw set of rectangles based off lists
                #Do one sort algo iteration
                #Update lists
            size = len(workinglist)
            quickSort(workinglist, 0, size - 1)

theme = pygame_menu.Theme(
                            background_color=pygame_menu.themes.TRANSPARENT_COLOR,
                            title=False,
                            widget_font=pygame_menu.font.FONT_FIRACODE,
                            widget_font_size = 20,
                            widget_font_color=(255, 255, 255),
                            widget_margin=(0, 15),
                            widget_selection_effect=pygame_menu.widgets.NoneSelection()
                            )

menu = pygame_menu.Menu(title='Sort Visualizer',height= 500, width= 500,
                    theme = theme )

algonumselect = menu.add.selector('Algorithmn :', 
                    [('Insertion Sort', 1), ('Merge Sort', 2), ('Count Sort', 3),
                    ('Quick Sort', 4), ('Radix Sort', 5), ('Selection Sort', 6),
                    ('Heap sort', 7), ('Bubble Sort', 8), ('Bucket Sort', 9),
                    ],
                    )

speedselect = menu.add.selector('Speed :', [('Fast', 1), ('Medium', 2), ('Slow', 3)])

col_optionselect = menu.add.selector('Colour Scheme :', [('Multi-colour ', 1), ('Red', 2), ('Green', 3), ('Blue', 4)])

numtosortselect = menu.add.range_slider('Number of value to sort:', 300, list(range(50,600,1)),
                    rangeslider_id='numtosort_slider',range_text_value_tick_enabled = False
                    )

menu.add.button('Run', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


if __name__ == '__main__':
    menu.mainloop(screen)






pygame.quit()