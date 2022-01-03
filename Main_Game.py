'''
Name: Abirami Karthikeyan
Date: June 10, 2019
Description: This program is an environmental awareness game called Clean Up!
'''

# I - Import 
import pygame
import MySprites
import random
import Screens
    
def main():

    '''Mainline logic of the program'''

    Screens.open_screen() #Opens the starting screen

    #Initailize
    pygame.init()
    pygame.mixer.init()
    
    # D - Display configuration
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Clean Up!")
    
    # E - Entities 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((178,223,238))
    screen.blit(background, (0,0))

    #Sound for right move (picking garbage)
    ding = pygame.mixer.Sound("Ding.wav")
    ding.set_volume(0.5)
    
    #Sound for wrong move (touching fish)
    splash = pygame.mixer.Sound("Splash.wav")
    splash.set_volume(0.5)

    #Initizes variables and stores sprites attributes in them
    player = MySprites.Player()
    
    can_1 = MySprites.Coke()
    can_2 = MySprites.Coke()
    can_3 = MySprites.Coke()

    wrapper_1 = MySprites.Wrapper()
    wrapper_2 = MySprites.Wrapper()
    wrapper_3 = MySprites.Wrapper()

    fish_1 = MySprites.Fish(100, 100)
    fish_2 = MySprites.Fish(250, 100)
    fish_3 = MySprites.Fish(400, 100)
    fish_4 = MySprites.Fish(550, 100)
    fish_5 = MySprites.Fish(45, 100)

    #2 Labels: one for the pieces of garbage collected and another for number of fishes harmed
    Garbage_collected = MySprites.Label("", (150, 540))
    Fish_harmed = MySprites.Label("", (150, 560))

    #Grouping the sprites for ease in collisions and update
    GarbageGroup = pygame.sprite.Group(can_1, can_2, can_3, wrapper_1, wrapper_2, wrapper_3)
    FishGroup = pygame.sprite.Group(fish_1,fish_2,fish_3,fish_4,fish_5)
    otherGroup = pygame.sprite.Group(player, Garbage_collected, Fish_harmed)

    #Variables to count the pieces of garbage collected and number of fishes harmed
    Number_garbage = 0
    Number_fish = 0
    
    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    
    # L - Loop
    while keepGoing:
        
        # T - Timer to set frame rate
        clock.tick(30)
        
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keepGoing = False
            
        #Collisions

        #Collision between player and Garbage
        if pygame.sprite.spritecollide(player, GarbageGroup, True):
            Number_garbage += 1
            ding.play() #Plays 'good' music
            Garbage_collected.set_text("Pieces of garbage collected: " + str(Number_garbage)) #Updates for display on screen
            choice_garbage = random.randrange(1,3) #Either a coke can or candy wrapper is created
            if choice_garbage == 1:
                coke = MySprites.Coke()
                GarbageGroup.add(coke)
            elif choice_garbage == 2:
                wrapper = MySprites.Wrapper()
                GarbageGroup.add(wrapper)

        #Collision between player and Fishes
        if pygame.sprite.spritecollide(player, FishGroup, True):
            Number_fish += 1
            splash.play() #Plays 'bad' music
            Fish_harmed.set_text("Fishes harmed: " + str(Number_fish))
            x_cor = random.randint(100, 700)
            y_cor = random.randint(100, 500)
            fish = MySprites.Fish(x_cor, y_cor)
            FishGroup.add (fish)
            if Number_fish == 3: #Exits loop if 3 fishes are harmed
                keepGoing = False

        
        #Refresh display
        screen.blit(background, (0,0))
                
        otherGroup.clear(screen, background)
        GarbageGroup.clear(screen, background)
        FishGroup.clear(screen, background)

        otherGroup.update()
        GarbageGroup.update()
        FishGroup.update()

        otherGroup.draw(screen)
        GarbageGroup.draw(screen)
        FishGroup.draw(screen)

        pygame.display.flip()

    Screens.close_screen(Number_garbage) #Calls the closing screen

    #Close the game window
    pygame.quit()

#Starts the game!
main()

  

