import pygame
import sys

pygame.init()

# Цвета в формате RGB
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размеры окна
W, H = 800, 600
FPS = 60  # частота кадров в секунду

# Создание окна
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # создает окно с указанными размерами
pygame.display.set_caption("BOUNCING BALL")  # заголовок окна
clock = pygame.time.Clock()  # управления скорости

# Начальные параметры мяча
radius = 10  # радиус мяча
x, y = W // 2, H // 2  # изначальные координаты мяча
speed_x, speed_y = 5, 5  # скорость по оси x,y
radius2 = 15  # радиус для второго мяча
x2, y2 = W // 3, H // 3  # изначальные координаты второго мяча
speed_x2, speed_y2 = -5, -5  # скорость по оси x,y
radius3 = 5  # радиус для третьего мяча
x3, y3 = W // 4, H // 4  # изначальные координаты третьего мяча
speed_x3, speed_y3 = 3, -3  # скорость по оси x,y

# Начальные параметры блоков
block1_x, block1_y = 200, 300  # Параметры первого блока
block1_width, block1_height = 100, 50
block2_x, block2_y = 500, 300  # Параметры второго блока
block2_width, block2_height = 100, 50

# Создание словаря для хранения цветов препятствий
block_colors = {(block1_x, block1_y): BLUE, (block2_x, block2_y): GREEN}

# Параметры для пяти блоков сверху с промежутками
top_blocks = []
block_width = (W // 5) - 10  # ширина блока, учитывая промежуток в 10 пикселей
for i in range(5):
    block_x = i * (block_width + 10)
    block_y = 50
    top_blocks.append(pygame.Rect(block_x, block_y, block_width, 20))

# Загрузка звукового файла
pop_sound = pygame.mixer.Sound('/Users/asseldiyarova/Desktop/pp2/tsis7/crush.wav')
block_break_sound = pygame.mixer.Sound('/Users/asseldiyarova/Desktop/pp2/tsis7/break.wav')

# Обработка событий клавиатуры
def handle_keys():
    global speed_x, speed_y, speed_x2, speed_y2, speed_x3, speed_y3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed_y = -abs(speed_y)
        speed_y2 = -abs(speed_y2)
        speed_y3 = -abs(speed_y3)
    if keys[pygame.K_DOWN]:
        speed_y = abs(speed_y)
        speed_y2 = abs(speed_y2)
        speed_y3 = abs(speed_y3)
    if keys[pygame.K_LEFT]:
        speed_x = -abs(speed_x)
        speed_x2 = -abs(speed_x2)
        speed_x3 = -abs(speed_x3)
    if keys[pygame.K_RIGHT]:
        speed_x = abs(speed_x)
        speed_x2 = abs(speed_x2)
        speed_x3 = abs(speed_x3)

# Игровой цикл
all_absorbed = False
absorbed_count = 0
destroyed_blocks = 0
eaten_balls = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # в случае закрытия окна игры происходит выход из программы
            pygame.quit()
            sys.exit()

    handle_keys()

    # Обработка столкновений с препятствиями
    for block_x, block_y in block_colors.keys():
        if block_x <= x + speed_x + radius <= block_x + block1_width and block_y <= y + speed_y + radius <= block_y + block1_height:
            speed_x = -speed_x
            speed_y = -speed_y
            block_colors[(block_x, block_y)] = BLUE  # меняем цвет препятствия на цвет мяча
        if block_x <= x2 + speed_x2 + radius2 <= block_x + block1_width and block_y <= y2 + speed_y2 + radius2 <= block_y + block1_height:
            speed_x2 = -speed_x2
            speed_y2 = -speed_y2
            block_colors[(block_x, block_y)] = GREEN  # меняем цвет препятствия на цвет мяча
        if block_x <= x3 + speed_x3 + radius3 <= block_x + block1_width and block_y <= y3 + speed_y3 + radius3 <= block_y + block1_height:
            speed_x3 = -speed_x3
            speed_y3 = -speed_y3
            block_colors[(block_x, block_y)] = RED  # меняем цвет препятствия на цвет мяча

    # Обработка столкновений с верхними блоками
    for block in top_blocks[:]:
        if block.collidepoint(x, y) or block.collidepoint(x + radius, y) or block.collidepoint(x - radius, y):
            speed_y = -speed_y
            top_blocks.remove(block)
            destroyed_blocks += 1
            block_break_sound.play()
        elif block.collidepoint(x2, y2) or block.collidepoint(x2 + radius2, y2) or block.collidepoint(x2 - radius2, y2):
            speed_y2 = -speed_y2
            top_blocks.remove(block)
            destroyed_blocks += 1
            block_break_sound.play()
        elif block.collidepoint(x3, y3) or block.collidepoint(x3 + radius3, y3) or block.collidepoint(x3 - radius3, y3):
            speed_y3 = -speed_y3
            top_blocks.remove(block)
            destroyed_blocks += 1
            block_break_sound.play()

    # Движение мяча, обновляет координаты мяча
    x += speed_x
    y += speed_y
    x2 += speed_x2
    y2 += speed_y2
    x3 += speed_x3
    y3 += speed_y3

    # Обработка столкновений мячей
    dx1 = x - x2
    dy1 = y - y2
    distance1 = (dx1**2 + dy1**2)**0.5
    if distance1 < radius + radius2 and not all_absorbed:
        if radius > radius2:
            radius += radius2
            x2, y2 = -100, -100
            pop_sound.play()
        else:
            radius2 += radius
            x, y = -100, -100
            pop_sound.play()
        absorbed_count += 1
        eaten_balls += 1

    dx2 = x - x3
    dy2 = y - y3
    distance2 = (dx2**2 + dy2**2)**0.5
    if distance2 < radius + radius3 and not all_absorbed:
        if radius > radius3:
            radius += radius3
            x3, y3 = -100, -100
            pop_sound.play()
        else:
            radius3 += radius
            x, y = -100, -100
            pop_sound.play()
        absorbed_count += 1
        eaten_balls += 1

    dx3 = x2 - x3
    dy3 = y2 - y3
    distance3 = (dx3**2 + dy3**2)**0.5
    if distance3 < radius2 + radius3 and not all_absorbed:
        if radius2 > radius3:
            radius2 += radius3
            x3, y3 = -100, -100
            pop_sound.play()
        else:
            radius3 += radius2
            x2, y2 = -100, -100
            pop_sound.play()
        absorbed_count += 1
        eaten_balls += 1

    # Проверка, все ли мячи были поглощены
    if absorbed_count == 2:  # Измените значение на количество всех мячей
        all_absorbed = True
        pop_sound.stop()

    # Обработка столкновений с краями окна
    if x + radius >= W or x - radius <= 0:
        speed_x = -speed_x
    if y + radius >= H or y - radius <= 0:
        speed_y = -speed_y
    if x2 + radius2 >= W or x2 - radius2 <= 0:
        speed_x2 = -speed_x2
    if y2 + radius2 >= H or y2 - radius2 <= 0:
        speed_y2 = -speed_y2
    if x3 + radius3 >= W or x3 - radius3 <= 0:
        speed_x3 = -speed_x3
    if y3 + radius3 >= H or y3 - radius3 <= 0:
        speed_y3 = -speed_y3

    # Отрисовка
    screen.fill(WHITE)  # заполняет экран белым цветом перед отрисовкой мяча, чтобы не было следов от движения мяча
    if not all_absorbed:
        pygame.draw.circle(screen, BLUE, (x, y), radius)  # рисует первый мяч
        pygame.draw.circle(screen, GREEN, (x2, y2), radius2)  # рисует второй мяч
        pygame.draw.circle(screen, RED, (x3, y3), radius3)  # рисует третий мяч
    else:
        pygame.draw.circle(screen, BLUE, (x, y), radius)  # рисует первый мяч
        pygame.draw.circle(screen, GREEN, (x2, y2), radius2)  # рисует второй мяч
        pygame.draw.circle(screen, RED, (x3, y3), radius3)  # рисует третий мяч
    for block_x, block_y in block_colors.keys():
        pygame.draw.rect(screen, block_colors[(block_x, block_y)], (block_x, block_y, block1_width, block1_height))  # рисует блоки
    for block in top_blocks:
        pygame.draw.rect(screen, RED, block)  # рисует верхние блоки
    font = pygame.font.Font(None, 36)
    text = font.render(f"Destroyed Blocks: {destroyed_blocks}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    text = font.render(f"Eaten Balls: {eaten_balls}", True, (0, 0, 0))
    screen.blit(text, (10, 50))
    pygame.display.flip()  # просто обновление экрана при перемещении мяча
    clock.tick(FPS)  # делает движение мяча более плавным и контролируемым, уменьшая нагрузку на процессор
