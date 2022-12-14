# Se utiliza para hacer gráficos en python: https://matplotlib.org/
# Para instalarlo pip install matplotlib

# Otros módulos externos para Python
# -Peticiones Http: https://requests.readthedocs.io/en/latest/
# -Interfaz gráfica python: https://www.wxpython.org/
# -Bases de datos SQL: https://www.sqlalchemy.org/
# -Biblioteca de algoritmos matematicos y datos cientificos: https://scipy.org/
# - Pygame para crear juegos en python
# - scikit-learn para marching learning: https://scikit-learn.org/stable/

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1500,1200,1100,1800]
legend = ["January","February","March","April"]

plt.xticks(x,legend) # Para poner la leyenda
plt.plot(x,y)
plt.show() #Mostrar el gráfico

plt.bar(x,y)
plt.ylabel("Sales in US$")
plt.title("Monthly sales")
plt.show()