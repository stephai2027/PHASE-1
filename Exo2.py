import matplotlib.pyplot as plt
import numpy as np

#Définissons l'axe des abscisses
x = np.linspace(0,2*np.pi,30)

#Explicitons chaque fonction
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.tan(x)
y4 = np.log(x)
y5 = np.exp(x)
y6 = np.log10(x)
y7 = x
y8 = x**2
y9 = x**3 

#Mise en forme des sous-graphes
plt.subplot(3,3,1)
plt.plot(x,y1,label = 'cos(x)',c = 'k')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,2)
plt.plot(x,y2,label = 'sin(x)')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,3)
plt.plot(x,y3,label = 'tan(x)',c = 'pink')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,4)
plt.plot(x,y4,label = 'ln(x)',c = 'green')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,5)
plt.plot(x,y5,label = 'exp(x)', c = 'red')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,6)
plt.plot(x,y6,label = 'log10(x)', c = 'yellow')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,7)
plt.plot(x,y7,label = 'x', c = 'brown')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,8)
plt.plot(x,y8,label = 'x^2', c = 'purple')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

plt.subplot(3,3,9)
plt.plot(x,y9,label = 'x^3',c = 'orange')
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.legend()
plt.grid()

#Affichage
plt.show()
