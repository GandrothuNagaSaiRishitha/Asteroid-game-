#i want to create a simple game as of now
import pygame
from sys import exit

pygame.init() #initialzing the pygame
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Asteriod Game')
#to control framerate of the game(ideally 60 frs)
clock=pygame.time.Clock()
#first we must set the surface, include the background and game asthetics in the surface and then like push it into the display.
screen_test=pygame.image.load()
while True:
    #here it creates elements and updates it in screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(screen_test,(200,100)) #fancy way of saying we want to put one surface on another
    
    pygame.display.update()
    clock.tick(60)
    
