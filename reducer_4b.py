import sys
location_dict = {}
for line in sys.stdin:
	line = line.strip()
	location, location_amount= line.split('\t')
	location_amount=float(location_amount)
	if location in location_dict:
		location_dict[location]+=location_amount
	else:
		location_dict[location]=location_amount

#Reducer
max_value=max(location_dict.values())
max_key=max(location_dict,key=location_dict.get)

print("Location "+ max_key +" with the most revenue is : "+ str(max_value) )

