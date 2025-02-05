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
snail_surf = pygame.image.load('images/iskelet.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom= (500,280))

player_surf= pygame.image.load('images\katana kedy.png').convert_alpha()
player_rect= player_surf.get_rect(midbottom= (40,281))

text_surf= font.render('my game',True,'Black')

while True: 
    for event in pygame.event.get(): #looking for inputs
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION: #down and up: clicking or not 
            

    screen.blit(background_surf,(0,0)) 
    screen.blit(ground_surf,(0,280)) #block image transfer// putting to surface 
    screen.blit(text_surf,(300,50))

    snail_rect.x -=4
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    
    if player_rect.colliderect(snail_rect): #collision check
        print('ded')
    
    mouse_pos= pygame.mouse.get_pos() #getting mouse pos mouse pressed-> (left,mid,right)
    if player_rect.collidepoint(mouse_pos):
        #pygame.mouse
    
    
    pygame.display.update()
    clock.tick(60) 
