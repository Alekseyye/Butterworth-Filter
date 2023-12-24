from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Характеристики фильтра
wc = 15  # частота среза, Гц
N = 3  # порядок фильтра
type = 'low'  # тип фильтра (низкие ('low') или высокие ('high') частоты)

# вычисление коэффициентов фильтра
b, a = signal.butter(N, wc, type, analog = True)

# получение и построение АЧХ фильтра
w, h = signal.freqs(b, a)  # получение функции h(w) для фильтра
plt.semilogx(w, 20 * np.log10(abs(h))) # график с логарифмическим масштабированием по оси абсцисс

if type == 'low':
    plt.title('АЧХ ФНЧ Баттерворта')   # название графика
else:
    plt.title('АЧХ ФВЧ Баттерворта')
    
plt.xlabel('Частота, рад/с')           # названия осей на графике
plt.ylabel('Понижение амплитуды, дБ')

plt.margins(0, 0.1)  # создание отступов от границ графика
plt.grid(True)  #добавление сетки
plt.axvline(wc, color = 'red') # добавление частоты среза на график
plt.show()

# характеристики исходного сигнала
t0 = 1  # длительность сигнала

w1 = 10  # частоты исходного сигнала
w2 = 20

f = 1000 # частота дискретизации

# исходный сигнал
t = np.linspace(0, t0, t0 * f)  # равномерный массив моментов времени t
sig = np.sin(2 * np.pi * w1 * t) + np.sin(2 * np.pi * w2 * t)

# фильтрация сигнала
sos = signal.butter(N, wc, type, fs = f, output = 'sos') # создание фильтра Баттерворта
filtsig = signal.sosfilt(sos, sig)

# графическое отображение исходного и фильтрованного сигнала
fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)

ax1.plot(t, sig)  # задание графика sig(t)
ax1.set_title('Исходный сигнал')  # название графика
ax1.axis([0, t0, -2, 2])  # установление пределов осей абсцисс и ординат
#ax1.set_xlabel('Время, с')
ax1.grid(True)

ax2.plot(t, filtsig)
ax2.set_title('Фильтрованный сигнал')
ax2.axis([0, t0, -2, 2])
ax2.set_xlabel('Время, с')
ax2.grid(True)

plt.tight_layout()
plt.show()