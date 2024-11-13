import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def sinplot(n=10):
    x=np.linspace(0,20,50)
    for i in range(1,n+1):
        plt.plot(x,np.sin(x+i*0.5)*(n+2-i))
sinplot()
plt.title("YOGITH.P-1KI23CS188-Aesthetic function")
sns.set_context("talk")
plt.show()