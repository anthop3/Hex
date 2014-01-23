import sys
import numpy as num
import pdb
import pylab as py
import math
import matplotlib.pyplot as py
import matplotlib.image as mpimg
import os
import makehex as makehex
import hexinfo as hex
import Image, ImageDraw, ImageFont

#=================================Functions====================================
def concentricity(ccx,ccy,cax,cay):

    result = (((ccx-cax)**2)+((ccy-cay))**2)**0.5
    return result

def hexline(hlx1,hlx2,hly1,hly2):

    result = (hly1-hly2)/(hlx1-hlx2)
    return result

def pinline(plx1,plx2,ply1,ply2):

    result = (ply1-ply2)/(plx1-plx2)
    return result

def rotation(hl_slope,pl_slope):

    sub = hl_slope-pl_slope
    mul = hl_slope*pl_slope
    result = math.atan(abs(sub/(1.0+mul)))
    return result

def distance(distx1,distx2,disty1,disty2):

    xlen = distx1 - distx2
    ylen = disty1 - disty2
    result = ((xlen**2)+(ylen**2))**(0.5)
    return result

#===========================Error Prop Functions===============================

def econc(eccx,ecax,eccy,ecay,ccx,ccy,cax,cay):
    e1 = (((eccx)**2)+((ecax)**2))**0.5
    e2 = (((eccy)**2)+((ecay)**2))**0.5
    ne1 = (((ccx-cax)**2)*2*e1)/(ccx-cax)
    ne2 = (((ccy-cay)**2)*2*e2)/(ccy-cay)
    e3 = (((ne1)**2)+((ne2)**2))**0.5
    ne3 = (((ccx-cax)**2)+((ccy-cay)**2))
    result = ((ne3**0.5)*0.5*e3)/(ne3)
    return result

def ehl(ehlx1,ehlx2,ehly1,ehly2,hlx1,hlx2,hly1,hly2):
    e1 = (((ehlx1)**2)+((ehlx2)**2))**0.5
    e2 = (((ehly1)**2)+((ehly2)**2))**0.5
    ne1 = (hlx1-hlx2)
    ne2 = (hly1-hly2)
    result = (((e1/ne1)**2)+((e2/ne2)**2))**0.5
    return result

def epl(eplx1,eplx2,eply1,eply2,plx1,plx2,ply1,ply2):
    e1 = (((eplx1)**2)+((eplx2)**2))**0.5
    e2 = (((eply1)**2)+((eply2)**2))**0.5
    ne1 = (plx1-plx2)
    ne2 = (ply1-ply2)
    result = (((e1/ne1)**2)+((e2/ne2)**2))**0.5
    return result

def erot(ehl,epl,hl_slope,pl_slope):
    e1 = (((ehl)**2)+((epl)**2))**0.5
    ne1 = hl_slope-pl_slope
    ne2 = hl_slope*pl_slope
    e2 = ne2*(((ehl/hl_slope)**2)+((epl/pl_slope)**2))**0.5
    ne3 = abs(ne1)/(1+ne2)
    e3 = ne3*(((e1)**2)+((e2)**2))**0.5
    result = e3*(1/(1+ne3**2))
    return result

def edist(edistx1,edistx2,edisty1,edisty2,distx1,distx2,disty1,disty2):
    e1 = (((edistx1)**2)+((edistx2)**2))**0.5
    e2 = (((edisty1)**2)+((edisty2)**2))**0.5
    ne1 = (((distx1-distx2)**2)*2*e1)/(distx1-distx2)
    ne2 = (((disty1-disty2)**2)*2*e2)/(disty1-disty2)
    e3 = (((ne1)**2)+((ne2)**2))**0.5
    ne3 = (((distx1-distx2)**2)+((disty1-disty2)**2))
    result = ((ne3**0.5)*0.5*e3)/(ne3)
    return result

def ehh(ezhex,ezbase):
    result = (((ezhex)**2)+((ezbase)**2))**0.5
    return result

def eph(ezpin,ezbase):
    result = (((ezpin)**2)+((ezbase)**2))**0.5
    return result

#==============================Reading the Data================================

SN = str(raw_input('serial number'))
filename = 'SmartScopefiles/NEW/' + SN + '.txt'
fibernumber = int(raw_input('fibernumber'))

if fibernumber == 7:
    hexList7 = [hex.Hex7(filename)]
    all7 = hex.Superhex(hexList7)
    
    angles = all7.get_meas(['angle'])
    widths = all7.get_meas(['width'])
    dist = all7.get_meas(['dist'])
    dia = all7.get_meas(['diameter'])
    coords = all7.get_meas(['coords'])
    hex_cent = all7.get_meas(['hex_cent'])
    xyangles = all7.get_meas(['xyangles'])
    xypin = all7.get_meas(['xypin'])
    zpin = all7.get_meas(['zpin'])
    zbase = all7.get_meas(['zbase'])
    zhex = all7.get_meas(['zhex'])
    xangles = all7.get_meas(['xangles'])
    yangles = all7.get_meas(['yangles'])

    w_nom = 0.418
    
if fibernumber == 19:
    hexList19 =[hex.Hex19(filename)]
    all19 = hex.Superhex(hexList19)

    angles = all19.get_meas(['angle'])
    widths = all19.get_meas(['width'])
    dist = all19.get_meas(['dist'])
    dia = all19.get_meas(['diameter'])
    coords = all19.get_meas(['coords'])
    hex_cent = all19.get_meas(['hex_cent'])
    xyangles = all19.get_meas(['xyangles'])
    xypin = all19.get_meas(['xypin'])
    zpin = all19.get_meas(['zpin'])
    zbase = all19.get_meas(['zbase'])
    zhex = all19.get_meas(['zhex'])
    xangles = all19.get_meas(['xangles'])
    yangles = all19.get_meas(['yangles'])
    
    w_nom = 0.683

if fibernumber == 37:
    hexList37 =[hex.Hex37(filename)]
    all37 = hex.Superhex(hexList37)

    angles = all37.get_meas(['angle'])
    widths = all37.get_meas(['width'])
    dist = all37.get_meas(['dist'])
    dia = all37.get_meas(['diameter'])
    coords = all37.get_meas(['coords'])
    hex_cent = all37.get_meas(['hex_cent'])
    xyangles = all37.get_meas(['xyangles'])
    xypin = all37.get_meas(['xypin'])
    zpin = all37.get_meas(['zpin'])
    zbase = all37.get_meas(['zbase'])
    zhex = all37.get_meas(['zhex'])
    xangles = all37.get_meas(['xangles'])
    yangles = all37.get_meas(['yangles'])
    
    w_nom = 0.943
       
if fibernumber == 61:
    hexList61 =[hex.Hex61(filename)]
    all61 = hex.Superhex(hexList61)

    angles = all61.get_meas(['angle'])
    widths = all61.get_meas(['width'])
    dist = all61.get_meas(['dist'])
    dia = all61.get_meas(['diameter'])
    coords = all61.get_meas(['coords'])
    hex_cent = all61.get_meas(['hex_cent'])
    xyangles = all61.get_meas(['xyangles'])
    xypin = all61.get_meas(['xypin'])
    zpin = all61.get_meas(['zpin'])
    zbase = all61.get_meas(['zbase'])
    zhex = all61.get_meas(['zhex'])
    xangles = all61.get_meas(['xangles'])
    yangles = all61.get_meas(['yangles'])
    
    w_nom = 1.219

if fibernumber == 91:
    hexList91 = [hex.Hex91(filename)]
    all91 = hex.Superhex(hexList91)

    angles = all91.get_meas(['angle'])
    widths = all91.get_meas(['width'])
    dist = all91.get_meas(['dist'])
    dia = all91.get_meas(['diameter'])
    coords = all91.get_meas(['coords'])
    hex_cent = all91.get_meas(['hex_cent'])
    xyangles = all91.get_meas(['xyangles'])
    xypin = all91.get_meas(['xypin'])
    zpin = all91.get_meas(['zpin'])
    zbase = all91.get_meas(['zbase'])
    zhex = all91.get_meas(['zhex'])
    xangles = all91.get_meas(['xangles'])
    yangles = all91.get_meas(['yangles'])

    w_nom = 1.476
    
if fibernumber == 127:
    hexList127 = [hex.Hex127(filename)]
    all127 = hex.Superhex(hexList127)
    
    angles = all127.get_meas(['angle'])
    widths = all127.get_meas(['width'])
    dist = all127.get_meas(['dist'])
    dia = all127.get_meas(['diameter'])
    coords = all127.get_meas(['coords'])
    hex_cent = all127.get_meas(['hex_cent'])
    xyangles = all127.get_meas(['xyangles'])
    xypin = all127.get_meas(['xypin'])
    zpin = all127.get_meas(['zpin'])
    zbase = all127.get_meas(['zbase'])
    zhex = all127.get_meas(['zhex'])
    xangles = all127.get_meas(['xangles'])
    yangles = all127.get_meas(['yangles'])
    
    w_nom = 1.745

#=================================Nominals=====================================

a_nom = 120.0
hex_height_nom = 3.632
pin_height_nom = 1.650
OD_nom = 2.7508
PD_nom = 2.75

#================================Finding the Values============================

angle_avgs = num.array([num.mean(angles[0,:,i]) for i in range(6)])
angle_stds = num.array([num.std(angles[0,:,i]) for i in range(6)])
width_avgs = num.array([num.mean(widths[0,:,i]) for i in range(3)])
width_stds = num.array([num.std(widths[0,:,i]) for i in range(3)])
dist_avgs = num.array([num.mean(dist[0,:,i]) for i in range(4)])
dist_stds = num.array([num.std(dist[0,:,i]) for i in range(4)])
dia_avg = num.mean(dia)
dia_std = num.std(dia)
coords_avgs = num.array([num.mean(coords[0,:,i]) for i in range(6)])
coords_stds = num.array([num.std(coords[0,:,i]) for i in range(6)])
c_x = num.array([(coords_avgs[0],coords_avgs[1],coords_avgs[3])])
c_x_avg = num.mean(c_x)
c_x_std = num.std(c_x)
c_y = num.array([(coords_avgs[3],coords_avgs[4],coords_avgs[5])])
c_y_avg = num.mean(c_y)
c_y_std = num.std(c_y)
coords_avgs = num.array([(c_x_avg,c_y_avg)])
coords_stds = num.array([(c_x_std,c_y_std)])
hex_cent_avgs = num.array([num.mean(hex_cent[0,:,i]) for i in range(2)])
hex_cent_stds = num.array([num.std(hex_cent[0,:,i]) for i in range(2)])
xyangles_avgs = num.array([num.mean(xyangles[0,:,i]) for i in range(4)])
xyangles_stds = num.array([num.std(xyangles[0,:,i]) for i in range(4)])
xypin_avgs = num.array([num.mean(xypin[0,:,i]) for i in range(2)])
xypin_stds = num.array([num.std(xypin[0,:,i]) for i in range(2)])
zpin_avg = num.mean(zpin)
zpin_std = num.std(zpin)
zbase_avg = num.mean(zbase)
zbase_std = num.std(zbase)
zhex_avg = num.mean(zhex)
zhex_std = num.std(zhex)
xa_avg = num.mean(xangles)
xa_stds = num.array([num.std(xangles[0,:,i]) for i in range(6)])
xa_std = num.std(xa_stds)
ya_avg = num.mean(yangles)
ya_stds = num.array([num.std(yangles[0,:,i]) for i in range(6)])
ya_std = num.std(ya_stds)

angle_diffs = angle_avgs - a_nom
width_diffs = width_avgs - w_nom

#========================defining values for Functions=========================

ccx = hex_cent_avgs[0]
ccy = hex_cent_avgs[1]
cax = xa_avg
cay = ya_avg

hlx1 = xyangles_avgs[0]
hlx2 = xyangles_avgs[1]
hly1 = xyangles_avgs[2]
hly2 = xyangles_avgs[3]

plx1 = hex_cent_avgs[0]
plx2 = xypin_avgs[0]
ply1 = hex_cent_avgs[1]
ply2 = xypin_avgs[1]

center_error = hex_cent_avgs - coords_avgs
conc = concentricity(ccx,ccy,cax,cay)
hl_slope = hexline(hlx1,hlx2,hly1,hly2)
pl_slope = pinline(plx1,plx2,ply1,ply2)
rotation = rotation(hl_slope,pl_slope)
theta = math.degrees(rotation)

cex = hex_cent_avgs[0]-xa_avg
cey = hex_cent_avgs[1]-ya_avg

distx1 = dist_avgs[0]
distx2 = dist_avgs[1]
disty1 = dist_avgs[2]
disty2 = dist_avgs[3]
dist1 = distance(distx1,distx2,disty1,disty2)
PD_error = dist1 - PD_nom

dia1 = dia_avg
dia_error = dia1 - OD_nom

#finding height errors
hex_height = zhex_avg - zbase_avg
hex_height_err = hex_height - hex_height_nom
pin_height = zpin_avg - zbase_avg
pin_height_err = pin_height - pin_height_nom

#==============================Error Prop======================================
# Defineing Error values

eccx = hex_cent_stds[0]
eccy = hex_cent_stds[1]
ecax = xa_std
ecay = ya_std
ehlx1 = xyangles_stds[0]
ehlx2 = xyangles_stds[1]
ehly1 = xyangles_stds[2]
ehly2 = xyangles_stds[3]
eplx1 = hex_cent_stds[0]
eplx2 = xypin_stds[0]
eply1 = hex_cent_stds[1]
eply2 = xypin_stds[1]
edistx1 = dist_stds[0]
edistx2 = dist_stds[1]
edisty1 = dist_stds[2]
edisty2 = dist_stds[3]
ezhex = zhex_std
ezpin = zpin_std
ezbase = zbase_std

# Values with no prop. needed

w_err = width_stds  # Standard Deviation of Widths
a_err = angle_stds  # Standard Deviation of Angles
dia_err = dia_std  # Standard Deviation of OD

# Needs Error Prop.

# Center Error
ecex = (((eccx)**2)+((ecax)**2)**0.5)
ecey = (((eccy)**2)+((ecay)**2)**0.5)
econc = econc(eccx,ecax,eccy,ecay,ccx,ccy,cax,cay)

# Rotation Error Prop.
epl = epl(eplx1,eplx2,eply1,eply2,plx1,plx2,ply1,ply2)
ehl = ehl(ehlx1,ehlx2,ehly1,ehly2,hlx1,hlx2,hly1,hly2)
erot = erot(ehl,epl,hl_slope,pl_slope)
erot = math.degrees(erot)

# Distnace Error Prop.
edist = edist(edistx1,edistx2,edisty1,edisty2,distx1,distx2,disty1,disty2)

# Height Error Prop.
ehh = ehh(ezhex,ezbase)
eph = eph(ezpin,ezbase)

#============================Making the Hex Image==============================
py.figure(2)
ax = makehex.makehex(w_nom, width_diffs, angle_diffs)
#ax.set_title(SN + 'Hex: W = %s mm' % w_nom, size=14)
#py.xlim([-1,2])
#py.ylim([-0.5,1])
py.axis('off')
py.savefig(SN + '.png', dpi=400)
Image.open(SN + '.png').save(SN + '.jpg','JPEG',quality=95)


#=============================Plotting the JPG=================================

#============================Setting the variables=============================

conc2 = str(round(conc,5))
cex2 = str(round(cex,5))
cey2 = str(round(cey,5))
dist2 = str(round(dist1,5))
dia2 = str(round(dia1,5))
diae = str(round(dia_error,5))
theta2 = str(round(theta,5))
phe = str(round(pin_height_err,5))
hhe = str(round(hex_height_err,5))
edia = str(round(dia_err,5))
ecex = str(round(ecex,5))
ecey = str(round(ecey,5))
econc = str(round(econc,5))
erot = str(round(erot,5))
edist = str(round(edist,5))
ehh = str(round(ehh,5))
eph = str(round(eph,5))
PD_error = str(round(PD_error,5))

#=============================Making the Data File=============================

f = open('Output/' + SN + 'data.txt', 'w+')

f.write('Serial_Number\tComments\tAngle_1_Err\tAngle_1_Std\tAngle_2_Err\tAngle_2_Std\tAngle_3_Err\tAngle_3_Std\tAngle_4_Err\tAngle_4_Std\tAngle_5_Err\tAngle_5_Std\tAngle_6_Err\tAngle_6_Std\tWidth_1_Err\tWidth_1_Std\tWidth_2_Err\tWidth_2_Std\tWidth_3_Err\tWidth_3_Std\tOD\tOD_Err\tOD_Std\tPin_Distance\tPin_Distnace_Std\tConcentricity\tConc._Std\tConc._X_Err\tConc._X_Std\tConc._Y_Err\tConc._Y_Std\tRotation_Err\tRotation_Std\tHex_Height_Err\tHex_Height_Std\tPin_Height_Err\tPin_Height_Std\n')
f.write('%s\t\t%i\t\t%.5f\t\t%.5f\t\t%.5f\t%.5f\t\t%.5f\t%.5f\t\t%.5f\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\t\t%s\t%s\t%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t%s\t\t%s\t\t%s\t\t%s\t%s\t%s\t%s\t\t%s\t%s\n'%(SN,fibernumber,angle_diffs[0],a_err[0],angle_diffs[1],a_err[1],angle_diffs[2],a_err[2],angle_diffs[3],a_err[3],angle_diffs[4],a_err[4],angle_diffs[5],a_err[5],width_diffs[0],w_err[0],width_diffs[1],w_err[1],width_diffs[2],w_err[2],dia2,diae,edia,dist2,edist,conc2,econc,cex2,ecex,cey2,ecey,theta2,erot,hhe,ehh,phe,eph))
f.close()


#==============================TABLE===========================================
table_vals1=[['Serial Number',SN,'','OD',dia2,edia],['Comments',fibernumber,'','OD Err',dia_error,dia_err],['Angle 1',angle_diffs[0],a_err[0],'Pin Dist',dist2,edist],['Angle 2',angle_diffs[1],a_err[1],'Pin Dist Err',PD_error,''],['Angle 3',angle_diffs[2],a_err[2],'Conc',conc2,econc],['Angle 4',angle_diffs[3],a_err[3],'Conc X',cex2,ecex],['Angle 5',angle_diffs[4],a_err[4],'Conc Y',cey2,ecey],['Angle 6',angle_diffs[5],a_err[5],'Rot Err',theta2,erot],['Width 1',width_diffs[0],w_err[0],'Hex Height Err',hhe,ehh],['Width 2',width_diffs[1],w_err[1],'Pin Height Err',phe,eph],['Width 3',width_diffs[2],w_err[2],'','','']]

#==============================plotting data===================================

py.subplot(121)
py.annotate('SN:' + SN , xy=(0,.6),xycoords='data')
py.annotate('Concentricity: ' + conc2, xy=(0,.54),xycoords='data')
py.annotate('     X, Y error: ' + cex2 +' , ' + cey2, xy=(0,.48),xycoords='data')
py.annotate('     Rotation error: ' + theta2, xy=(0,.42),xycoords='data')
py.annotate('Pin Distance: ' + dist2, xy=(0,.36),xycoords='data')
py.annotate('Outer Diameter: ' + dia2, xy=(0,.3),xycoords='data')
py.ylim(0,1)
py.axis('off')
#py.axis('scaled')

py.subplot(122)
img=mpimg.imread(SN + '.jpg')
imgplot = py.imshow(img, origin='upper')
py.axis('off')

py.savefig(SN + 'data.png', dpi = 400)
Image.open(SN + 'data.png').save(SN + 'data.jpg','JPEG',quality=95)

os.system('rm ' + SN + '.png')
os.system('rm ' + SN + '.jpg')

py.figure(3,figsize=(5,6))
img=mpimg.imread(SN + 'data.jpg')
imgplot = py.imshow(img, origin='upper')
the_table = py.table(cellText=table_vals1)
py.axis('off')
py.savefig(SN + '.png', dpi = 400)
Image.open(SN + '.png').save('JPEG/' + SN + '.jpg','JPEG',quality=95)

os.system('rm ' + SN +'.png')
os.system('rm ' + SN + 'data.png')
os.system('rm ' + SN + 'data.jpg')
#===========================================================================

