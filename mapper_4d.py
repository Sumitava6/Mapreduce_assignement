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
		start_date_time = line[1]
		end_date_time=line[2]
		start_date=start_date_time.split(' ')[0].split('-')
		end_date=end_date_time.split(' ')[0].split('-')
		start_time=start_date_time.split(' ')[1].split(':')
		end_time=end_date_time.split(' ')[1].split(':')
		location = line[7]
		for num in range(len(start_date)):
			start_date[num]=int(start_date[num])
			end_date[num]=int(end_date[num])
			start_time[num]=int(start_time[num])
			end_time[num]=int(end_time[num])

		dt1 = datetime.datetime(start_date[0],start_date[1],start_date[2],start_time[0],start_time[1],start_time[2]) 
		dt2 = datetime.datetime(end_date[0],end_date[1],end_date[2],end_time[0],end_time[1],end_time[2]) 
		tdelta = dt2 - dt1 
		print ('%s\t%s' % (location.strip(), tdelta.total_seconds()))
