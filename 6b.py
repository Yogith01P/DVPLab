import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
plt.plot(overs,runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("over",color='black')
plt.ylabel("runs",color='red')
plt.title("YOGITH.P-1KI23CS188-Line formate")
plt.show()
