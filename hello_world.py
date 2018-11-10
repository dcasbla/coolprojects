import pygame
import time
import random

pygame.init()

display_with = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_blue = (142,255,249)

boat_with =  100

gameDisplay = pygame.display.set_mode((display_with,display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

boatImg = pygame.image.load('boat.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:"+str(count),True, black)
    gameDisplay.blit(text,(0,0))

def boat(x,y):
    gameDisplay.blit(boatImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def crash():
    message_display('You Crashed')

def text_objects(text, font):
    TextSurface = font.render(text, True, black)
    return TextSurface, TextSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_with/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    pygame.event.clear()
    time.sleep(2)

    game_loop()

def game_loop():
    x = (display_with * 0.45)
    y = (display_height * 0.75 )

    x_change = 0

    thing_startx = random.randrange(0, display_with)
    thing_starty = -600
    thing_speed = 15
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -30
                elif event.key == pygame.K_RIGHT:
                    x_change = 30

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key  == pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        gameDisplay.fill(light_blue)

        # (gameDisplay, color, [thingx, thingy, thingw, thingh])
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        boat(x,y)
        things_dodged(dodged)

        if x > display_with - boat_with or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_with)
            dodged += 1
            thing_speed += 2
        if thing_speed >= 36:
            thing_speed -= 4
        if thing_speed == 20:
            thing_speed += 2

        if y < thing_starty+thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + boat_with > thing_startx and x + boat_with < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
