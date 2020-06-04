import arcpy
outpoly = r'E:\oprek\coralreef.shp'
arcpy.RasterToPolygon_conversion("terumbu1.tif",outpoly)
