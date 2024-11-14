import tkinter as tk
from tkinter import ttk

def check_triangle():
    try:
        # Получаем значения сторон треугольника из полей ввода
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        
        # Проверка на положительность сторон
        if a <= 0 or b <= 0 or c <= 0:
            result_label.config(text="Ошибка: Стороны треугольника должны быть положительными числами!", fg="red")
            return
        
        # Проверка существования треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            result_label.config(text="Ошибка: Такой треугольник не существует!", fg="red")
            return
        
        # Определение типа треугольника
        if a == b == c:
            result_label.config(text="Равносторонний треугольник", fg="green")
        elif a == b or b == c or a == c:
            result_label.config(text="Равнобедренный треугольник", fg="green")
        else:
            result_label.config(text="Разносторонний треугольник", fg="green")
    except ValueError:
        result_label.config(text="Ошибка: Пожалуйста, введите целые числа!", fg="red")

# Создание основного окна
root = tk.Tk()
root.title("Проверка типа треугольника")
root.geometry("400x400")
root.config(bg="#F0F8FF")  # Цвет фона окна

# Настройки для стилей
label_style = {'font': ('Arial', 12), 'bg': '#87CEEB', 'padx': 5, 'pady': 5}
entry_style = {'font': ('Arial', 12), 'bd': 2, 'relief': 'solid', 'width': 20}
button_style = {'font': ('Arial', 12, 'bold'), 'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45a049', 'relief': 'raised'}

# Метки и поля для ввода сторон
tk.Label(root, text="Сторона a:", **label_style).grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root, **entry_style)
entry_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Сторона b:", **label_style).grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root, **entry_style)
entry_b.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Сторона c:", **label_style).grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root, **entry_style)
entry_c.grid(row=2, column=1, padx=10, pady=10)

# Кнопка для проверки
button_check = tk.Button(root, text="Проверить", command=check_triangle, **button_style)
button_check.grid(row=3, column=0, columnspan=2, pady=20)

# Метка для вывода результата
result_label = tk.Label(root, text="", **label_style)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Добавление стиля к кнопке с эффектом при наведении
def on_enter(e):
    button_check['bg'] = '#45a049'

def on_leave(e):
    button_check['bg'] = '#4CAF50'

button_check.bind("<Enter>", on_enter)
button_check.bind("<Leave>", on_leave)

# Запуск приложения
root.mainloop()
