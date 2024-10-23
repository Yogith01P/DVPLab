import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,20,7)
y1=x
print(y1)
y2=np.square(x)
print(y2)
y3=np.sqrt(x)
print(y3)
plt.plot(x,y1,'red',x,y2,'green',x,y3,'blue')
plt.legend(['x','square(x)','sqrt(x)'])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xticks(x)
plt.yticks(y2)
plt.title("Linear-YOGITH.P-1KI23CS188")
plt.show()