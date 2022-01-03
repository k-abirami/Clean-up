'''This file consists of the opening and closing screen for the Clean Up game'''

# I - Import 
import pygame

def open_screen():

    '''This function creates the opening screen. It accepts and returns no values'''

    #Initialize
    pygame.init()
    
    # D - Display configuration
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Introduction")

    # E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((178,223,238))

    #Two different font sizes
    mySystemFont_1 = pygame.font.SysFont("Calibri", 80)
    mySystemFont_2 = pygame.font.SysFont("Calibri", 30)

    #Messages to ensure game is more user friendly
    message_1 = mySystemFont_1.render("Clean Up!", 7, (0, 0, 0))
    message_2 = mySystemFont_2.render("Rules: Clean the ocean by picking up trash. ", 7, (25,25,112))
    message_3 = mySystemFont_2.render("Use arrow keys to move the player. ", 7, (25,25,112))
    message_4 = mySystemFont_2.render("Make sure to not hit any fishes. ", 7, (25,25,112))
    message_5 = mySystemFont_2.render("The game ends once you have hit 3 fishes. ", 7, (25,25,112))
    message_6 = mySystemFont_2.render("Become the ocean's savior by collecting 50 pieces of trash. ", 7, (25,25,112))
    message_7 = mySystemFont_2.render("Press space to start the game! ", 7, (0,0,0))
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    keepGoing = False
                
        # R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(message_1, (250, 100))
        screen.blit(message_2, (125, 250))
        screen.blit(message_3, (125, 300))
        screen.blit(message_4, (125, 350))
        screen.blit(message_5, (125, 400))
        screen.blit(message_6, (75, 450))
        screen.blit(message_7, (150, 525))
        
        pygame.display.flip()
        
    # Close the game window
    pygame.quit()

def close_screen(Trash):

    '''This function creates the closing screen. It accepts the number of garbage pieces collected
        It returns no values'''

    #Initailize
    pygame.init()
    
    # D - Display configuration
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Closing")

    # E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((178,223,238))

    mySystemFont_1 = pygame.font.SysFont("Calibri", 80)
    mySystemFont_2 = pygame.font.SysFont("Calibri", 40)

    #Message to encourage every user
    message_1 = mySystemFont_1.render("Congratulations!!!", 7, (0, 0, 0))

    if Trash >= 50:
        message_2 = mySystemFont_2.render("You are the ocean's savoir! ", 7, (25,25,112))
        message_3 = mySystemFont_2.render("You picked up " + str(Trash) + " pieces of trash!", 7, (25,25,112))

    else:
        message_2 = mySystemFont_2.render("You picked up " + str(Trash) + " pieces of trash!", 7, (25,25,112))
        message_3 = mySystemFont_2.render("", 7, (25,25,112))
        
    message_4 = mySystemFont_2.render("Press space to play again! ", 7, (0,0,0))
    message_5 = mySystemFont_2.render("Press 'q' to quit! ", 7, (0,0,0))
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    import Main_Game
                    Main_Game.main()#Calls main game if user wants to play again
                    pygame.quit()
                if event.key == pygame.K_q:
                    keepGoing = False
                    pygame.quit()
                    
        # R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(message_1, (150, 100))
        screen.blit(message_2, (150, 300))
        screen.blit(message_3, (150, 350))
        screen.blit(message_4, (150, 475))
        screen.blit(message_5, (150, 525))
        
        pygame.display.flip()
        
    # Close the game window
    pygame.quit()
