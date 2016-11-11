from osgeo  import gdal, gdal_array
import numpy as np
import os

directory = "U:\Shared\GIS\StuData\TRTIMM3460\Fall 2016\GISC 3200K\Project_Images\LE70130352012135EDC00"
mask_directory = "U:\Shared\GIS\StuData\TRTIMM3460\Fall 2016\GISC 3200K\Project_Images\LE70130352012135EDC00\gap_mask"
bandlist = []
masklist = []
os.chdir(directory)
for filename in os.listdir(directory):
    if filename[-6] == 'B':
        bandlist.append(filename)
bandlist = tuple(bandlist)

b1 = gdal.Open(bandlist[0])
b2 = gdal.Open(bandlist[1])
array1 = b1.ReadAsArray()
array2 = b2.ReadAsArray()

for maskname in os.listdir(mask_directory):
    if maskname[-6] == 'B':
        masklist.append(maskname)
masklist = tuple(masklist)
os.chdir(mask_directory)
m1 = gdal.Open(masklist[0])
m2 = gdal.Open(masklist[1])
marray1 = m1.ReadAsArray()
marray2 = m2.ReadAsArray()


stacked = np.array([array1,array2])
