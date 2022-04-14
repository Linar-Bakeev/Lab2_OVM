from __future__ import print_function
import psutil

vmem = psutil.virtual_memory()

total = vmem.total/1024/1024/1024
total = round(total, 2)

avail = vmem.available/1024/1024/1024
avail = round(avail, 2)

perc = vmem.percent
perc = round(perc, 2)

usedM = vmem.used/1024/1024/1024
usedM = round(usedM, 2)

free = vmem.free/1024/1024/1024
free = round(free, 2)

print("Всего памяти:", end=' ')
print(total, end=' ')
print("Гб")

print("Процент занятой памяти на данный момент:", end=' ')
print(perc, end='')
print("%")

print("Используемая память:", end=' ')
print(usedM, end=' ')
print("Гб")

print("Свободно:", end=' ')
print(free, end=' ')
print("Гб")