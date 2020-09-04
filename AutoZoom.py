import webbrowser as wb
from dateutil.relativedelta import *
from datetime import *

currentTime = datetime.now()
# currentTime = datetime.now().replace(hour=11,  minute=6, second=0, microsecond=0)

today9am = datetime.now().replace(hour=9,  minute=0, second=0, microsecond=0)
today10am = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
today11am = datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)
today12pm = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
today1pm = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)

times = [today9am, today10am, today11am, today12pm, today1pm]
MWTimes = [today10am, today11am, today12pm, today1pm]
TThTimes = [today9am, today12pm]
FTimes = [today9am, today10am, today11am, today1pm]

classTimes = {
    today9am: "https://byu.zoom.us/j/91277814447",
    today10am: "https://byu.zoom.us/j/95410316293",
    today11am: "https://byu.zoom.us/j/94375040389?pwd=WlpUSUFINEEzQlpidEc3cW9qRFFqQT09",
    today12pm: "https://byu.zoom.us/j/93122632257?pwd=UUt4d0VjcFRRWk1HcklRNURVVFVUdz09",
    today1pm: "https://byu.zoom.us/j/99200035497?pwd=alR6R1dYZE9yVmkydVFuc01lVDFZQT09"
}


def getClassTime(times):
    shortestTime = relativedelta(currentTime, times[0])
    finalTime = times[0]

    for time in times:
        timeUntil = relativedelta(currentTime, time)

        if abs(shortestTime.hours) >= abs(timeUntil.hours):
            if abs(shortestTime.minutes >= abs(timeUntil.minutes)):
                finalTime = time

    return finalTime


if currentTime.weekday() == 0 or currentTime.weekday() == 2:  # MONDAY/WEDNESDAY
    classTime = getClassTime(MWTimes)
elif currentTime.weekday() == 1 or currentTime.weekday() == 3:  # TUESDAY/THURSDAY
    classTime = getClassTime(TThTimes)
else:  # FRIDAY
    classTime = getClassTime(FTimes)

print(classTime)
wb.open(classTimes[classTime])
