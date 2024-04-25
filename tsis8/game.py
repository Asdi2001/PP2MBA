import pygame
import sys

pygame.init()

# Цвета в формате RGB
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Размеры окна
W, H = 800, 600
FPS = 60 #частота кадров в секунду

# Создание окна
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE) # создает окно с указанными размерами
pygame.display.set_caption("BOUNCING BALL") #заголовок окна
clock = pygame.time.Clock() # управления скорости 

# Начальные параметры мяча
radius = 10 # радиус мяча
x, y = W // 2, H // 2 # изначальные координаты мяча
speed_x, speed_y = 5, 5 # скорость по оси x,y
radius2 = 15 # радиус для второго мяча
x2, y2 = W // 3, H // 3 # изначальные координаты второго мяча
speed_x2, speed_y2 = -5, -5 # скорость по оси x,y
radius3 = 5 # радиус для третьего мяча
x3, y3 = W // 4, H // 4 # изначальные координаты третьего мяча
speed_x3, speed_y3 = 3, -3 # скорость по оси x,y

# Начальные параметры блоков
block1_x, block1_y = 200, 300 # Параметры первого блока
block1_width, block1_height = 100, 50
block2_x, block2_y = 500, 300 # Параметры второго блока
block2_width, block2_height = 100, 50

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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # в случае закрытия окна игры происходит выход из программы
            pygame.quit()
            sys.exit()
    
    handle_keys()
    
    # Движение мяча, обновляет координаты мяча
    x += speed_x
    y += speed_y
    x2 += speed_x2
    y2 += speed_y2
    x3 += speed_x3
    y3 += speed_y3
    
    # Обнаружение столкновений с краями окна
    if x + radius >= W or x - radius <= 0:
        speed_x = -speed_x # проверяет, достиг ли мяч правого или левого края окна. Если да, то меняет направление скорости по оси x, чтобы мяч отскочил от края.
    if y + radius >= H or y - radius <= 0:
        speed_y = -speed_y # проверяет, достиг ли мяч верхнего или нижнего края окна. Если да, то меняет направление скорости по оси y, чтобы мяч отскочил от края.
    if (block1_x <= x + radius <= block1_x + block1_width and
        block1_y <= y + radius <= block1_y + block1_height): #Проверка столкновения мяча с первым блоком-препятствием.
        speed_x = -speed_x
        speed_y = -speed_y
    if (block2_x <= x + radius <= block2_x + block2_width and
        block2_y <= y + radius <= block2_y + block2_height): #Проверка столкновения мяча со вторым блоком-препятствием.
        speed_x = -speed_x
        speed_y = -speed_y
        
    if x2 + radius2 >= W or x2 - radius2 <= 0:
        speed_x2 = -speed_x2
    if y2 + radius2 >= H or y2 - radius2 <= 0:
        speed_y2 = -speed_y2
    if (block1_x <= x2 + radius2 <= block1_x + block1_width and
        block1_y <= y2 + radius2 <= block1_y + block1_height): #Проверка столкновения мяча с первым блоком-препятствием.
        speed_x2 = -speed_x2
        speed_y2 = -speed_y2
    if (block2_x <= x2 + radius <= block2_x + block2_width and
        block2_y <= y2 + radius <= block2_y + block2_height): #Проверка столкновения мяча со вторым блоком-препятствием.
        speed_x2 = -speed_x2
        speed_y2 = -speed_y2
        
    if x3 + radius3 >= W or x3 - radius3 <= 0:
        speed_x3 = -speed_x3
    if y3 + radius3 >= H or y3 - radius3 <= 0:
        speed_y3 = -speed_y3
    if (block1_x <= x3 + radius3 <= block1_x + block1_width and
        block1_y <= y3 + radius3 <= block1_y + block1_height): #Проверка столкновения мяча с первым блоком-препятствием.
        speed_x3 = -speed_x3
        speed_y3 = -speed_y3
    if (block2_x <= x3 + radius3 <= block2_x + block2_width and
        block2_y <= y3 + radius3 <= block2_y + block2_height): #Проверка столкновения мяча со вторым блоком-препятствием.
        speed_x3 = -speed_x3
        speed_y3 = -speed_y3
        
    # Обнаружение столкновений между мячами и отталкивание их друг от друга
    dx1 = x - x2 # Вычисляем разницу по оси x между координатами первого мяча и второго мяча.
    dy1 = y - y2 # Вычисляем разницу по оси y между координатами первого мяча и второго мяча.
    distance1 = (dx1**2 + dy1**2)**0.5 # Вычисляем расстояние между центрами двух мячей с помощью теоремы Пифагора
    if distance1 < 2 * radius: #  Проверяем, если расстояние меньше, чем сумма радиусов двух мячей 
        speed_x, speed_y = -speed_x, -speed_y # Меняем направление скорости первого мяча на противоположное
        speed_x2, speed_y2 = -speed_x2, -speed_y2 # Меняем направление скорости второго мяча на противоположное

    dx2 = x - x3 # Вычисляем расстояние по оси x между первым и третьим мячами
    dy2 = y - y3 # Вычисляем расстояние по оси y между вторым и третьим мячами
    distance2 = (dx2**2 + dy2**2)**0.5
    if distance2 < 2 * radius: # Проверяем столкновение первого и третьего мячей и меняем их скорости при необходимости
        speed_x, speed_y = -speed_x, -speed_y
        speed_x3, speed_y3 = -speed_x3, -speed_y3

    dx3 = x2 - x3 # Вычисляем расстояние по оси x между вторым и третьим мячами
    dy3 = y2 - y3 # Вычисляем расстояние по оси y между вторым и третьим мячами
    distance3 = (dx3**2 + dy3**2)**0.5
    if distance3 < 2 * radius2: # Проверяем столкновение второго и третьего мячей и меняем их скорости при необходимости
        speed_x2, speed_y2 = -speed_x2, -speed_y2
        speed_x3, speed_y3 = -speed_x3, -speed_y3

        
    # Отрисовка
    screen.fill(WHITE) # заполняет экран белым цветом перед отрисовкой мяча, чтобы не было следов от движения мяча
    pygame.draw.circle(screen, BLUE, (x, y), radius) # рисует первый мяч 
    pygame.draw.circle(screen, GREEN, (x2, y2), radius2) # рисует второй мяч 
    pygame.draw.circle(screen, RED, (x3, y3), radius3) # рисует третий мяч 
    pygame.draw.rect(screen, BLUE, (block1_x, block1_y, block1_width, block1_height)) # рисует первый блок
    pygame.draw.rect(screen, GREEN, (block2_x, block2_y, block2_width, block2_height)) # рисует второй блок
    pygame.display.flip() # просто обновление экрана при перемещении мяча
    clock.tick(FPS) #  делает движение мяча более плавным и контролируемым, уменьшая нагрузку на процессор