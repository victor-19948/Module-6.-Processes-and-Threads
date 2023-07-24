from multiprocessing.pool import ThreadPool
import requests
import time

links = ['https://github.com/timeline.json',
         'https://github.com/timeline.json',
         'https://github.com/timeline.json',
         'https://github.com/timeline.json',
         'https://github.com/timeline.json']


def get_html(link):
    print(requests.get(link).text)


t_start = time.time()
for i in range(len(links)):
    get_html(links[i])
t1 = (time.time() - t_start)

t_start = time.time()
with ThreadPool(processes=len(links)) as executor:
    executor.map(get_html, links)
t2 = (time.time() - t_start)

t_difference = t1 - t2

print(f'Время последовательного запуска: {t1} секунд')
print(f'Время параллельного запуска: {t2} секунд')
print(f'Разница во времени: {t_difference} секунд')
