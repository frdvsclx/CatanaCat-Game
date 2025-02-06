import pygame 
from sys import exit


pygame.init() #initializing pygame

screen=pygame.display.set_mode((800,400)) #creating display screen
pygame.display.set_caption('Katana Run!')
clock = pygame.time.Clock()
font= pygame.font.Font('font/Pixeltype.ttf',50)


#creating character surface
background_surf= pygame.image.load('images/backgrounds.png').convert_alpha() #convert_alpha: python analizes images much easier
ground_surf= pygame.image.load('images/ground.png').convert_alpha()

player_surf= pygame.image.load('images\katana kedy.png').convert_alpha()
player_rect= player_surf.get_rect(midbottom= (60,281))
player_gravity= 0

snail_surf = pygame.image.load('images/iskelet.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom= (500,280))

score_surf= font.render('my game',True,'Black')
score_rect= score_surf.get_rect(center= (400,50)) 

while True: 
    for event in pygame.event.get(): #looking for inputs, event for real time actions 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >=281: #down and up: clicking or not  
            if player_rect.collidepoint(event.pos): 
                   player_gravity = -20
                    
        if event.type == pygame.KEYDOWN: #check if there is a keyboard button have been pressed         
             if event.key == pygame.K_SPACE and player_rect.bottom >=281 :
                    player_gravity = -20
                                     
    #the longer you fall, the faster you fall 
                 
    screen.blit(background_surf,(0,0)) 
    screen.blit(ground_surf,(0,280)) #block image transfer// putting to surface 
    #pygame.draw.rect(screen,'black',score_rect) 
    #pygame.draw.line(screen,'gold',(0,0),(800,400),10)
    screen.blit(score_surf,score_rect)

    snail_rect.x -=4
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    
    
    #player:
    player_gravity +=1
    player_rect.y += player_gravity
    if player_rect.bottom >=280: player_rect.bottom = 281
    screen.blit(player_surf,player_rect)
    
    
    
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
