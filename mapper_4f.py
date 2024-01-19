import sys
import datetime
# input comes from STDIN (standard input)
var=0
for line in sys.stdin:
	var=var+1
	if var==1:
		continue
	line = line.strip()
	line = line.split(",")
	if len(line) >=2:
		amount=line[16]
		date_time= line[2]
		date,time=date_time.split(' ')
		year,month,day=date.split('-')
		hour,min,sec=time.split(':')
		print ('%s\t%s\t%s\t%s' % (month,amount,day,hour))
