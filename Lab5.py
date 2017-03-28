CityPop={}
npts = 0
f = open("C:/Users/abautis/Desktop/GEOG378/CityPop.csv","rt")
for line in f:
   fields = line.split(',')

   latitude = fields[1]
   longitude = fields[2]
   city = fields[3]
   yr2010 = fields[13]

   npts += 1

