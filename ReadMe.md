#What?
This program takes a folder containing Landsat imagery, and composites all of the 30-meter spatial resolution bands within said folder. Users will specify this folder through a raw_input variable, and will also be asked which Landsat Satellite was used to acquire there imagery as well as whether the imagery was acquired before of after May 31, 2003. If the imagery was collected by Landsat 7 after May 31, 2003, the program will correct for errors caused by the deactivation of Landsat 7's scanline corrector.

#Why?
Throughout undergraduate study, I have read a plethora of acedemic journals in regards to sceintific study using remotely sensed imagery. Landsat imagery is undoubtedly the most frequently used form of said imagery, and as such, this program set out to speed up the process of processing this imagery.

#How?
This program used Arcpy, Sys, and OS. Arcpy.sa (spatial analyst) was used for the purpose of accessing focal statistics (used to correct for scanline errors) and for composite bands.
