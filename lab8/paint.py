import pygame

def main():
    pygame.init()

    # Создание экрана 
    screen = pygame.display.set_mode((1920, 1080))


    clock = pygame.time.Clock()

    # Начальные значения для радиуса, координаты x и y, режима цвета и инструмента
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    tool = 'line'

    points = []

    POS = (-1, -1)

    # Начальный цвет (синий)
    color = (0, 0, 255)

    # Основной цикл программы
    while True:
        # Получение состояния нажатых клавиш
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # Если пользователь закрыл окно, завершить программу
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # Обработка комбинаций клавиш для выхода из программы
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                # Обработка нажатий клавиш для смены режима цвета и инструмента
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
            # Обработка события нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool == 'line':
                    # Изменение радиуса линии при нажатии кнопок мыши
                    if event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3:
                        radius = max(1, radius - 1)
                elif tool == 'circle':
                    # Рисование окружности при нажатии левой кнопки мыши
                    if event.button == 1:
                        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 50, 5)
                elif tool == 'rectangle':
                    # Захват начальной позиции при нажатии левой кнопки мыши
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if tool == 'rectangle':
                    # Рисование прямоугольника при отпускании левой кнопки мыши
                    if event.button == 1:
                        pygame.draw.rect(screen, color, (min(pygame.mouse.get_pos()[0], POS[0]),
                                                         min(POS[1], pygame.mouse.get_pos()[1]),
                                                         abs(pygame.mouse.get_pos()[0] - POS[0]),
                                                         abs(pygame.mouse.get_pos()[1] - POS[1])))
           
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                # Добавление текущей позиции мыши в список точек
                points = points + [position]
                # Ограничение списка точек до 256 элементов
                points = points[-256:]

        # Рисование линий между точками в зависимости от выбранного инструмента
        if tool == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
        # Использование ластика при нажатой левой кнопке мыши
        elif tool == 'eraser':
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 10)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение частоты обновления экрана до 60 кадров в секунду
        clock.tick(60)

# Функция для рисования линии между двумя точками
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Запуск основной функции
main()
