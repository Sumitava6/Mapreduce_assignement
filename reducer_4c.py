import sys
payment_dict = {}
for line in sys.stdin:
	payment = line.strip()
	if payment in payment_dict:
		payment_dict[payment]+=1
	else:
		payment_dict[payment]=1

#Reducer

sorted_payment_dict = sorted(payment_dict.items(), key=lambda x:x[1])

for key,value in sorted_payment_dict:
	print("payment method: " + key+ "\t Num_of transactions : "+str(value))
