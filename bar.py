import pygame

BLACK = (0,0,0)

class bar(pygame.sprite.Sprite):
    def __init__(self, color, width, height,Xloc,Yloc):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the bar, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [Xloc, Yloc, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    
