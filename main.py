from __future__ import print_function
import psutil

import wmi

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])


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


print('Название ОС: {0}'.format(os_name))
print('Версия: {0}'.format(os_version))
print('ЦП: {0}'.format(proc_info.Name))
print('Видеокарта/Графический чип: {0}'.format(gpu_info.Name))

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