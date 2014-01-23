import numpy as num

class Hex(object):
    '''
    class that houses ferrule data that is unspecific of hex size
    '''
    def __init__(self, width=None, angle=None, xyangles=None, diameter=None, dist=None, hex_cent=None, xypin=None, zpin=None, zbase=None, zhex=None, xangles=None, yangles=None,
    			 **nom_dict):
        self.nom_diameter = nom_dict.get('nom_diameter', 2.819)
        self.nom_angle = nom_dict.get('nom_angle',120.0)
        self.nom_width = nom_dict.get('nom_width',0.678)
        self.nom_dist = nom_dict.get('nom_dist',2.75)
        self.tol_width = nom_dict.get('tol_width',0.003)
        self.width = width
        self.angle = angle
        self.diameter = diameter
        self.dist = dist
        self.hex_cent = hex_cent
        self.xyangles = xyangles
        self.xypin = xypin
        self.zpin = zpin
        self.zbase = zbase
        self.zhex = zhex
        self.xangles = xangles
        self.yangles = yangles
        self.nom_diff(attr = 'width')
        
    def nom_diff(self, nom=None, attr=None):
    	'''
    	attr must be string
    	returns self.diff_attr
    	'''
    	if nom is None:
    		nom = self.__getattribute__('nom_%s' % attr)
    	val = self.__getattribute__(attr)
    	self.__setattr__('diff_%s' % attr, nom - val)
    	return (nom - val)
    def concentricity(self):
        odx = self.od_coords[0]
        ody = self.od_coords[1]
        wxs = self.width_coords[0,:]
        wys = self.width_coords[1,:]
        conc = [((odx - wx)**2 + (ody - wy)**2)**0.5 for wx in wxs for wy in wys]
        return

class Hex7(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 0.413}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords
        self.fiber = 7
    
    def readfile(self, datafile):
    	'''
    	reads 7 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles

class Hex19(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 0.678}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords
        self.fiber = 19
    
    def readfile(self, datafile):
    	'''
    	reads 19 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles
    
class Hex37(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 0.943}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords,
        self.fiber = 37
    
    def readfile(self, datafile):
    	'''
    	reads 37 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles

class Hex61(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 1.209}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords
        self.fiber = 61
    
    def readfile(self, datafile):
    	'''
    	reads 61 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles


class Hex91(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 1.471}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords
        self.fiber = 91
    
    def readfile(self, datafile):
    	'''
    	reads 91 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles

class Hex127(Hex):
    '''
    class that will house all ferrule data from a given data file
    attributes:
    [angles]: six interior angles on hex
    [widths]: three widths on hex
    [center coords]: coordinates of center relative to lower left corner
    nominals and tolerances
    '''
    def __init__(self, filename):
    	nom_dict = {'nom_width': 1.729}
        angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles = self.readfile(filename)
        Hex.__init__(self, width=widths, angle=angles, xyangles=xyangles, diameter=diameter,
        			dist=distance, hex_cent=hex_cent, xypin=xypin, zpin=zpin, zbase=zbase, zhex=zhex, xangles=xangles, yangles=yangles, **nom_dict)
        self.coords = coords
        self.fiber = 127
    
    def readfile(self, datafile):
    	'''
    	reads 127 fiber ferrule datafile into angles,widths,diameter,distance.
    	'''
        
    	data = num.genfromtxt(datafile,usecols=(3),comments='Step',skip_header=12,
    						invalid_raise=False)
        data = data[num.isfinite(data)]

        angles = num.array([(data[12],data[15],data[0],data[3],data[6],data[9]),(data[43],data[46],data[31],data[34],data[37],data[40]),(data[74],data[77],data[62],data[65],data[68],data[71]),(data[105],data[108],data[93],data[96],data[99],data[102]),(data[136],data[139],data[124],data[127],data[130],data[133]),(data[167],data[170],data[155],data[158],data[161],data[164]),(data[198],data[201],data[186],data[189],data[192],data[195]),(data[229],data[232],data[217],data[220],data[223],data[226]),(data[260],data[263],data[248],data[251],data[254],data[257]),(data[291],data[294],data[279],data[282],data[285],data[288])])
        #for xyanlges I want two rows for each array
        xyangles = num.array([(data[4],data[13],data[5],data[14]),(data[35],data[44],data[36],data[45]),(data[66],data[75],data[67],data[76]),(data[97],data[106],data[98],data[107]),(data[128],data[137],data[129],data[138]),(data[159],data[168],data[160],data[169]),(data[190],data[199],data[191],data[200]),(data[221],data[230],data[222],data[231]),(data[252],data[261],data[253],data[262]),(data[283],data[292],data[284],data[293])])
        xangles = num.array([(data[1],data[4],data[7],data[10],data[13],data[16]),(data[32],data[35],data[38],data[41],data[44],data[47]),(data[63],data[66],data[69],data[72],data[75],data[78]),(data[94],data[97],data[100],data[103],data[106],data[109]),(data[125],data[128],data[131],data[134],data[137],data[140]),(data[156],data[159],data[162],data[165],data[168],data[171]),(data[187],data[190],data[193],data[196],data[199],data[202]),(data[218],data[221],data[224],data[227],data[230],data[233]),(data[249],data[252],data[255],data[258],data[261],data[264]),(data[280],data[283],data[286],data[289],data[292],data[295])])
        yangles = num.array([(data[2],data[5],data[8],data[11],data[14],data[17]),(data[33],data[36],data[39],data[42],data[45],data[48]),(data[64],data[67],data[70],data[73],data[76],data[79]),(data[95],data[98],data[101],data[104],data[107],data[110]),(data[126],data[129],data[132],data[135],data[138],data[141]),(data[157],data[160],data[163],data[166],data[169],data[172]),(data[188],data[191],data[194],data[197],data[200],data[203]),(data[219],data[222],data[225],data[228],data[231],data[234]),(data[250],data[253],data[256],data[259],data[262],data[265]),(data[281],data[284],data[287],data[290],data[293],data[296])])
        widths = num.array([(data[18],data[21],data[24]),(data[49],data[52],data[55]),(data[80],data[83],data[86]),(data[111],data[114],data[117]),(data[142],data[145],data[148]),(data[173],data[176],data[179]),(data[204],data[207],data[210]),(data[235],data[238],data[241]),(data[266],data[269],data[272]),(data[297],data[300],data[303])])
        diameter = num.array([(data[27],data[58],data[89],data[120],data[151],data[182],data[213],data[244],data[275],data[306])])
        #merged 2X2 array into 1 line
        distance = num.array([(data[28],data[321],data[29],data[322]),(data[59],data[324],data[60],data[325]),(data[90],data[327],data[91],data[328]),(data[121],data[330],data[122],data[331]),(data[152],data[333],data[153],data[334]),(data[183],data[336],data[184],data[337]),(data[214],data[339],data[215],data[240]),(data[245],data[342],data[246],data[343]),(data[276],data[345],data[277],data[346]),(data[307],data[348],data[308],data[349])])
        #merged 2X3 array into 1 line
        coords = num.array([(data[19],data[22],data[25],data[20],data[23],data[26]),(data[50],data[53],data[56],data[51],data[54],data[57]),(data[81],data[84],data[87],data[82],data[85],data[88]),(data[112],data[115],data[118],data[113],data[116],data[119]),(data[143],data[146],data[149],data[144],data[147],data[150]),(data[174],data[177],data[180],data[175],data[178],data[181]),(data[205],data[208],data[211],data[206],data[209],data[212]),(data[236],data[239],data[242],data[237],data[240],data[243]),(data[267],data[270],data[273],data[268],data[271],data[274]),(data[298],data[301],data[304],data[299],data[299],data[302])])
        hex_cent = num.array([(data[28],data[29]),(data[59],data[60]),(data[90],data[91]),(data[121],data[122]),(data[152],data[153]),(data[183],data[184]),(data[214],data[215]),(data[245],data[246]),(data[276],data[277]),(data[307],data[308])])
        xypin = num.array([(data[321],data[322]),(data[324],data[325]),(data[327],data[328]),(data[330],data[331]),(data[333],data[334]),(data[336],data[337]),(data[339],data[340]),(data[342],data[343]),(data[345],data[346]),(data[348],data[349])])
        zpin = num.array([(data[350],data[351],data[352],data[353],data[354],data[355],data[356],data[357],data[358],data[359])])
        zbase = num.array([(data[310],data[311],data[312],data[313],data[314],data[315],data[316],data[317],data[318],data[319])])
        zhex = num.array([(data[30],data[61],data[92],data[123],data[154],data[185],data[216],data[247],data[278],data[309])])        
        
        return angles, xyangles, widths, diameter, distance, coords, hex_cent, xypin, zpin, zbase, zhex, xangles, yangles
  
class Superhex(object):
	'''
	class that houses a list of hex objects
	'''
	def  __init__(self, hexlist):
		self.hexlist = hexlist
		Superhex.load_hex(self)
	
	def load_hex(self):
		for i in range(len(self.hexlist)):
			self.__setattr__('hex%i'%(i+1),self.hexlist[i])
		self.nhexs = len(self.hexlist)
		
	def get_tol(self,attrs):
		'''
		tolerance returned and stored in self.diff_attr
		'''
		tol = num.array(len(attrs))
		for attr in attrs:
			 tol = num.array([h.nom_diff(attr = attr) for h in self.hexlist])
		return tol
		
	def get_meas(self,attrs):
		meas = num.array(len(attrs))
		for attr in attrs:
			meas = num.array([h.__getattribute__(attr) for h in self.hexlist])
		return meas
