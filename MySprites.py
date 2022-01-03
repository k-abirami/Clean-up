'''This file consists of sprite classes necessary for Clean Up'''

# I - Import and Initialize
import pygame
import random

class Player (pygame.sprite.Sprite):

    '''This class creates the player (sea diver)'''
    
    def __init__ (self): #Initialize
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 300

    def update(self): 

        #Moves the player according to the key pressed
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= 5
        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += 5
        if pressed_key[pygame.K_UP]:
            self.rect.centery -= 5
        if pressed_key[pygame.K_DOWN]:
            self.rect.centery += 5

        #Checks boundaries
        if self.rect.right > 800:
            self.rect.centerx -= 5
        if self.rect.left < 0:
            self.rect.centerx += 5
        if self.rect.top < 0:
            self.rect.centery += 5
        if self.rect.bottom > 600:
            self.rect.centery -= 5
            
class Coke (pygame.sprite.Sprite):

    '''This class creates the first type of Garbage - coke can'''
    
    def __init__ (self): #Initialize

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("coke_can.png")
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(25,750) #Moves in random speed from a random starting place
        self.rect.centery = random.randrange(23,555)
        self.__direction = random.randrange(1, 8)

    def update (self):
        #Moves left to right
        self.rect.right += self.__direction
        if (self.rect.left < 0) or (self.rect.right > 800):
            self.__direction = -self.__direction

class Wrapper (pygame.sprite.Sprite):

    '''This class creates the second type of Garbage - candy wrapper'''
    
    def __init__ (self): #Initialize
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("candy_wrapper.png")
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(25,750) #Moves in random speed from a random starting place
        self.rect.centery = random.randrange(23,555)
        self.__direction = random.randrange(1, 8)

    def update (self):
        #Moves top to down
        self.rect.top += self.__direction
        if (self.rect.top < 0) or (self.rect.bottom > 600):
            self.__direction = -self.__direction

class Fish (pygame.sprite.Sprite):

    '''This class creates the fish'''
    
    def __init__ (self, x_cor, y_cor): #Initialize
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("fish.png")
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x_cor
        self.rect.centery = y_cor
        self.__direction = random.randrange(1, 8)

    def update (self):
        #Moves diagonally
        self.rect.top += self.__direction
        self.rect.right += self.__direction
        if (self.rect.top < 0) or (self.rect.bottom > 600):
            self.__direction = -self.__direction
        if (self.rect.left < 0) or (self.rect.right > 800):
            self.__direction = -self.__direction

class Label (pygame.sprite.Sprite):

    '''This class creates label to update the status'''
    
    def __init__ (self, message, x_y_coordinate):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont("Calibri", 20)
        self.__text = message
        self.__center = x_y_coordinate

    def set_text(self, message):
        self.__text = message

    def update(self):
        self.image = self.__font.render(self.__text, 7, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center
    
