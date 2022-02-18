import time
import math

#declare variable for the concert start time at 7PM on March 29 and convert to a float
concertStart = time.strptime("29 Mar 22 19", "%d %b %y %H")
concertStartDec = time.mktime(concertStart)

#find current time and convert to a float
currentTime = time.localtime()
currentTimeDec = time.mktime(currentTime)

#find the difference between the concert start time and current time in seconds
timeDiff = concertStartDec - currentTimeDec

#convert time difference from seconds to days and round down
dayDiff = timeDiff/86400
diffDayInt = math.floor(dayDiff)

#subtract number of days in seconds from time difference, convert to hours, and round down
hourDiff = (timeDiff-(diffDayInt*86400))/3600
diffHourInt = math.floor(hourDiff)

#subtract sum of number of days and number of hours from time difference, convert to minutes, and round down
minDiff = (timeDiff-((diffHourInt*3600)+(diffDayInt*86400)))/60
diffMinInt = math.floor(minDiff)

#print output to console
print("The Greta Van Fleet concert at US Bank Arena starts in " + str(diffDayInt) + " days, " + str(diffHourInt) + " hours, and " + str(diffMinInt) + " minutes.")
