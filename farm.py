import pygame

#PYGAME INITIALIZATION
pygame.init()

#DISPLAY RESOLUTION
screen = pygame.display.set_mode((1024, 768))

#FONT VARIABLES/CONVERTER
    #render
def text_format(message, font, size, color):
    converted_font = pygame.font.SysFont(font, size)
    new_font = converted_font.render(message, 0, color)
    return new_font

#COLOR SHORTCUT
black = (0, 0, 0)

#FONT TYPE - SYS(TEST) 
font = "arial"


#MAIN MENU w/ SELECTION
def main_menu():
    menu = True
    selected = "start"
 
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected="start"
                elif event.key == pygame.K_DOWN:
                    selected="quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                    if selected == "quit":
                        pygame.quit()
                        quit()

#MENU UI/INTERFACE
        
        title=text_format("Farm Simulator", font, 90, black)
        if selected=="start":
            text_start=text_format("START", font, 75, black)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, black)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()




#TITLE AND ICON HEADER
#Icon 32x32 png
#icon("Variable name")
pygame.display.set_caption("Farming Simulator")
icon = pygame.image.load("images/food.png")
pygame.display.set_icon(icon)

#PLAYER - 64x64 png
#Player start location
# player_image = pygame.image.load(".png")
# playerx = 500
# playery = 350
# playerx_move = 0

#we add in x,y values in player() to assign new
#coordinates to help manipulate movement
#screen.blit() essentially draws an image
#2 values require png file and coordinates
# def player(x, y):
#     screen.blit(player_image, (x, y))

#WHILE LOOP - GAME
#Anything that persists continiuously must be in the loop
running = True
while running:

    #START LOOP
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running == False

        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:

    #BACKGROUND OF THE SCREEN
    #based on RGB values - screen.fill()
    screen.fill((10,100,0))
    pygame.display.update()