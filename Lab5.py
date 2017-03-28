CityPop={}

f = open("C:/Users/abautis/Desktop/GEOG378/CityPop.csv","rt")
for line in f:
   fields = line.split(',')

   latitude = fields[1]
   longitude = fields[2]
   city = fields[3]
   label= fields[4]
   yr1970 = fields[5]
   yr1975 = fields[6]
   yr1980 = fields[7]
   yr1985 = fields[8]
   yr1990 = fields[9]
   yr1995 = fields[10]
   yr2000 = fields[11]
   yr2010 = fields[12]
   yr2010 = fields[13]


