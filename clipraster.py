import gdal

gdal.UseExceptions()

rasin = "lyzenga.tif"
shpin =	"batas.shp"
rasout = "coral.shp"

result = gdal.Warp(rasout, rasin, cutlineDNSName=shpin)

iface.addRassterLayer(rasout)