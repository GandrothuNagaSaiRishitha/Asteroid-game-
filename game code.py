
import pygame
from sys import exit

pygame.init() 
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Asteriod Game')
#to control framerate of the game(ideally 60 frs)
clock=pygame.time.Clock()
#first we must set the surface, include the background and game asthetics in the surface and then like push it into the display.
screen_test=pygame.image.load("graphics/space background.png").convert_alpha()
asteriod_pic=pygame.image.load("graphics/asteroid pic.jpg").convert_alpha()
new_asteriod_pic=pygame.transform.scale(asteriod_pic,(100,100))



yoda=pygame.image.load("graphics/8d4cff7a-c7e4-4ec9-9567-3bd4e9cb25a7.png")
new_yoda=pygame.transform.scale(yoda,(100,100))
ast_x=0
ast_y=0
while True:
    #here it creates elements and updates it in screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(screen_test,(0,0))
    screen.blit(new_yoda,(650,250))
    ast_x+=1
    ast_y+=1 
    if ast_x>800:
        ast_x=10
    elif ast_y>500:
        ast_y=100
    screen.blit(new_asteriod_pic,(ast_x,ast_y))

    pygame.display.update()
    clock.tick(60)
    
