import datetime
from datetime import timedelta



def schedule(day, work_day, rest_day, start_day):
    day_count=start_day
    f=True
    work_day_count=1
    rest_day_count=1
    List=[]
    for i in range(day):
        if f==True :
             List.append(day_count)
             if work_day_count==work_day :
                work_day_count=1
                f=False
             if f==True:
                 work_day_count=work_day_count+1

        else:
           if rest_day_count==rest_day:
               f=True
               rest_day_count=1
           if f == False:
               rest_day_count = rest_day_count + 1
        day_count = day_count + timedelta(days=1)



    return List

schedule_data={
    "days":5,
    "work_days":2,
    "rest_day":1,
    "start_date":datetime.datetime(2020,1,30)
              }

schedule_rezult=schedule(schedule_data.get("days"),schedule_data.get("work_days"),schedule_data.get("rest_day"),schedule_data.get("start_date"))

print(schedule_rezult)



