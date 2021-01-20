import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-50, 50)
ys = []
ys2 = []
ys3 = []
ys4 = []
ys5 = []
ys6 = []
ys7 = []
ys8 = []
ys9 = []
ys10 = []
ys11 = []
ys12 = []
for x in xs:
    y = 0.05*x**2 + 50
    y2 = 0.05*x**2 + 40
    y3 = 0.05*x**2 + 30
    y4 = 0.05*x**2 + 20
    y5 = 0.05*x**2 + 10
    y6 = 0.05*x**2
    y12 = -y6
    y7 = -y5
    y8 = -y4
    y9 = -y3
    y10 = -y2
    y11 = -y
    ys.append(y)
    ys2.append(y2)
    ys3.append(y3)
    ys4.append(y4)
    ys5.append(y5)
    ys6.append(y6)
    ys7.append(y7)
    ys8.append(y8)
    ys9.append(y9)
    ys10.append(y10)
    ys11.append(y11)
    ys12.append(y12)


plt.plot(xs, ys)
plt.plot(xs, ys2)
plt.plot(xs, ys3)
plt.plot(xs, ys4)
plt.plot(xs, ys5)
plt.plot(xs, ys6)
plt.plot(xs, ys7)
plt.plot(xs, ys8)
plt.plot(xs, ys9)
plt.plot(xs, ys10)
plt.plot(xs, ys11)
plt.plot(xs, ys12)

### vertical bends ###

ys = np.linspace(-50, 50)
xs = []
xs2 = []
xs3 = []
xs4 = []
xs5 = []
xs6 = []
xs7 = []
xs8 = []
xs9 = []
xs10 = []
xs11 = []
xs12 = []
for y in ys:
    x = 0.05*y**2 + 50
    x2 = 0.05*y**2 + 40
    x3 = 0.05*y**2 + 30
    x4 = 0.05*y**2 + 20
    x5 = 0.05*y**2 + 10
    x6 = 0.05*y**2 
    x7 = -x5
    x8 = -x4
    x9 = -x3
    x10 = -x2
    x11 = -x
    x12 = -x6
    xs.append(x)
    xs2.append(x2)
    xs3.append(x3)
    xs4.append(x4)
    xs5.append(x5)
    xs6.append(x6)
    xs7.append(x7)
    xs8.append(x8)
    xs9.append(x9)
    xs10.append(x10)
    xs11.append(x11)
    xs12.append(x12)


plt.plot(xs, ys)
plt.plot(xs2, ys)
plt.plot(xs3, ys)
plt.plot(xs4, ys)
plt.plot(xs5, ys)
plt.plot(xs6, ys)
plt.plot(xs7, ys)
plt.plot(xs8, ys)
plt.plot(xs9, ys)
plt.plot(xs10, ys)
plt.plot(xs11, ys)
plt.plot(xs12, ys)

plt.show()