# Tarea3: Variables aleatorias múltiples
## 1) A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Dado que se cuenta con un conjunto discreto de datos, la función de densidad marginal de cada variable aleatoria vendría dada por

<img src="https://render.githubusercontent.com/render/math?math=f_X(x)=\displaystyle\sum_{n=5}^25 P(x,y_n)"> y <img src="https://render.githubusercontent.com/render/math?math=f_Y(y)=\displaystyle\sum_{m=5}^15 P(x_m,y)">

Para visualizar qué forma tiene la distribución de los datos se hizo un gráfico de barras para cada conjunto marginal de X y Y.
De este gráfico se vio que ambos conjuntos de datos tienen la forma de una distribución normal, por lo que de estimó un modelo para cada VA al comparar mediante *curve_fit* del paquete *stats.optimize* los datos con la función que define la distribución normal, la cual es

<img src="https://render.githubusercontent.com/render/math?math=f_X(x)=\frac{1}{\sqrt{2 \pi \sigma^2}} \cdot e^{\left(\frac{-(x-\mu)^2}{2 \sigma^2}\right)}">

de lo que se obtuvo un valor de *mu* y *sigma* para cada distribución

-| X | Y 
----------|---|-----
Mu | 9,9048438 | 15,0794609
Sigma | 3,299442875 | 6,02693775

Por lo que el modelo que mejor se ajusta los valores de X sería

<img src="https://render.githubusercontent.com/render/math?math=f_X(x)=\frac{1}{\sqrt{2 \pi \cdot (3,299442875)^2}} \cdot e^{\left(\frac{-(x-9,9048438)^2}{2 \cdot (3,299442875)^2}\right)}">

y el modelo que mejor se ajusta a los valores de Y sería

<img src="https://render.githubusercontent.com/render/math?math=f_X(x)=\frac{1}{\sqrt{2 \pi \cdot (6,02693775)^2}} \cdot e^{\left(\frac{-(x-15,0794609)^2}{2 \cdot (6,02693775)^2}\right)}">

## 2) Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos?

Dado que las funciones marginales son independientes aplica la siguiente relación

<img src="https://render.githubusercontent.com/render/math?math=f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)">
