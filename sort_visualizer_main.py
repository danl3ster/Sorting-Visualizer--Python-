import pygame
import pygame_menu
import random
from pygame.locals import *
import time

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
    colourdict = {}
    VIBGYOR = [(148, 0, 211),(75, 0, 130),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 127, 0),(255, 0 , 0)]
    count = 0
    sectioncount = 0

    #Assign Multicolour rectangles
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
    
    #Assign red gradient
    if col_option == 2:

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
    
    #Assign green gradient
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

    #Assign blue gradient
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
    global sorted
    sorted = False

    ##Algorithmns

    #Insertion Sort
    if algonum == 1:
        sorted = False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            if sorted == False:
                #Insertion sort algo
                i = 1
                while i < len(workinglist):

                    #Draws current state of array
                    screen.fill(BLACK)
                    for k in range(0,len(workinglist)-1):
                        if k == i or k == j:
                            pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                        else:
                            pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                    pygame.display.flip()

                    j = i
                    while j > 0 and workinglist[j-1] > workinglist[j]:
                        workinglist[j-1], workinglist[j] = workinglist[j],workinglist[j-1]
                        j = j-1
                    i = i + 1
                    clock.tick(speed)

                screen.fill(BLACK)
                #Draws final state of array
                for k in range(0,len(workinglist)-1):
                            pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                pygame.display.flip()

            sorted = True
            time.sleep(2)
            game_active = False

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
                if arr[left] <= arr[j]:
                    left += 1
                else:
                    # storing the smaller element in temp variable
                    temp = arr[j]
                    i = j

                    # this while loop will shift all the elements one step to right to make space 
                    while i != left:
                        arr[i] = arr[i-1]
                        i -= 1
                    arr[left] = temp

                    #Draws current state of array
                    screen.fill(BLACK)
                    for k in range(0,len(arr)-1):
                        if k == j:
                            pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                        else:
                            pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                    pygame.display.flip()
                    clock.tick(speed)

                    left += 1
                    m += 1
                    j += 1
                    k += 1
    if algonum == 2:
        sorted = False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            if sorted == False:
                mergesort(workinglist,0,len(workinglist)-1)
            sorted = True
            time.sleep(2)
            game_active = False

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
            screen.fill(BLACK)
            for k in range(0,len(array)-1):
                if k == i:
                    pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[array[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)

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

            #Draws current state of array
            screen.fill(BLACK)
            for k in range(0,len(array)-1):
                if k == i:
                    pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[array[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)

            pygame.display.flip()
            clock.tick(speed)
    if algonum == 3:
        sorted = False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            if sorted == False:
                countsort(workinglist)   
            sorted = True
            time.sleep(2)
            game_active = False

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

                # find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = partition(array, low, high)

                #draws current state of array
                screen.fill(BLACK)
                for k in range(0,len(array)-1):
                    if k == pi or k == high:
                        pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
                    else:
                        pygame.draw.line(screen,colourdict[array[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + array[k]),rectwidth)
                pygame.display.flip()
                clock.tick(speed)

                # recursive call on the left of pivot
                quickSort(array, low, pi - 1)

                # recursive call on the right of pivot
                quickSort(array, pi + 1, high)    
    if algonum == 4:
        sorted = False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            if sorted == False:
                size = len(workinglist)
                quickSort(workinglist, 0, size - 1)
                for k in range(0,len(workinglist)-1):
                        pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                pygame.display.flip()
                clock.tick(speed)
            sorted = True
            time.sleep(2)
            game_active = False

    #Selection Sort
    if algonum == 5:
        sorted = False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

        # Traverse through all array elements
            if sorted == False:
                for i in range(len(workinglist)):
                    
                    # Find the minimum element in remaining
                    # unsorted array
                    min_idx = i
                    for j in range(i+1, len(workinglist)):
                        if workinglist[min_idx] > workinglist[j]:
                            min_idx = j
                            
                    # Swap the found minimum element with
                    # the first element       
                    workinglist[i], workinglist[min_idx] = workinglist[min_idx], workinglist[i]

                    #Draws current state of array
                    screen.fill(BLACK)
                    for k in range(0,len(workinglist)-1):
                        if k == i or k == min_idx:
                            pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                        else:
                            pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
                    pygame.display.flip()
                    clock.tick(speed)
            sorted = True
            time.sleep(2)
            game_active = False
    
    #Heap sort
    def heapify(arr, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < N and arr[i] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < N and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
    
            # Heapify the root.
            heapify(arr, N, largest)  
    def heapSort(arr):
        N = len(arr)
    
        # Build a maxheap.
        for i in range(N//2 - 1, -1, -1):
            heapify(arr, N, i)


        # One by one extract elements
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)
            
            #Draws current state of array
            screen.fill(BLACK)
            for k in range(0,len(arr)-1):
                if k == i:
                    pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)
    if algonum == 6:
        sorted == False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop


            if sorted == False:
                heapSort(workinglist)  

            #Draws final state of array
            for k in range(0,len(workinglist)-1):
                pygame.draw.line(screen,colourdict[workinglist[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + workinglist[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)

            sorted = True
            time.sleep(2)
            game_active = False

    #Bubble Sort
    def bubbleSort(arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            #Draws current state of array
            screen.fill(BLACK)
            for k in range(0,len(arr)-1):
                if k == i:
                    pygame.draw.line(screen,(255, 255, 255),(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    if algonum == 7:
        sorted == False
        while game_active:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    game_active = False # Flag that we are done so we exit this loop

            if sorted == False:
                bubbleSort(workinglist)  
            sorted = True
            time.sleep(2)
            game_active = False

    #Bucket Sort
    def bucketSort(arr, noOfBuckets):
        max_ele = max(arr)
        min_ele = min(arr)
    
        # range(for buckets)
        rnge = (max_ele - min_ele) / noOfBuckets
    
        temp = []
    
        # create empty buckets
        for i in range(noOfBuckets):
            temp.append([])
    
        # scatter the array elements
        # into the correct bucket
        for i in range(len(arr)):
            diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

            #Draws current state of array
            screen.fill(BLACK)
            for k in range(0,len(arr)-1):
                if k == i:
                    pygame.draw.line(screen,(255,255,255),(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                else:
                    pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
            pygame.display.flip()
            clock.tick(speed)

            # append the boundary elements to the lower array
            if(diff == 0 and arr[i] != min_ele):
                temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
    
            else:
                temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
    
        # Sort each bucket individually
        for i in range(len(temp)):
            if len(temp[i]) != 0:
                temp[i].sort()

    
        # Gather sorted elements 
        # to the original array
        kk = 0
        for lst in temp:
            if lst:
                for i in lst:
                    screen.fill(BLACK)
                    for k in range(0,len(arr)-1):
                        pygame.draw.line(screen,colourdict[arr[k]],(Xcoordlist[k],10),(Xcoordlist[k],10 + arr[k]),rectwidth)
                    pygame.display.flip()
                    clock.tick(speed)
                    arr[kk] = i
                    kk = kk+1
    if algonum == 8:
            sorted == False
            while game_active:
                # --- Main event loop
                for event in pygame.event.get(): # User did something
                    if event.type == pygame.QUIT: # If user clicked close
                        game_active = False # Flag that we are done so we exit this loop


                if sorted == False:
                    bucketSort(workinglist,20)  
                sorted = True
                time.sleep(2)
                game_active = False

##Menu code

#Menu Theme
theme = pygame_menu.Theme(
                            background_color=pygame_menu.themes.TRANSPARENT_COLOR,
                            title=False,
                            widget_font=pygame_menu.font.FONT_FIRACODE,
                            widget_font_size = 20,
                            widget_font_color=(255, 255, 255),
                            widget_margin=(0, 15),
                            widget_selection_effect=pygame_menu.widgets.NoneSelection()
                            )

#Initialise menu
menu = pygame_menu.Menu(title='Sort Visualizer',height= 500, width= 500,
                    theme = theme )

#adds algo selector 
algonumselect = menu.add.selector('Algorithmn :', 
                    [('Insertion Sort', 1), ('Merge Sort', 2), ('Count Sort', 3),
                    ('Quick Sort', 4), ('Selection Sort', 5),('Heap sort', 6),
                    ('Bubble Sort', 7), ('Bucket Sort', 8),
                    ],
                    )

#adds speed selector 
speedselect = menu.add.selector('Speed :', [('Fast', 1), ('Medium', 2), ('Slow', 3)])

#adds colour option selector
col_optionselect = menu.add.selector('Colour Scheme :', [('Multi-colour ', 1), ('Red', 2), ('Green', 3), ('Blue', 4)])

#adds num to sort range slider
numtosortselect = menu.add.range_slider('Number of value to sort:', 300, list(range(50,600,1)),
                    rangeslider_id='numtosort_slider',range_text_value_tick_enabled = False
                    )

#adds action buttons
menu.add.button('Run', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


if __name__ == '__main__':
    menu.mainloop(screen)

pygame.quit()