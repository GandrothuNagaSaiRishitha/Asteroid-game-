#i wanrt to create a simple game as of now
import pygame
from sys import exit

pygame.init() #initialzing the pygame
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Asteriod Game')
#to control framerate of the game(ideally 60 frs)
clock=pygame.time.Clock()

while True:
    #here it creates elements and updates it in screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update
    clock.tick(60)
    
