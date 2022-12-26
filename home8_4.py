"""
Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
"""
import logging
import time

def dec_log(func):
    def log():
        print("Start")
        func()
        logging.debug("A DEBUG Message")
        logging.info("An INFO")
        logging.warning("A WARNING")
        logging.error("An ERROR")
        logging.critical("A message of CRITICAL severity")  
        print("End")
    return log

def dec_time(func):
    def timefunc():
        print("Start")
        tic = time.perf_counter()
        func()
        toc = time.perf_counter()
        print(f"Время выполнения функции {toc - tic:0.4f} секунд")
        print("End")
    return timefunc

def dec_sleep(func):
    def timesleep():
        print("Start")
        tic = time.perf_counter()
        time.sleep(3)
        func()
        toc = time.perf_counter()
        print(f"Время выполнения функции {toc - tic:0.4f} секунд")
        print("End")
    return timesleep

def immutable_function ():
    print("You don't change me!")
    
print('Список декораторов: \n dec_log - логирование \n dec_time - время \n dec_sleep - задержка')

name = input('Введите декоратор: ')
if name == 'dec_log':
    immutable_function_decorated = dec_log(immutable_function)
    immutable_function_decorated()
elif name == 'dec_time':
    immutable_function_decorated = dec_time(immutable_function)
    immutable_function_decorated()
elif name == 'dec_sleep':
    immutable_function_decorated = dec_sleep(immutable_function)
    immutable_function_decorated()
else:
    print('Команда введена неверно')    