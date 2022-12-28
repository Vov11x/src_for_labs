from numpy import sin, cos, transpose, linalg, matmul
import pylab

# табличні дані спостережень
xdata = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8,
         3.2, 3.6, 4, 4.4, 4.8, 5.2, 5.6, 6]
ydata = [1.79, 2.005, 2.225, 2.41, 2.526, 2.553, 2.489, 2.349,
         2.161, 1.954, 1.74, 1.603, 1.504, 1.478, 1.531, 1.661]
print('Табличні дані:\nX:', xdata, '\nY:', ydata)


# функція залежності y від x, b
def y_of_x_and_b(x, b):
    y = b[0]
    for i in range(1, int(len(b) / 2)):
        y += b[2 * i - 1] * sin(x) ** i + b[2 * i] * cos(x) ** i
    return y


# функція fi від xj
def f_of_x(x, i, j):
    if j % 2 == 1:
        xi = sin(x) ** i
    else:
        xi = cos(x) ** i

    return xi


# функція для побудови матриці X, перший стовбець якої складається з одиниць, а інші елементи Xij дорівнюють
# значенням функції fi від xj
def find_matrix_x(n):
    X = [[1 for i in range(n + 1)] for j in range(len(xdata))]

    for i in range(1, n + 1):
        for j in range(len(xdata)):
            X[j][i] = f_of_x(xdata[j], i, j)

    return X


# функція для пошуку набору коефіцієнтів b з n bi
# b = (Xt * X) ** (-1) * Xt * y
def find_b(n):
    X = find_matrix_x(n)
    X_t = transpose(X)
    invert = linalg.inv(matmul(X_t, X))
    b = matmul(matmul(invert, X_t), ydata)
    return b


# вибір найкращого набору коефіцієнтів b методом найменших квадратів
found_b = []
list_squares_criterion = 10000
for n in range(50):
    bn = find_b(n)
    y_of_b = 0
    for i in range(len(xdata)):
        y_of_b += (y_of_x_and_b(xdata[i], bn) - ydata[i]) ** 2

    if y_of_b < list_squares_criterion:
        list_squares_criterion = y_of_b
        found_b = bn
        
print('\nЗначення критерію найменших квадратів =', list_squares_criterion)
print('Найкращий набір коефіцієнтів b:', found_b)

# Альтернативний варіант
'''print('\nАльтернативний варіант. Результати для кількості bn = 5:')
found_b = find_b(6)
list_squares_criterion = 0
for i in range(len(xdata)):
    list_squares_criterion += (y_of_x_and_b(xdata[i], found_b) - ydata[i]) ** 2
print('Значення критерію найменших квадратів =', list_squares_criterion)
print('Набір коефіцієнтів b:', found_b)'''


y = [0 for i in range(len(xdata))]
for i in range(len(xdata)):
    y[i] = round(y_of_x_and_b(xdata[i], found_b), 3)
print('\nЗначення Y при знайдених коефіцієнтах b:')
print(y)

pylab.plot(xdata, ydata, label='Table data', color='blue')
pylab.plot(xdata, y, label='Found data', color='red')
pylab.legend()
pylab.show()
