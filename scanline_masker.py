import sys, os, arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

wd="C:\Imagery\LE70180362016309EDC00" #have this as your directory where all rasters are located

arcpy.env.workspace = wd
raster_list=arcpy.ListRasters("", "tif")

for Ras in raster_list:
    arcpy.AddMessage("Processing" + Ras)
    desc = arcpy.Describe(Ras)
    if desc.bandCount == 1:
        arcpy.SetRasterProperties_management(Ras, nodata="1 0")
    Con(IsNull(Ras), FocalStatistics(Ras, NbrRectangle(15,15,"CELL"),"MEAN"),Ras).save("C:\Imagery\LE70180362016309EDC00\SC_Corrected\{}".format(Ras))

 
        
