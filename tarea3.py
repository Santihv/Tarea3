'''
Tarea #3
IE0405: Modelos Probabilísticos de Señales y Sistemas
Santiago Hernández Vargas
B73737
'''

#Importar librerías necesarias
import numpy as np 
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv

with open('xy.csv') as datosxy:
  lectura = csv.reader(datosxy)
  next(lectura) #Salta la primera línea de encabezado
  datos = [i for i in lectura]
  
  '''
  1) A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.
  '''

  #Obtener cada fila de números
  probs = []
  for i in datos:
    del(i[0])
    lista = []
    for j in i:
      lista.append(float(j))
    probs.append(lista)
  #print(probs)

  #Obtener los valores marginales de cada variable
  xmarginal = np.sum(probs, axis=1)
  ymarginal = np.sum(probs, axis=0)
  #print('X: ', xmarginal)
  #print('Y: ', ymarginal)
  
  #Visualizar la distribución de X
  x = np.linspace(5,15,len(xmarginal))
  
  plt.bar(x, xmarginal, label='Datos X')
  plt.legend()
  plt.savefig('X.png')

  #Curva de ajuste X
  #Definir la función que genera la distribución normal
  def normal(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))

  #Obtener los parámetros de X
  paramx, _ = curve_fit(normal, x, xmarginal)
  mux, sigmax = paramx[0], paramx[1]
  print('Mux = ', mux, 'Sigmax = ', sigmax)

  #Obtener el modelo de fX(x)
  fX = stats.norm(mux,sigmax)
  x_modelo = np.linspace(fX.ppf(0.01), fX.ppf(0.99), 100)
  plt.plot(x_modelo,fX.pdf(x_modelo),label='fX(x)', color="tab:orange")
  plt.legend()
  plt.savefig('fX.png')


  #Visualizar la distribución de Y
  y = np.linspace(5,25,len(ymarginal))
  plt.cla()
  plt.bar(y, ymarginal, label='Datos Y')
  plt.legend()
  plt.savefig('Y.png')

  #Obtener los parámetros de Y
  paramy, _ = curve_fit(normal, y, ymarginal)
  muy, sigmay = paramy[0], paramy[1]
  print('Muy = ', muy, 'Sigmay = ', sigmay)  

  #Obtener el modelo de Y
  
  fY = stats.norm(muy,sigmay)
  y_modelo = np.linspace(fY.ppf(0.01), fY.ppf(0.99), 100)
  plt.plot(y_modelo,fY.pdf(y_modelo),label='fY(y)', color="tab:orange")
  plt.legend()
  plt.savefig('fY.png')


  '''
  2) Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos?
  '''
  
  fXx = normal(x_modelo,mux,sigmax)
  fYy = normal(y_modelo,muy,sigmay)
  
  def conjunta(x,y,mux,sigmax,muy,sigmay):
    return (1/(np.sqrt(2*np.pi*sigmax**2)) * np.exp(-(x-mux)**2/(2*sigmax**2))) * (1/(np.sqrt(2*np.pi*sigmay**2)) * np.exp(-(y-muy)**2/(2*sigmay**2)))

 


  '''
  3) Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.
  '''
  '''
  #Evaluando con el modelo en todo su dominio
  xx = np.linspace(5,15,100)
  yy = np.linspace(5,25,100)
  correlación = 0
  f = 0
  for m in xx:
    c = 0
    for n in yy:
      correlación += m*n*fXY[f][c]
      c += 1
    f += 1
  print('Correlación modelo = ',correlación)
  '''
  
  #Evaluando con el modelo en valores "discretos"
  fx = normal(x,mux,sigmax)
  fy = normal(y,muy,sigmay)

  fxy = []
  for i in fx:
    fila = []
    for j in fy:
      fila.append(i*j)
    fxy.append(fila)

  correlación_discreta = 0
  f = 0
  for m in x:
    c = 0
    for n in y:
      correlación_discreta += m*n*fxy[f][c]
      c += 1
    f += 1
  print('Correlación modelo = ',correlación_discreta)
  
  #Evaluando con los datos discretos
  cor = 0
  f = 0
  for m in x:
    c = 0
    for n in y:
      cor += m*n*probs[f][c]
      c += 1
    f += 1
  print('Correlación datos = ',cor)

  #No correlación
  RXY = fX.stats(moments='m')*fY.stats(moments='m')
  print('RXY = ',RXY)

  #Covarianza Cxy
  covarianza = cor - fX.stats(moments='m')*fY.stats(moments='m')
  print('Covarianza = ', covarianza)

  #Coeficiente de correlación Ro
  coef_corre = covarianza/(sigmax*sigmay)
  print('Coeficiente de correlación: Ro = ',coef_corre)

  '''
  4) Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
  '''
  '''
  #Los gráficos de fX y fY ya fueron generados en el inciso 1)
  
  fXY = []
  for i in fXx:
    fila = []
    for j in fYy:
      fila.append(i*j)
    fXY.append(fila)
  #print('Con el modelo: ',fXY)
  

  plt.cla()
  fig = plt.figure()
  ax = plt.axes(projection="3d")
  #X = normal(x_modelo,mux,sigmax)
  #Y = normal(y_modelo,muy,sigmay)
  X,Y = np.meshgrid(x_modelo,y_modelo)
  #Z = conjunta(x_modelo,y_modelo,mux,sigmax,muy,sigmay)
  ax.plot_surface(X,Y,np.array(fXY),cmap="viridis")
  plt.show()
  '''