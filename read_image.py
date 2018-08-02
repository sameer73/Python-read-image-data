# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

import numpy as np
import imageio
import visvis as vv
from PIL import Image,ImageDraw
import sys
import itertools
import os
col = Image.open("input.jpg")
gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
bw = np.asarray(gray).copy()
z = 1 

def mean_calculate(bw):
	temp = []
	for each in bw:
		get_mean = np.mean(each)
		if get_mean >= 120 and get_mean <= 250:
			temp.append('1')
		else:
			temp.append('0')

	return temp


def print_image(temp,bw,generate_img=False):
	low = 0
	upper = 0
	i = 0
	x_obj = []
	y=0
	global z
	directory = 'outputletter/'+str(z)
	if not os.path.exists(directory):
		os.makedirs(directory)			
		z = z+1

	while i < len(temp):
		if temp[i]=='0':
			if low != upper:
				x_bw = bw[low:upper]

				xy = np.transpose(x_bw)
				if generate_img:
					imfile = Image.fromarray(xy)
					imfile.save(directory+"/rest"+str(y)+".jpg")
					y=y+1
				else:
					
					get_list = mean_calculate(xy)
					imfile = Image.fromarray(x_bw)
					imfile.save(directory+"/restupper"+str(low)+".jpg")
					print_image(get_list,xy,generate_img=True)
					
				low = upper
			low = i
			upper = i
		elif temp[i]=='1':
			upper = i
		
		
		i = i+1

	return True

get_list = mean_calculate(bw)
print_image(get_list,bw,generate_img=False)