import pygame
import random 
from os import path
import random 
import math 
import tester2
from itertools import cycle
import subprocess
import runpy

WIDTH = 1024
HEIGHT = 768
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0,255,0)

#initializing pygame and sound 
pygame.init()
pygame.mixer.init()


#set up game folders
game_folder = path.dirname(__file__)
images_folder = path.join(game_folder, "images")
snd_folder = path.join(game_folder, "snd")

#load  images 
spritesheet = pygame.image.load(path.join(images_folder, 'player_walk.png'))
player_img = pygame.image.load(path.join(images_folder, 'farmer.png'))


fishing_img = pygame.image.load(path.join(images_folder, 'fishing.png'))
bg_img = pygame.image.load(path.join(images_folder,'farm2.png'  ))
corn_start = pygame.image.load(path.join(images_folder, 'corn_start.png'))
corn_mid = pygame.image.load(path.join(images_folder, "corn_mid.png"))
corn_full = pygame.image.load(path.join(images_folder, 'corn_full_2.png'))
chicken = pygame.image.load(path.join(images_folder,"chicken.png"))
llama_img = pygame.image.load(path.join(images_folder,"llama.png"))
small_fish = pygame.image.load(path.join(images_folder,"smallfish.png"))
medium_fish = pygame.image.load(path.join(images_folder,"mediumfish.png"))
large_fish = pygame.image.load(path.join(images_folder,"largefish.png"))
house = pygame.image.load(path.join(images_folder,"house.png"))
car = pygame.image.load(path.join(images_folder,"carImg.png"))
boat = pygame.image.load(path.join(images_folder,"rowboat.png"))
foodImg = pygame.image.load("images/food.png")
pygame.display.set_icon(foodImg)




#load music
pygame.mixer_music.load(path.join(snd_folder,"snowy.wav"))
pygame.mixer.music.set_volume(.4)

#screen display and clock setting 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PyFarm")
clock = pygame.time.Clock()

#creating classes for player, interaction zones, corn, animals
class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        self.image = player_img
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
            # self.image = pygame.image.load(os.path.join(img_folder, "character_image.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x=500
        self.rect.y=350
        self.llama_count = 0
        self.chicken_count = 0
        # self.last_update = 0
        # self.current_frame = 0
        # self.walk_r_frames = [player_walk_r_0,player_walk_r_1,player_walk_r_2,player_walk_r_3]
        
        #Literal copy and paste here until next comment because sprite animation in pygame sucks ass
       
        self.sheet = spritesheet
        self.sheet.set_clip(pygame.Rect(0, 0, 45, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

        #how do rectangles work
        self.left_states = { 0: (180, 0, 45, 45), 1: (225, 0, 45, 45), 2: (270, 0, 45, 45) , 3:(315,0,45,45)}
        self.right_states = { 0: (0, 0, 45, 45), 1: (45, 0, 45, 45), 2: (90, 0, 45, 45), 3:(135,0,45,45) }
        self.up_states = { 0: (0, 0, 45, 45), 1: (0, 0, 45, 45), 2: (0, 0, 45, 45), 3: (0, 0, 45, 45) }
        self.down_states = { 0: (0, 0, 45, 45), 1: (0, 0, 45, 45), 2: (0, 0, 45, 45), 3: (0, 0, 45, 45) }


    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 6
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 6
        if direction == 'up':
            self.rect.y -= 6
        if direction == 'down':
            self.rect.y += 6
 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])
 
        
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
    
    #plagiarism ends. what a stupid way to spell that word.
    # http://xorobabel.blogspot.com/2012/10/pythonpygame-2d-animation-jrpg-style.html
    
    # def update(self):
    #     self.speedx = 0
    #     self.speedy = 0
    #     keystate = pygame.key.get_pressed()
    #     if keystate[pygame.K_LEFT]:
    #         self.speedx = -4
    #     if keystate[pygame.K_RIGHT]:
    #         self.speedx = 4
    #     if keystate[pygame.K_UP]:
    #         self.speedy = -4
    #     if keystate[pygame.K_DOWN]:
    #         self.speedy = 4
    #     self.rect.x += self.speedx
    #     self.rect.y += self.speedy
    
    # def animate (self):
    #     now = pygame.time.get_ticks()
    #     if self.vel.x != 0
    #     if now - self.last_update
    

    def plant_1 (self):
        corn1 = Corn(60,580)
        all_sprites.add(corn1)
        inventory.haypenny -= 1
    
    def plant_2 (self):
        corn2 = Corn(318,580)
        all_sprites.add(corn2)
        inventory.haypenny -= 1

    
    def plant_3(self):
        corn3 = Corn(580,580)
        all_sprites.add(corn3)
        inventory.haypenny -= 1

    
    def plant_4(self):
        corn4 = Corn(835,580)
        all_sprites.add(corn4)
        inventory.haypenny -= 1

        
    def buy_chicken (self):
        chicken = Chicken(random.randrange(850,995),random.randrange(120,220))
        all_sprites.add(chicken)
        inventory.haypenny -= 24
    
    def collect_egg(self):
        inventory.haypenny += (self.chicken_count * 2)
        
    def buy_llama (self):
        llama = Llama(random.randrange(600,730),random.randrange(10,150))
        all_sprites.add(llama)
        llama_list.add(llama)
        inventory.haypenny -= 32
        self.llama_count += 1
        
    # def move_llama (self):
    #     llama_list.move_to_front()
    
    def collect_wool(self):
        inventory.haypenny += (self.llama_count * 4)

    def buy_house(self):
        house = House()
        all_sprites.add(house)
        inventory.haypenny -=100
    
    def buy_car(self):
        car = Car()
        all_sprites.add(car)
        inventory.haypenny -=70

    def buy_boat(self):
        boat = Boat()
        all_sprites.add(boat)
        inventory.haypenny -= 30


    def go_fish (self):
        self.image = fishing_img
        luck =  random.choice([0,1,2,3]) 
        if luck == 0:
            pass
        if luck == 1:
            smallfish = Smallfish()
            all_sprites.add(smallfish)
            inventory.haypenny += 1
        if luck ==2:
            mediumfish = Mediumfish()
            all_sprites.add(mediumfish)
            inventory.haypenny += 3
        if luck == 3:
            largefish = Largefish()
            all_sprites.add(largefish)
            inventory.haypenny += 6

    
    

  
        

class Actionzone_farming(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150,50))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x   #275
        self.rect.y = y   #475

class Actionzone_ranching(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x   #275
        self.rect.y = y   #475

class Corn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [corn_start,corn_mid,corn_full]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x     #318 for plot 2
        self.rect.y = y   #580 for plot 2
        self.grow_time = 4000
        self.grow_time2 = 10000
        self.last = pygame.time.get_ticks()
        self.can_harvest = False
        
    def update (self): 
        now = pygame.time.get_ticks()
        if now - self.last >= self.grow_time:
            self.image = self.images[1]
            if now - self.last >= self.grow_time2:
                self.image = self.images[2]
                self.can_harvest = True
            if self.can_harvest == True and player.rect.colliderect(self.rect):
                    self.harvest()
        
    def harvest (self):
        self.kill()
        inventory.haypenny +=4
    
   

  
        
    
class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,50))
        self.rect = self.image.get_rect()
        self.haypenny = 100

    
    



class Chicken(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = chicken
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.last = pygame.time.get_ticks()
        self.egg_timer = 8000
        
    
    # def update (self): 
    #     now = pygame.time.get_ticks()
    #     if now - self.last >= self.egg_timer:
    #         inventory.haypenny += 2
    

class Llama(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = llama_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.last = pygame.time.get_ticks()
        self.wool_timer = 12000
        
    # def move(self):    
    #     if player.buy_llama:
    #         self.LayeredUpdates.move_to_back

class Smallfish(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = small_fish
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 50
        self.display_time = 1500
        self.last = pygame.time.get_ticks()
        
    def update (self): 
        now = pygame.time.get_ticks()
        if now - self.last >= self.display_time:
            self.kill()

class Mediumfish(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = medium_fish
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 50
        self.display_time = 1500
        self.last = pygame.time.get_ticks()
        
    def update (self): 
        now = pygame.time.get_ticks()
        if now - self.last >= self.display_time:
            self.kill()

class Largefish(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = large_fish
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 50
        self.display_time = 1500
        self.last = pygame.time.get_ticks()
        
    def update (self): 
        now = pygame.time.get_ticks()
        if now - self.last >= self.display_time:
            self.kill()

class House(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = house
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 263

class Car(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = car
        self.rect = self.image.get_rect()
        self.rect.x = 43
        self.rect.y = 380

class Boat(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boat
        self.rect = self.image.get_rect()
        self.rect.x = 43
        self.rect.y = 30
    

   

        

    
#adding sprites to sprite group and creating instances for start up 
all_sprites = pygame.sprite.Group()
llama_list = pygame.sprite.Group()
layered_updates = pygame.sprite.LayeredUpdates
plants = pygame.sprite.Group()
player = Player((WIDTH/2, 500))
inventory = Inventory()
actionzone_farming_1 = Actionzone_farming(70,500)
actionzone_farming_2 = Actionzone_farming(295,500)
actionzone_farming_3 = Actionzone_farming(560,500)
actionzone_farming_4 = Actionzone_farming(830, 500)
action_zone_ranching_1 = Actionzone_ranching(650,350)
action_zone_ranching_2 = Actionzone_ranching(800,350)
action_zone_ranching_3 = Actionzone_ranching(180,110)
action_zone_shop = Actionzone_ranching(885,470)

# all_sprites.add(player)
all_sprites.add(actionzone_farming_1, actionzone_farming_2, actionzone_farming_3,actionzone_farming_4)
all_sprites.add(action_zone_ranching_1,action_zone_ranching_2, action_zone_ranching_3, action_zone_shop)
all_sprites.add(inventory)

pygame.mixer.music.play(loops=-1)
#game loop 

running = True 

while running: 
                     
    #keep running at right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        # check for closing window 
        if event.type == pygame.QUIT:
            running = False
        if  player.rect.colliderect(actionzone_farming_2.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.plant_2()
        if  player.rect.colliderect(actionzone_farming_1.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.plant_1()
        if  player.rect.colliderect(actionzone_farming_3.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.plant_3()
        if  player.rect.colliderect(actionzone_farming_4.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.plant_4()   
        if  player.rect.colliderect(action_zone_ranching_2.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.buy_chicken()
        if  player.rect.colliderect(action_zone_ranching_1.rect) and inventory.haypenny >= 32 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.buy_llama()
                    # player.move_llama()
        if  player.rect.colliderect(action_zone_ranching_1.rect) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                    player.collect_wool()
        if  player.rect.colliderect(actionzone_farming_2.rect) and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                player.plant_2()
        if  player.rect.colliderect(action_zone_ranching_3.rect) and event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                player.go_fish()
        if  player.rect.colliderect(action_zone_shop.rect) and inventory.haypenny >= 100 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9:
                    player.buy_house()
        if  player.rect.colliderect(action_zone_shop.rect) and inventory.haypenny >= 70 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                    player.buy_car()
        if  player.rect.colliderect(action_zone_shop.rect) and inventory.haypenny >= 30 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                    player.buy_boat()
    
     
    #update 
    all_sprites.update()
        #draw/render
    screen.blit(bg_img,(0,0))
    all_sprites.draw(screen)
        
    screen.blit(player.image, player.rect)
    player.handle_event(event)
    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()