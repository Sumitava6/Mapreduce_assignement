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
		payment= line[9]
		print ('%s' % (payment.strip()))
