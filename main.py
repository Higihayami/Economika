import warnings
from array import array
import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, cos, sin

#Ценовая дискриминация первой степени
print ("Ценовая дискриминация первой степени")
warnings.filterwarnings('ignore')
print("Введите цену 1")
p = int(input())
print("Введите цену 2")
p2 = int(input())
print("Введите количество товара 1")
q = int(input())
print("Введите количество товара 2")
q2 = int(input())
print("Введите надбавку")
a = int(input())
print("Введите количество потребителей")
n = int(input())
Tq = p*q+a
print("Двухставочный тариф равен ", Tq)



y = np.arange(p2, p)
x = np.arange(q, q2)

dotxy = (q2+1)/(q2/p+2)
dotyx  = q2-(q2/p)*dotxy
plt.plot(q2-(q2/p)*y, y, "black")
plt.plot(-1 + 2*y, y, "black")
plt.text(0,dotxy, "CS", fontsize = 13 )
plt.axhline(y=dotxy,color="black", linestyle="--")
plt.axvline(x=dotyx,color="black", linestyle="--")
plt.autoscale(enable = True, axis = 'x', tight= True)
plt.autoscale(enable = True, axis = 'y', tight= True)
plt.xlabel("q")
plt.ylabel("P")
plt.show()

osy = (q2+1)/(2+(q2/p))
osx = q2-(q2/p)*osy

s = ((p-osy)*(osx - q))/2
print("Излишки потребителя",s)

amax = s/n

print("Максимальная надбавка к стоимости", amax)

sw = ((osx - q) * (osy - p2))/2
pribyl = s + (abs(p-p2)*abs(q2-q)-sw)

print("Прибыль для производителя равна ", pribyl)
print("\n")

#Ценовая дискриминация второй степени

print("Ценовая дискриминация второй степени")
print("Введите цену 1 для категории 1")
popt1 = int(input())
print("Введите цену 2 для категории 1")
popt2 = int(input())

print("Введите количество товара 1 для категории 1")
proz1 = int(input())
print("Введите количество товара 2 для категории 1")
proz2 = int(input())

print("Введите цену 1 для категории 2")
qopt1 = int(input())
print("Введите цену 2 для категории 2")
qopt2 = int(input())

print("Введите количество товара 1 для категории 2")
qroz1 = int(input())
print("Введите количество товара 2 для категории 2")
qroz2 = int(input())

kopt = ((popt1 - popt2)/(qopt1-qopt2))
kroz = ((proz1 - proz2)/(qroz1-qroz2))

yopt = popt1 - kopt * qopt1
xopt = ((0-yopt)/kopt)

yroz = proz1 - kroz *qroz1
xroz = ((0-yroz)/kroz)

y = array('f',[yopt, 0.0])
y2 = array('f',[yroz, 0.0])
yos = array('i', [proz2, proz2])
x2 = array('f',[0.0, xroz])
x = array('f',[0.0, xopt])

q1 = array('i', [qroz1, qroz1])
q1y = array('i', [0, proz1])

q2 = array('i', [qroz2, qroz2])
q2y = array('i', [0, proz2])

plt.plot(x,y, color = "black")
plt.plot(x2,y2, color = "black")
plt.plot(x2, yos, color = "black")
plt.plot(q1, q1y,"--", color = "black")
plt.plot(q2, q2y,"--", color = "black")
plt.text(0, xroz, "A")
plt.text(qroz1, xroz, "E")
plt.text(qopt2, xroz, "C")
plt.text(0, proz1, "B")
plt.text(qroz1, 0, "q1")
plt.text(qroz2, 0, "q2")
plt.autoscale(enable = True, axis = 'x', tight= True)
plt.autoscale(enable = True, axis = 'y', tight= True)
#plt.plot(-1 + 2*y, y)
plt.show()

AB = yroz - proz2
AC = qroz2

STr = AB*AC/2

BE = proz1 - proz2
EC = qroz2 - qroz1

StrEc  = BE*EC/2

Ex = 110 - qroz1
Ey = qopt1 - proz2

SE = Ex * Ey / 2

SC = StrEc - SE

A = yopt - proz2

StrAE = A * proz2 / 2

SA = StrAE - SE

SB = STr - SA - SC - SE

print("Потребительский излишек ", SB)
print("величина потребительского излишка потребителей первой группы ", SA)
print(f"\n")


#Ценовая дискриминация третьей степени

print("Ценовая дискриминация третьей степени")
print("Введите цену 1 для категории 1")
p = int(input())
print("Введите цену 2 для категории 1")
p2 = int(input())

print("Введите количсетво товара 1 для категории 1")
q = int(input())
print("Введите количсетво товара 2 для категории 1")
q2 = int(input())

print("Введите цену 1 для категории 2")
price = int(input())
print("Введите цену 2 для категории 2")
price2 = int(input())

print("Введите количсетво товара 1 для категории 2")
quantity = int(input())
print("Введите количсетво товара 2 для категории 2")
quantity2 = int(input())

print("Введите надбавку")
a = int(input())

print("Введите количество потребителей")
n = int(input())
Tq = p*q+a
print("Двухставочный тариф равен ", Tq)

a = 1
b = 1
c = 1
parabx = np.linspace(0, 10, 1000)
paraby = a * parabx ** 2 + b * parabx + c


y = np.arange(p2, p)
x = np.arange(q, q2)
y2 = np.arange(price2, price)
x2 = np.arange(quantity, quantity2)
fig, ax = plt.subplots()


e = (p/q)*(p2/q2)
print("Эластичность спроса равна ",e)
proizv = (p*q)*(1+1/e)
print("Предельная выручка",proizv)


ax.plot(parabx, paraby, color = "black")
plt.plot(q2-(q2/p)*y, y,"--",  color = "black")
plt.plot(quantity2-(quantity2/price)*y2, y2, color = "black")
plt.plot(-1 + 2*y, y, color = "black")
plt.autoscale(enable = True, axis = 'x', tight= True)
plt.autoscale(enable = True, axis = 'y', tight= True)
plt.show()