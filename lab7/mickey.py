import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

mickey_body = pygame.image.load("mainclock.png")  
mickey_hand_left = pygame.image.load("leftarm.png")  
mickey_hand_right = pygame.image.load("rightarm.png")  

#osnova
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
     #time
    current_time = datetime.now().time()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second
     
    screen.fill((255, 255, 255))

    screen.blit(mickey_body, (width // 2 - mickey_body.get_width() // 2, height // 2 - mickey_body.get_height() // 2))

    #second
    rotated_hand_left = pygame.transform.rotate(mickey_hand_left, -6 * second)
    screen.blit(rotated_hand_left, (width // 2 - rotated_hand_left.get_width() // 2, height // 2 - rotated_hand_left.get_height() // 2))

    #minutes
    rotated_hand_right = pygame.transform.rotate(mickey_hand_right, -6 * minute)
    screen.blit(rotated_hand_right, (width // 2 - rotated_hand_right.get_width() // 2, height // 2 - rotated_hand_right.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)