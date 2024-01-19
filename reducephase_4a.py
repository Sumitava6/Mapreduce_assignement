import sys
vendor_dict = {}
for line in sys.stdin:
	line = line.strip()
	vendor, vendor_amount = line.split('\t')
	vendor_count, vendor_amount= int(vendor), float(vendor_amount)
	if vendor in vendor_dict:
		vendor_dict[vendor][1]+=vendor_amount
		vendor_dict[vendor][0]+=vendor_count
	else:
		vendor_dict[vendor] = []
		vendor_dict[vendor].append(vendor_count)
		vendor_dict[vendor].append(vendor_amount)

#Reducer

if vendor_dict['1']>=vendor_dict['2']:
	print("Creative Mobile Technologies has more trips\n"+"count: "+str(vendor_dict['1'][0])+"\nrevenue: "+str(vendor_dict['1'][1]))
else:
	print("VeriFone Inc. has more trips\n"+"count: "+str(vendor_dict['2'][0])+"\nrevenue: "+str(vendor_dict['2'][1]))
