import pygame
import random
import time  

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 800
screen_height = 600

block_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('snake')

clock = pygame.time.Clock()

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def draw_food(food_position, food_weight):
    if food_weight == 1:
        pygame.draw.rect(screen, red, [food_position[0], food_position[1], block_size, block_size])
    elif food_weight == 2:
        pygame.draw.rect(screen, (255, 165, 0), [food_position[0], food_position[1], block_size * 2, block_size * 2])
    elif food_weight == 3:
        pygame.draw.rect(screen, (255, 215, 0), [food_position[0], food_position[1], block_size * 3, block_size * 3])

def generate_food():
    food_x = random.randint(0, (screen_width - block_size) // block_size) * block_size
    food_y = random.randint(0, (screen_height - block_size) // block_size) * block_size
    food_weight = random.randint(1, 3)  
    return (food_x, food_y), food_weight

def main():
    snake = [(screen_width / 2, screen_height / 2)]
    snake_direction = (1, 0)  

    food_position, food_weight = generate_food()

    score = 0

    food_timer = time.time()  
    food_duration = 5  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake_direction = (1, 0)
        elif keys[pygame.K_UP]:
            snake_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            snake_direction = (0, 1)

        new_head = (snake[0][0] + snake_direction[0] * block_size,
                    snake[0][1] + snake_direction[1] * block_size)

        # Проверка на столкновение с границами экрана и перемещение на противоположную сторону
        if new_head[0] < 0:
            new_head = (screen_width - block_size, new_head[1])
        elif new_head[0] >= screen_width:
            new_head = (0, new_head[1])
        elif new_head[1] < 0:
            new_head = (new_head[0], screen_height - block_size)
        elif new_head[1] >= screen_height:
            new_head = (new_head[0], 0)

        if new_head in snake[1:]:
            pygame.quit()
            quit()

        snake.insert(0, new_head)

        if new_head == food_position:
            food_position, food_weight = generate_food()
            score += food_weight
            food_timer = time.time()  
        else:
            snake.pop()

        if time.time() - food_timer > food_duration:
            food_position, food_weight = generate_food()
            food_timer = time.time()

        screen.fill(white)

        draw_snake(snake)
        draw_food(food_position, food_weight)

        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Счет: " + str(score), True, black)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(10)

main()
