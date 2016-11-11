from osgeo  import gdal, gdal_array
import numpy as np
import os

directory = "U:\Shared\GIS\StuData\TRTIMM3460\Fall 2016\GISC 3200K\Project_Images\LE70130352012135EDC00"
bandlist = []
os.chdir(directory)
for filename in os.listdir(directory):
    if filename[-6] == 'B':
        bandlist.append(filename)
bandlist = tuple(bandlist)
b1 = gdal.Open(bandlist[0])
b2 = gdal.Open(bandlist[1])

array1 = b1.ReadAsArray()
array2 = b2.ReadAsArray()
stacked = np.array([array1,array2])

gdal_array.SaveArray(stacked.astype("int"), "b12_stacked.tif",
                                "GTiff", gdal.Open(bandlist[0]))
