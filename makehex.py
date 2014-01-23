import sys
import numpy as np
import pdb
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import os

def makehex(width, widths, angles, ax = None):
	if ax is None:
		ax = plt.axes()

	pts = np.array([[0,0],[1,0],[(3./2),(np.sqrt(3)/2.0)],[1,np.sqrt(3)],
				[0,np.sqrt(3)],[(-1.0/2),np.sqrt(3.)/2],[0,0]])
	xaxis = np.array([[2,0],[2.5,0]])
	yaxis = np.array([[2.25,0.5],[2.25,-0.5]])
	
	height_norm = width/np.sqrt(3.0)
	pts = pts*height_norm

	#point for the pin
	circx = 2.5
	circy = 0.75

	x = pts[:,0]
	y = pts[:,1]
	
	w1x = [(0.5*(x[0]+x[1])),(0.5*(x[3]+x[4]))]
	w1y = [(0.5*(y[0]+y[1])),(0.5*(y[3]+y[4]))]
	w2x = [(0.5*(x[1]+x[2])),(0.5*(x[4]+x[5]))]
	w2y = [(0.5*(y[1]+y[2])),(0.5*(y[4]+y[5]))]
	w3x = [(0.5*(x[5]+x[0])),(0.5*(x[2]+x[3]))]
	w3y = [(0.5*(y[5]+y[0])),(0.5*(y[2]+y[3]))]
	
	#lines for  xycoordinate system
	x1,y1 = np.array([[x[2]+0.5,x[2]+0.9],[y[0]-0.2,y[0]-0.2]])
	x2,y2 = np.array([[x[2]+0.75,x[2]+0.75],[y[0],y[0]-0.4]])
	xline = mlines.Line2D(x1, y1, lw=1)
	yline = mlines.Line2D(x2, y2, lw=1)
	
	#point for the pin
	circx = x[2]+1
	circy = y[2]

	buffer = (x[2]-x[1])*3.0
	x_min = x[5]-buffer
	x_max = x[2]+buffer
	y_min = y[0]-(buffer/2.0)
	y_max = y[3]+(buffer/2.0)

	ax.plot(circx,circy, ' ok')
	ax.plot(x, y, color='black', linewidth=2)
	ax.plot(x1, y1, color='black', linewidth=1)
	ax.plot(x2, y2, color='black', linewidth=1)
	ax.plot(w1x,w1y,color='red')
	ax.plot(w2x,w2y,color='green')
	ax.plot(w3x,w3y,color='blue')
	
	ax.set_xlim(x_min, x_max)
	ax.set_ylim(y_min, y_max)
	ax.set_aspect(1)
	ax.locator_params(nbins=4)

	ha = ["right","left","left","left","right","right"]
	va = ["top","top","center","bottom","bottom","center"]
	xt=[x[0]-0.1,x[1]+0.1,x[2]+0.1,x[3]+0.1,x[4]-0.1,x[5]-0.1]
	yt=[y[0]-0.1,y[1]-0.1,y[2]+0.0,y[3]+0.1,y[4]+0.1,y[5]+0.0]
	bbox_props = dict(fc = "gainsboro", pad=3)
	
	for i in range(6):
		ax.annotate('%s deg' %(round(angles[i],2)), xy=(x[i],y[i]), xytext=(xt[i],yt[i]),
					bbox=bbox_props, ha=ha[i], va=va[i], size=14)
	
	color=['red', 'green', 'blue']
	wx = [w1x[0], w2x[0]+0.1, w3x[0]-0.1]
	wy = [w1y[0]-0.1, w2y[0], w3y[0]]
	ha = ['center', 'left', 'right']
	va = ['top', 'center', 'center']
	
	for i in range(3):
		ax.annotate('%s mm' % round(widths[i],3), xy=(wx[i],wy[i]), xytext=(wx[i],wy[i]),
					ha=ha[i], va=va[i], size=14, color=color[i])
	ax.annotate('X', xy=(x[2]+0.7,y[0]),size=14)
	ax.annotate('Y', xy=(x[2]+0.45,y[0]-0.2),size=14)
	
	return ax
