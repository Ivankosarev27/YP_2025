import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
dark_brown = (72, 60, 50)
light_brown = (210, 180, 140)
window_color = (173, 216, 230)
window_border_color = (255, 255, 255)
cross_color = (255, 255, 255)
cat_color = (255, 165, 0)  # Рыжий цвет для кошки
eye_color = (0, 255, 0)  # Зеленый цвет для глаз

# Задний фон
rect(screen, dark_brown, (0, 0, 400, 200))
rect(screen, light_brown, (0, 200, 400, 200))

# Параметры окна
window_x = 250
window_y = 50
window_width = 100
window_height = 75
window_border_width = 3

# Рисуем окно
rect(screen, window_color, (window_x, window_y, window_width, window_height))
rect(screen, window_border_color, (window_x, window_y, window_width, window_height), window_border_width)

# Рисуем крест
line(screen, cross_color, (window_x + window_width // 2, window_y), (window_x + window_width // 2, window_y + window_height), 3)
line(screen, cross_color, (window_x, window_y + window_height // 2), (window_x + window_width, window_y + window_height // 2), 3)

# --- Параметры кошки ---
cat_x = 200
cat_y = 320  # Подвинем кошку немного ниже
cat_scale = 1.2 # Увеличим размер кошки

# Голова
head_radius = int(30 * cat_scale)  # Уменьшим голову относительно тела
circle(screen, cat_color, (int(cat_x), int(cat_y - 50 * cat_scale)), head_radius)

# Тело
body_width = int(120 * cat_scale)  # Увеличиваем тело
body_height = int(70 * cat_scale)
ellipse(screen, cat_color, (int(cat_x - body_width // 2), int(cat_y - body_height // 2), body_width, body_height))

# Хвост (более изогнутый)
tail_length = int(80 * cat_scale)
tail_width = int(15 * cat_scale)
tail_x = int(cat_x + body_width // 2 - 15* cat_scale)
tail_y = int(cat_y + 20*cat_scale )
ellipse(screen, cat_color, (tail_x, tail_y - tail_length, tail_width, tail_length))

# Лапы
paw_width = int(20 * cat_scale)
paw_height = int(15 * cat_scale)
paw_y = int(cat_y + body_height // 2 )
paw_offset = int(body_width // 4 )

ellipse(screen, cat_color, (int(cat_x - body_width // 2 + paw_offset - paw_width//2), paw_y, paw_width, paw_height))
ellipse(screen, cat_color, (int(cat_x + body_width // 2 - paw_offset - paw_width//2), paw_y, paw_width, paw_height))

# Уши (треугольники, более реалистичное расположение)
ear_size = int(20 * cat_scale)
ear_offset = int(15 * cat_scale)

polygon(screen, (0, 0, 0), [(int(cat_x - ear_offset), int(cat_y - 80 * cat_scale)), (int(cat_x - 30*cat_scale), int(cat_y - 60*cat_scale)),
                    (int(cat_x - 10*cat_scale), int(cat_y - 60*cat_scale))])
polygon(screen, (0, 0, 0), [(int(cat_x + ear_offset), int(cat_y - 80 * cat_scale)), (int(cat_x + 30*cat_scale), int(cat_y - 60*cat_scale)),
                    (int(cat_x + 10*cat_scale), int(cat_y - 60*cat_scale))])

# Мордочка (нос и рот) - упрощенно
nose_radius = int(5 * cat_scale)
circle(screen, (255, 0, 0), (int(cat_x), int(cat_y - 60*cat_scale)), nose_radius) # красный нос

# Глаза
eye_radius = int(7 * cat_scale)
eye_offset = int(15 * cat_scale)
circle(screen, eye_color, (int(cat_x - eye_offset), int(cat_y - 50 * cat_scale)), eye_radius)
circle(screen, eye_color, (int(cat_x + eye_offset), int(cat_y - 50 * cat_scale)), eye_radius)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()