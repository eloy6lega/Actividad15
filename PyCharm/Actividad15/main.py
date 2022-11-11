import pandas as pd
import matplotlib.pyplot as plt

persona1 = [15, 'Pedro', 170]
persona2 = [17, 'María', 152]
persona3 = [13, 'Jorge', 166]
persona4 = [16, 'Carlos', 182]
persona5 = [18, 'Sandra', 159]

listapersonas = [persona1, persona2, persona3, persona4, persona5]

personas = pd.DataFrame(listapersonas,columns=['EDAD', 'NOMBRE', 'ALTURA EN CM'])

print(personas)

plt.plot(personas['NOMBRE'], personas['EDAD'])
plt.show()

plt.fill_between(personas['NOMBRE'], personas['EDAD'])
plt.show()

plt.scatter(personas['EDAD'], personas['ALTURA EN CM'])
plt.show()

plt.bar(personas['NOMBRE'], personas['ALTURA EN CM'])
plt.show()

plt.barh(personas['ALTURA EN CM'], personas['NOMBRE'])
plt.show()
