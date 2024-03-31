import pygame 
import sys

weight = 800
height = 600

screen = pygame.display.set_mode((weight, height))

white = (255,255,255)
red = (255,0,0)

rad = 25
ballx = weight // 2
bally = height // 2
speed = 20
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP] and bally>0:
        bally -= speed
    if keys[pygame.K_DOWN] and bally < height:
        bally +=speed
    if keys[pygame.K_LEFT] and ballx > 0:
        ballx -= speed
    if keys[pygame.K_RIGHT] and ballx < weight:
        ballx += speed
    
    screen.fill(white)
    pygame.draw.circle(screen,red,(ballx, bally), rad)
    pygame.display.flip()
    clock.tick(30)