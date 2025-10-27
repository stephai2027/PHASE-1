import numpy as np
import matplotlib.pyplot as plt

#Definissons l'axe temporel
t = np.linspace(0,20,1000)

#Definissons les trois tensions
V1 = 220*np.sqrt(2)*np.sin(2*50*np.pi*t)
V2 = 220*np.sqrt(2)*np.sin(2*50*np.pi*t - (2/3)*np.pi )
V3 = 220*np.sqrt(2)*np.sin(2*50*np.pi*t + (2/3)*np.pi)

#Mise en forme 
plt.xlabel("l'axe des temps")
plt.ylabel("l'axe des tensions")
plt.plot(t,V1,c = 'green',label = "V1")
plt.legend()
plt.plot(t,V2,c = 'red',label = "V2")
plt.legend()
plt.plot(t,V3,c = 'yellow',label = "V3")
plt.legend()
plt.title("L'évolution d'un système équilibré triphasé")

#Affichage
plt.grid()
plt.show()