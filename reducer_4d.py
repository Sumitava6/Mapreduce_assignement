import sys
import datetime
location_dict = {}
for line in sys.stdin:
	line = line.strip()
	location, location_time = line.split('\t')
	location_count, location_time= int(location), float(location_time)
	if location in location_dict:
		location_dict[location][1]+=location_time
		location_dict[location][0]+=location_count
	else:
		location_dict[location] = []
		location_dict[location].append(location_count)
		location_dict[location].append(location_time)

#Reducer
for location in location_dict.keys():
	average_time_min=round(((location_dict[location][1]/location_dict[location][0])/60),2)
	average_time_min_decimal=round(((location_dict[location][1]/location_dict[location][0])//60),2)
	
	print(" for location id "+ location +" the average amount is:"+"\t"+str(average_time_min)+" mins "+str(average_time_min_decimal)+" secs")
