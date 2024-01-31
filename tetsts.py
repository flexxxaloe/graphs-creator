import matplotlib.pyplot as plt

# Ваши данные
x = [1, 10, 50, 100, 150, 200, 250]
x2 = [1, 10, 20, 30, 50, 75, 100]


#08k
v = [0.019, 0.18, 0.897, 1.823, 2.716, 3.709, 4.548]
y = [0.008, 0.085, 0.408, 0.789, 1.192, 1.625, 2.036]
z = [0.02, 0.18, 0.912, 1.871, 2.799, 3.721, 4.581]


#1k
r = [0.044, 0.452, 2.283, 4.535, 6.795, 9.114, 11.127]
fg = [0.019, 0.192, 0.988, 2.032, 3.062, 3.93, 5.057]
tg = [0.046, 0.446, 2.257, 4.501, 6.884, 9.036, 11.255]

#4k
qw = [0.412, 4.105, 8.281, 12.335, 20.238, 30.44, 40.978]
ars = [0.184, 1.799, 3.54, 5.396, 8.815, 13.6, 18.293]
vc = [0.436, 4.4, 8.487, 12.726, 21.317, 32.055, 42.843]


#16k
eee = [1.185, 11.816, 23.92, 36.221, 58.522, 88.698, 119.274]
qqq = [0.508, 5.188, 10.443, 15.774, 26.295, 38.786, 52.524]
www = [1.167, 11.928, 23.781, 36.559, 60.466, 89.704, 119.314]


#brightness
x3 = [-255, -200, -111,  0, 111, 200,255]
default = [0, 2.730004, 21.708843, 49.849869, 40.997044, 18.447075, 0.822017]
simple = [0, 2.732445, 21.730598, 49.930443, 41.062611, 18.457220, 0.823380]

#16k pic
def16 = [0, 3.108976, 8.796325, 17.811277, 30.280937, 44.939838, 42.075085, 50.010990, 75.674454]
sim16 = [0, 3.113942, 8.796648, 17.813457, 30.296768, 44.956276, 42.135864, 50.093170, 75.744827]


plt.plot(x3, default,  label='Abweichung der Helligkeit 800 default Version')
plt.plot(x3, simple, linestyle='--',label='Abweichung der Helligkeit 800 simple Version')

# create graph
'''plt.plot(x, v, label='standart 800')
plt.plot(x, y, label='simple 800')
plt.plot(x, z, label='simd 800')

plt.plot(x, r, label='standart 1k')
plt.plot(x, fg, label='simple 1k')
plt.plot(x, tg, label='simd 1k')

plt.plot(x, qw, label='standart 4k')
plt.plot(x, ars, label='simple 4k')
plt.plot(x, vc, label='simd 4k')

plt.plot(x, eee, label='standart 16k')
plt.plot(x, qqq, label='simple 16k')
plt.plot(x, www, label='simd 16k')'''

# label
plt.xlabel('Helligkeit')
plt.ylabel('Abweichungswert')
plt.title('')
plt.legend()

#save graph
plt.savefig('pic.png')
# show graph
plt.show()

