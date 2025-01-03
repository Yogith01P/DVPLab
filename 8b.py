import numpy as np
from bokeh.io import output_file
from bokeh.io import show
from bokeh.layouts import row,column
from bokeh.plotting import figure
fig=figure(width=500,height=300,title='Different types of plots')
x=np.linspace(0,10,100)
y=np.sin(x)
fig.line(x,y,line_width=2,legend_label='line plot')
fig.vbar(x=x,top=y,legend_label='Bar chart',width=0.5,bottom=0)
fig.circle(x,y,size=5,color='red',legend_label='Scatter plot')
fig.xaxis.axis_label='X axis'
fig.yaxis.axis_label='Y axis'
fig.legend.location='top_left'
show(fig)