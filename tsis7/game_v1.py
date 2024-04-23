#1 версия,учитываются клавиши для изменения траектории

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
speed_x, speed_y = 5, 5 # скорость мяча по оси x,y

# Игровой цикл 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # в случае закрытия окна игры происходит выход из программы
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # была ли нажита клавиша для изменения направления
            if event.key == pygame.K_UP:
                speed_y = -abs(speed_y) 
            elif event.key == pygame.K_DOWN:
                speed_y = abs(speed_y)
            elif event.key == pygame.K_LEFT:
                speed_x = -abs(speed_x)
            elif event.key == pygame.K_RIGHT:
                speed_x = abs(speed_x)

    # Движение мяча, обновляет координаты мяча
    x += speed_x
    y += speed_y

    # Обнаружение столкновений с краями окна
    if x + radius >= W or x - radius <= 0:
        speed_x = -speed_x # проверяет, достиг ли мяч правого или левого края окна. Если да, то меняет направление скорости по оси x, чтобы мяч отскочил от края.
    if y + radius >= H or y - radius <= 0:
        speed_y = -speed_y # проверяет, достиг ли мяч верхнего или нижнего края окна. Если да, то меняет направление скорости по оси y, чтобы мяч отскочил от края.

    # Отрисовка
    screen.fill(WHITE) # заполняет экран белым цветом перед отрисовкой мяча, чтобы не было следов от движения мяча
    pygame.draw.circle(screen, BLUE, (x, y), radius) # рисует сам мяч 
    pygame.display.flip() # просто обновление экрана при перемещении мяча
    clock.tick(FPS) #  делает движение мяча более плавным и контролируемым, уменьшая нагрузку на процессор

