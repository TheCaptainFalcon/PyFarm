from __future__ import absolute_import, division, print_function
from itertools import cycle
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/farm.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Background_Items(pygame.sprite.Sprite):
    def __init__(self, font, location):
        pygame.sprite.sprite.__init__(self)
        self.image = pygame.image.load("images/green_bg.jpg")       
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# BLINK 
BLINK_EVENT = pygame.USEREVENT + 0 

def main_menu():
    width = 1024
    height = 768
    black_color = (0, 0, 0)
    green_color = (0, 255, 0)
    purple_color = (128, 0, 128)
    white_color = (255,255,255)
    green_color = (0, 128, 0)
    transparent = (0,0,0,0)


    # pygame.mixer.init()
    # sound = pygame.mixer.Sound('.wav')
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('PyFarm')

    clock = pygame.time.Clock()
    #FONT
    font_title = "font/dimbo_regular.ttf"
    font_name = "font/retro.ttf"
    
    stop_game = False
    
    BackGround = Background('images/farm.jpg', [-195,0])
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    wood = pygame.image.load("images/wood_mod2.png")
    screen.blit(wood, (-325,-700))

    # Background_Items = Background("images/wood_mod.png", [-195,0])
    # pygame.draw(Background_Items.image, Background_Items.rect)

    # Title Text
    font = pygame.font.Font(font_title, 72)
    text = font.render('PyFarm', True, black_color)
    screen.blit(text, (422, 150))    


    # BLINK EFFECT
    press_any = pygame.font.Font("font/retro.ttf", 50)
    on_text_surface = press_any.render('Press Any Key To Start', True, white_color)
    blink_rect = on_text_surface.get_rect()
    blink_rect.center = screen_rect.center
    off_text_surface = pygame.Surface(blink_rect.size)
    blink_surfaces = cycle([on_text_surface, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)

    selected = "start"

    while not stop_game:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                
                # screen.fill(black_color)
                # pygame.display.update()
                # #USE FOR SECOND SCREEN
                # # Sub-Title Text
                # font = pygame.font.Font(font_name, 50)
                # sub_text = font.render("Use Arrow Keys to Move", True, white_color)
                # screen.blit(sub_text, (125,250))    

                # #Sub-Title Text 2
                # font = pygame.font.Font(font_name, 50)
                # sub_text = font.render("Press Space to Interact", True, white_color)
                # screen.blit(sub_text, (110, 300))   

                # #Sub-Title Text 3
                # font = pygame.font.Font(font_name, 50)
                # sub_text = font.render("Press \"c\" to remove fishing pole", True, white_color)
                # screen.blit(sub_text, (125, 350))

                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()    

                

                    


              
                if event.type == pygame.QUIT:
                    stop_game = True
                    pygame.quit()
                    quit()
            

        # BackGround = Background('images/menu.png', [0,0])
        # screen.fill([255, 255, 255])
        # screen.blit(BackGround.image, BackGround.rect)

        # # Title Text
        # font = pygame.font.Font(font_name, 70)
        # text = font.render('PyFarmville', True, green_color)
        # screen.blit(text, (265, 110))    

        # # Sub-Title Text
        # font = pygame.font.Font(font_name, 50)
        # sub_text = font.render("Use Arrow Keys to Move", True, black_color)
        # screen.blit(sub_text, (125,250))    

        # #Sub-Title Text 2
        # font = pygame.font.Font(font_name, 50)
        # sub_text = font.render("Press Space to Interact", True, black_color)
        # screen.blit(sub_text, (110, 300))        
        
        
        pygame.display.update()

        clock.tick(60)



    pygame.quit()

if __name__ == '__main__':
    main_menu()