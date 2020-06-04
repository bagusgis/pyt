import arcpy
outpoly = r'C:\coralreef.shp'
arcpy.RasterToPolygon_conversion("terumbu1.tif",outpoly)
