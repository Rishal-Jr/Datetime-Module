import random
import time
def getdatetime(stardate,enddate):
    print("Printing random date between",stardate,"and",enddate)
    randomgenerator=random.random()
    dateformate="%m/%d/%Y"
    starttime=time.mktime(time.strptime(stardate,dateformate))
    endtime=time.mktime(time.strptime(enddate,dateformate))
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformate,time.localtime(randomtime))
    return randomdate
print("Random Date=",getdatetime(1/1/2020,12/12/2024))
