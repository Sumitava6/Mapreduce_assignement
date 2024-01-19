import sys
# input comes from STDIN (standard input)
var=0
for line in sys.stdin:
	var=var+1
	if var==1:
		continue
	line = line.strip()
	line = line.split(",")
	if len(line) >=2:
		vendor = line[0]
		total_amount = line[16]
		print ('%s\t%s' % (vendor.strip(), total_amount.strip()))


