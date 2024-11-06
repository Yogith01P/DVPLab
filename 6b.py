import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[6,20,26,27,10,15,25,30,27,15,32,26,24,18,21,28,30,27,29,30]
plt.plot(overs,runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("over",color='black')
plt.ylabel("runs",color='red')
plt.title("YOGITH.P-1KI23CS188-Line formate")
plt.show()