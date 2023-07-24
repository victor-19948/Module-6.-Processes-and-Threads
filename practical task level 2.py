from multiprocessing.pool import ThreadPool
import time
from datetime import datetime

names = ['Альфа', 'Бета', 'Гамма', 'Дельта', 'Эпсилон']


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


t_start = time.time()
for i in range(len(names)):
    get_thread(names[i])
t1 = (time.time() - t_start)

t_start = time.time()
with ThreadPool(processes=len(names)) as executor:
    executor.map(get_thread, names)
t2 = (time.time() - t_start)

t_difference = t1 - t2

print(f'Время последовательного запуска: {t1} секунд')
print(f'Время параллельного запуска: {t2} секунд')
print(f'Разница во времени: {t_difference} секунд')
