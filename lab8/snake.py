import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Размеры экрана
screen_width = 800
screen_height = 600

# Размеры блока змейки и еды
block_size = 20

# Создание окна игры
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('snake')

clock = pygame.time.Clock()

# Функция отрисовки змейки
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

# Функция отрисовки еды
def draw_food(food_position):
    pygame.draw.rect(screen, red, [food_position[0], food_position[1], block_size, block_size])

# Функция для создания новой позиции еды
def generate_food():
    food_x = random.randint(0, (screen_width - block_size) // block_size) * block_size
    food_y = random.randint(0, (screen_height - block_size) // block_size) * block_size
    return (food_x, food_y)

# Основная функция игры
def main():
    snake = [(screen_width / 2, screen_height / 2)]
    snake_direction = (1, 0)  # Изначальное направление движения - вправо

    food_position = generate_food()

    score = 0

    while True:
        # Обработка событий Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Управление змейкой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake_direction = (1, 0)
        elif keys[pygame.K_UP]:
            snake_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            snake_direction = (0, 1)

        # Обновление позиции змейки
        new_head = (snake[0][0] + snake_direction[0] * block_size,
                    snake[0][1] + snake_direction[1] * block_size)

        # Проверка на столкновение с границами экрана
        if not (0 <= new_head[0] < screen_width and 0 <= new_head[1] < screen_height):
            pygame.quit()
            quit()

        # Проверка на столкновение с самой собой
        if new_head in snake[1:]:
            pygame.quit()
            quit()

        # Добавление новой головы змейки
        snake.insert(0, new_head)

        # Если змейка съела еду
        if new_head == food_position:
            food_position = generate_food()
            score += 1
        else:
            # Удаление последнего сегмента змейки, если не была съедена еда
            snake.pop()

        # Очистка экрана
        screen.fill(white)

        # Отрисовка змейки и еды
        draw_snake(snake)
        draw_food(food_position)

        # Отображение счета
        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Счет: " + str(score), True, black)
        screen.blit(score_text, (10, 10))

        # Обновление экрана
        pygame.display.update()

        # Ограничение частоты обновления экрана до 10 кадров в секунду
        clock.tick(10)

# Запуск игры
main()
