from random import random
import pylab
from math import log, exp

# початкові параметри
n = 10000; lmbd = 0.12
e = [random() for i in range(n)]
print('n =', n, 'lambda =', lmbd)

# згенеровані значення x
x = [0 for i in range(n)]
for i in range(n):
    x[i] = (-1 / lmbd) * log(e[i])

# поділ на інтервали
num_of_intervals = 20
interval_width = (max(x) - min(x)) / num_of_intervals
interval = [0 for i in range(num_of_intervals + 1)]
for i in range(len(interval)):
    interval[i] = min(x) + interval_width * i

print('\nПоділ на інтервали: кількість інтервалів =', num_of_intervals)

# кількість входжень xi до інтервалів
x_in_intervals = [0 for i in range(num_of_intervals)]
x.sort()
x[0] += 10 ** (-9)
for i in range(n):
    for j in range(num_of_intervals):
        if interval[j] < x[i] <= interval[j + 1]:
            x_in_intervals[j] += 1

print('Кількість входжень в і-й інтервал:', x_in_intervals)
print('Усього розподілено значень x:', sum(x_in_intervals))

# перевірка за критерієм хі квадрат
p_theory = [0 for i in range(num_of_intervals)]
for i in range(len(p_theory)):
    p_theory[i] = n * (exp(-lmbd * interval[i]) - exp(-lmbd * interval[i + 1]))

chi_square = sum([((x_in_intervals[i] - p_theory[i]) ** 2) / p_theory[i] for i in range(num_of_intervals)])
chi_square = 0
for i in range(num_of_intervals):
    chi_square += ((x_in_intervals[i] - p_theory[i]) ** 2) / p_theory[i]

# вивід результатів
print('\nТабличне значення критерію хі квадрат при рівні значимості α = 0.05 та кількості степенів свободи 19 = 31.14.')
print('Якщо розраховане значення буде меньше табличного, з довірчою ймовірністю 0,95 можна буде стверджувати,'
      '\nщо випадкова величина розподілена за заданим законом розподілу.')
print('\nРозреховане значення критерію хі квадрат = ', chi_square)

if chi_square < 31.14:
    print('Випадкова величина розподілена за експоненційним законом розподілу.')
else:
    print('Випадкова величина не розподілена за експоненційним законом розподілу.')

# гістограма розподілу
pylab.bar(interval[0:20], x_in_intervals, width=interval_width)
pylab.title('Гістограма розподілу величини x')
pylab.show()

