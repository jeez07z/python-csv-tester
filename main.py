import csv

from datetime import datetime
from dateutil.tz import tzlocal

# assign local timezone
local_tz =  datetime.now(tzlocal()).astimezone().tzinfo

# define time format
format = "%Y-%m-%d %H:%M:%S"

# read from input.csv, append timezone and datetime and write to output.csv 
with open('input.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []

        for row in reader:
            utc_datetime = datetime.strptime(row[0], format)
            local_datetime = utc_datetime.astimezone(local_tz)
            row.append(local_tz)
            row.append(local_datetime.strftime(format))
            all.append(row)

        writer.writerows(all)
       
