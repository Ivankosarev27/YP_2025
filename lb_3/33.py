import turtle

screen = turtle.Screen()
screen.setup(width=800, height=1000)
screen.bgcolor("white")  # Фон

turtle = turtle.Turtle()
turtle.speed(0)  # Максимальная скорость

# --- Функции для рисования ---

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Устанавливаем начало окружности
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# --- Рисуем элементы ---

# Задний фон (здание)
draw_rectangle(-400, 300, 800, 400, "#735725") # Верхняя часть здания
draw_rectangle(-400, -300, 800, 600, "#8B7355")  # Нижняя часть (земля)

# Окна
window_positions = [-250, 0, 250]
window_width = 150
window_height = 250

for x_pos in window_positions:
    draw_rectangle(x_pos - window_width//2, 350, window_width, window_height, "white") #Рамки
    draw_rectangle(x_pos - window_width//2 + window_width//3, 350, window_width//3, window_height, "#ADD8E6") #Стекла
    draw_rectangle(x_pos - window_width//2, 350 + window_height//3, window_width, window_height//3, "#ADD8E6") # Стекла

# Коты и клубки (примерно)
draw_circle(-100, -100, 50, "#696969")  # серый кот (упрощенно)
draw_circle(150, 100, 30, "#B0B0B0") #клубок

turtle.hideturtle() # Скрываем черепашку
screen.mainloop() # Держим окно открытым