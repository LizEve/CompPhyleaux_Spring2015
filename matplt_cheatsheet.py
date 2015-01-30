##NOTES
"""
http://matplotlib.org/users/pyplot_tutorial.html


plt.plot([x-data],[y-data],'color options')
color options:
	b- = blue line, default
	ro = red circles

axis() takes a list of [xmin, xmax, ymin, ymax] 

"""

##Quick plots

def simple_dot_plot(xnums, ynums, xlabel, ylabel, data_label):
    plt.plot(xnums, ynums, 'ro',label=data_label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()