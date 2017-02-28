import pygame
import time
import random

pygame.init()

black = (0, 0, 0)          
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 180, 0)
dark_green = (0, 130, 0)
yellow = (255, 150, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('RPG')

clock = pygame.time.Clock()

block_size = 10

FPS = 30

font = pygame.font.SysFont(None, 25) 

# Defining snake function:
def snake(block_size, snakeList):
    for XnY in snakeList: # starting the growing of the snake
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# keep game loop as simple as possible
def gameLoop():
    gameEXIT = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1 # adding 1 to length of snake

    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0


    while not gameEXIT:

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:

                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                gameEXIT = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT: 

                    lead_x_change = -block_size

                    lead_y_change = 0

                elif event.key == pygame.K_RIGHT:

                    lead_x_change = block_size

                    lead_y_change = 0

                elif event.key == pygame.K_UP: 

                    lead_y_change = -block_size

                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:

                    lead_y_change = block_size

                    lead_x_change = 0



    # BOUNDARIES
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True


    # LOGIC LOOP:
        lead_x += lead_x_change
        lead_y += lead_y_change
        

        gameDisplay.fill(dark_green)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

    # snake growth
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(block_size, snakeList)

        pygame.display.update()

    # EVENT FOR SNAKE/APPLE COLLISION:
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
            snakeLength += 1

        clock.tick(FPS)


    pygame.quit()
    quit()



gameLoop()
