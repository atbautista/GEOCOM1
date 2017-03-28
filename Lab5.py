f = open("C:/Users/abautis/Desktop/GEOG378/CityPop.csv","r")

CSV={}

for line in f:
   fields = line.split(",")

   lat = fields[1]
   lon = fields[2]
   city = fields[3]
   label= fields[4]
   yr1970 = fields[5]
   yr1975 = fields[6]
   yr1980 = fields[7]
   yr1985 = fields[8]
   yr1990 = fields[9]
   yr1995 = fields[10]
   yr2000 = fields[11]
   yr2005 = fields[12]
   yr2010 = fields[13]
   CSV[(yr1970,yr1975,yr1980,yr1985,yr1990,yr1995,yr2000,yr2005,yr2010)] = label

f.close()

s= raw_input("Enter City:")
dic= CSV.values()

if s in dic:
    print "City is in File"
    print CSV[(yr1970)]

#http://stackoverflow.com/questions/11871323/getting-a-specific-value-from-a-csv-file-with-python-raw-input
#http://stackoverflow.com/questions/5040119/querying-csv-with-raw-input-in-python
