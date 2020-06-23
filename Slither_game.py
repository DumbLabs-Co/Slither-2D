import pygame,sys
import time
import random

#live update of score & speed increases with increase in snake length
pygame.init()
custom_red = (255,18,44)
desert_sand = (237,201,175)
red = (255,0,0)
cyber_yellow = (255,211,0)
chocolate_cosmos = (92,20,36)
english_red = (159,69,75)
white = (255,255,255)
green = (50,90,50)
black = (0,0,0)
window_width = 1200
window_height = 700

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Slither 2D')
bg_music = pygame.mixer.music.load("slither_song.mp3")
bg = pygame.image.load("slither_bg.jpg")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0

def myquit():
    pygame.quit()
    sys.exit(0)

font = pygame.font.SysFont(None, 25, bold=True)
font1 = pygame.font.SysFont(None, 30, bold=True, italic = True)

def drawGrid():
	sizeGrd = window_width // blockSize

def snake(blockSize, snakelist):
    for size in snakelist:
        pygame.draw.ellipse(gameDisplay, green,[size[0],size[1],blockSize,blockSize],10)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/6, window_height/2])

def message(msg, color):
    screen_text = font1.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/24, window_height/21])

def gameLoop():
    
    gameExit = False
    gameOver = False

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0
    snakelist = []
    snakeLength = 1
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.blit(bg, (0, 0))
            message_to_screen(score + "Game over, press p to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameLoop()           

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel

                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel

                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel

                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.blit(bg, (0,0))
        AppleThickness = 20

        pygame.draw.ellipse(gameDisplay, custom_red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        snake(blockSize, snakelist)
        pygame.display.update()
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
        speed = FPS + snakeLength/5
        score="Score: " + str((snakeLength-1)*10)+ "  "
        message(score,red)
        pygame.display.update()
        clock.tick(speed)
        
    pygame.quit()
    quit()
gameLoop()
