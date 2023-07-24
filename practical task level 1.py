import time

names = ['Альфа', 'Бета', 'Гамма', 'Дельта', 'Эпсилон']

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


for i in range(len(names)):
    get_thread(names[i])
