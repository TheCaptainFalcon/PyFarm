import pygame
import time
import random
from itertools import cycle
import coke
import os
import subprocess
import runpy

pygame.init()
pygame.mixer.pre_init
pygame.mixer.init


selection = pygame.mixer.Sound("snd/jump3.wav")

width = 1024
height = 768

# Color
black = (0,0,0)
white = (255,255,255)
green =(0, 200, 0)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((width, height))
menuImg = pygame.image.load("images/farm.jpg")
woodImg = pygame.image.load("images/wood_mod3.png")
foodImg = pygame.image.load("images/food.png")

pygame.display.set_caption("PyFarm")
pygame.display.set_icon(foodImg)


 #FONT
font_title = "font/dimbo_regular.ttf"
font_name = "font/retro.ttf"

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(woodImg, (x,y))

def press():
    instruct = True
    click = pygame.mouse.get_pressed()

    while instruct:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()

            elif click[0] == 1 or event.type == pygame.KEYDOWN:
                game_instruct()
   
            
def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font(font_title, 70)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((width/2),(height/2) )
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

# def crash():
#     message_display("You Crashed")


def farm(x1,y1):
    gameDisplay.blit(menuImg, (x1,y1))    

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                pygame.mixer.Sound.play(selection)
                game_instruct()
            elif action == "quit":
                pygame.quit()
            
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smalltext= pygame.font.Font(font_title, 40)
    textsurf, textrect =text_objects(msg, smalltext)
    textrect.center = (( x + (w/2), y+ (h/2)) )
    gameDisplay.blit(textsurf, textrect)

# def blinking():
#     clock = pygame.time.Clock()
#     gameDisplay_rect = gameDisplay.rect()

#     BLINK_EVENT = pygame.USEREVENT + 0

#     font = pygame.font.Font(font_title, 50)
#     on_text_surface = font.render(
#         'Press Any Key To Start', True, pygame.Color('white'))
#     # blink_rect = on_text_surface.get_rect()
#     # blink_rect.center = gameDisplay_rect.center
#     off_text_surface = pygame.Surf
#     blink_surfaces = cycle([on_text_surface, off_text_surface])
#     blink_surface = next(blink_surfaces)
#     pygame.time.set_timer(BLINK_EVENT, 1000)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == BLINK_EVENT:
#                 blink_surface = next(blink_surfaces)

#         gameDisplay.blit(blink_surface, blink_rect)
#         pygame.display.update()
#         clock.tick(60)

def game_intro():
    pygame.mixer.music.load("snd/how_it_began.wav")
    pygame.mixer.music.play(-1)
    x1 = (width *-.19)
    y1 = (height * .00005)

    x = (width * .37 )
    y = (height * .19 )

    clock = pygame.time.Clock()
    intro = True
    while intro:
        for event in pygame.event.get():
            
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        farm(x1,y1)
        car(x,y)
        
        largetext = pygame.font.Font(font_title, 70)
        textsurf, textrect = text_objects("PyFarm", largetext)
        textrect.center = ((width/2),(height/3) )
        gameDisplay.blit(textsurf, textrect)


        button("START", 150,550,100,50, white, green, "play")
        button("QUIT", 750,550,100,50, white, red, "quit")
  



        pygame.display.update()
        clock.tick(15)

def game_instruct():
    game_instruct == True
    gameDisplay.fill(black)
                
    #USE FOR SECOND SCREEN
    # Sub-Title Text
    font = pygame.font.Font(font_name, 50)
    sub_text = font.render("Use Arrow Keys to Move", True, white)
    gameDisplay.blit(sub_text, (300,250))    

    #Sub-Title Text 2
    font = pygame.font.Font(font_name, 50)
    sub_text = font.render("Press Space to Interact", True, white)
    gameDisplay.blit(sub_text, (295, 300))   

    #Sub-Title Text 3
    font = pygame.font.Font(font_name, 50)
    sub_text = font.render("Press \"c\" to also interact", True, white)
    gameDisplay.blit(sub_text, (220, 350))

    #Sub-Title Text 4
    font = pygame.font.Font(font_name, 45)
    sub_text = font.render("Press any key to Begin", True, green)
    gameDisplay.blit(sub_text, (325, 450))


    pygame.display.update()

    while game_instruct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            else:
                

                

               

                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(selection)
                    pygame.mixer.music.stop()
                    game_loop()
                    

def game_loop(): #REPLACE WITH MAIN GAME LOOP
    # x = (width * .4 )
    # y = (height * .4 )

    # x_change = 0 

    

    pygame.display.set_caption("PyFarm")

    clock = pygame.time.Clock()

    # gameExit = False

    # while not gameExit:

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()

    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_LEFT:
    #                 x_change = -5
    #             elif event.key == pygame.K_RIGHT:
    #                 x_change = 5

    #         if event.type == pygame.KEYUP:
    #             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #                 x_change = 0
 
 
    gameDisplay.fill(black)    


    runpy.run_path("coke.py")


    pygame.display.update()

    clock.tick(60)
    
game_intro()
game_instruct()
game_loop()
pygame.quit()
quit()