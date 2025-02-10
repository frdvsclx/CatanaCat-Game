import pygame 
import math
from sys import exit

def display_score():
    current_time= pygame.time.get_ticks() - start_time #gives time since pygame started
    score_surf=font.render(current_time/1000,False,'black')
    score_rect= score_surf.get_rect(center= (400,50)) 
    screen.blit(score_surf,score_rect)   

pygame.init() #initializing pygame

screen=pygame.display.set_mode((800,400)) #creating display screen
pygame.display.set_caption('Katana Run!') #naming the game
clock = pygame.time.Clock() #for fps stability
font= pygame.font.Font('font/Pixeltype.ttf',50)
isgameactive= True
start_time= 0

#creating surface and importing images:  
background_surf= pygame.image.load('images/sky2.png').convert_alpha() #convert_alpha: python analizes images much easier
background_width= background_surf.get_width()
ground_surf= pygame.image.load('images/ground.png').convert_alpha()

#infinite sky
scroll=0
tiles= math.ceil(800 / background_width) +1

#characters and snail:
player_surf= pygame.image.load('images\katana kedy.png').convert_alpha()
player_rect= player_surf.get_rect(midbottom= (100,270))
player_gravity= 0

cucumber_surf = pygame.image.load('images/cucumber.png').convert_alpha()
cucumber_rect = cucumber_surf.get_rect(midbottom= (500,270))

#score_surf= font.render('my game',True,'Black')
#score_rect= score_surf.get_rect(center= (400,50)) 


while True: 
    
    for event in pygame.event.get(): #looking for inputs, event for real time actions 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
            
      
        if isgameactive: 
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >=265: #down and up: clicking or not  
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
                        
            if event.type == pygame.KEYDOWN: #check if a key is pressed on the keyboard          
                if event.key == pygame.K_SPACE and player_rect.bottom >=265 :
                        player_gravity = -20
                        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                isgameactive=  True
                cucumber_rect.left= 1000
                start_time= pygame.time.get_ticks()
                                        
    #the longer you fall, the faster you fall 
    
    if isgameactive:
        
        for i in range(0,tiles):
            screen.blit(background_surf,(i*background_width + scroll,0))
    
    
        scroll -=3
        if abs(scroll) > background_width:
            scroll=0
                  
                     
        screen.blit(ground_surf,(0,265)) #block image transfer// putting to surface 
        #pygame.draw.rect(screen,'black',score_rect) 
        #pygame.draw.line(screen,'gold',(0,0),(800,400),10)
        #screen.blit(score_surf,score_rect)

        cucumber_rect.x -=4
        if cucumber_rect.right <=0: cucumber_rect.left = 800
        screen.blit(cucumber_surf,cucumber_rect)
        
    
        #player:
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >=265: player_rect.bottom = 270
        screen.blit(player_surf,player_rect)
        
        #collison
        if cucumber_rect.colliderect(player_rect): #player and snail if thouch  
            pygame.draw.line
            isgameactive = False
    
    
    #else: 
        
    
    #-----------stuff--------------------
    #keys= pygame.key.get_pressed() ##outputs 0 or 1, basılanları saklar?    
    #if keys[pygame.K_SPACE]: 
        #jump
    
    #if player_rect.colliderect(snail_rect): #collision check
    #    print('ded')
    
    #mouse_pos= pygame.mouse.get_pos() #getting mouse pos mouse pressed-> (left,mid,right)
    #if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    clock.tick(60) 
