# %% [markdown]
# Подключение библиотек

# %%
import tkinter as tk
import random
from time import time

# %% [markdown]
# Инициализация переменных

# %%
correct_answer = 0
start_time = 0
correct_count = 0
incorrect_count = 0
total_time = 0.0
best_time = None
correct_answer_time_count = 0

number_of_options = 5

win_width = 600
win_height = 500

# %% [markdown]
# Функция генерирующая пример

# %%
def generate_example():
    global correct_answer, start_time
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    
    operation = random.choice(["+", "-"])
    question = f"{a} {operation} {b} = ?"
    correct_answer = eval(f"{a} {operation} {b}") # Это вместо if-ов
    
    question_label.config(text=question)

    answers = [correct_answer]
    
    while len(answers) < number_of_options:
        wrong = correct_answer + random.randint(-10, 10)
        if wrong != correct_answer and wrong not in answers:
            answers.append(wrong)

    random.shuffle(answers) # Перемешиваем ответы

    for i in range(number_of_options):
        buttons[i].config(text=str(answers[i]))

    start_time = time()

# %% [markdown]
# Функция проверки правильности ответа

# %%
def check_answer(selected_value):
    global correct_count, incorrect_count, total_time, best_time, correct_answer_time_count
    elapsed = time() - start_time

    if selected_value == correct_answer:
        result_label.config(text="Верно!", fg="green")
        correct_count += 1
        
        total_time += elapsed
        correct_answer_time_count += 1
        if best_time is None or elapsed < best_time:
            best_time = elapsed
    else:
        result_label.config(text="Неправильно!", fg="red")
        incorrect_count += 1

    update_stats()
    win.after(50, generate_example())

# %% [markdown]
# Функция обновления статистики игрока

# %%
def update_stats():
    if correct_answer_time_count > 0:
        avg_time = total_time / correct_answer_time_count
        best_str = f"{best_time:.2f}с"
    else:
        avg_time = 0
        best_str = "–"

    stats_text = (
        f"Верно: {correct_count}\n"
        f"Ошибок: {incorrect_count}\n"
        f"Среднее время: {avg_time:.2f}с\n"
        f"Лучшее время: {best_str}"
    )
    stats_label.config(text=stats_text)

# %% [markdown]
# Создание окна

# %%
win = tk.Tk()

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)

win.title("Математический дартс")
win.geometry(f"{win_width}x{win_height}+{x}+{y}")

# %% [markdown]
# Отображение статистики

# %%
stats_label = tk.Label(win, text="", font=("Arial", 10), justify="left", anchor="nw", fg="blue")
stats_label.place(x=10, y=10)

# %% [markdown]
# Создание основных элементов интерейсов

# %%
question_label = tk.Label(win, text="", font=("Arial", 18))
question_label.pack(pady=20)

buttons = []
for i in range(number_of_options):
    btn = tk.Button(win, text="", font=("Arial", 14), width=10, height=2,
                    command=lambda i=i: check_answer(int(buttons[i].cget("text"))))
    btn.pack(pady=5)
    buttons.append(btn)

result_label = tk.Label(win, text="", font=("Arial", 14))
result_label.pack(pady=10)

# %% [markdown]
# Инициализация игры

# %%
generate_example()
update_stats()

win.mainloop()


