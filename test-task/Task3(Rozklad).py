import datetime
from datetime import timedelta



def Rozklad(Days,Work_Day,Rest_Day,Start_day):
    y=Start_day
    f=True
    a=1
    b=1
    List=[]
    for i in range(Days):
        if f==True :
             List.append(y)
             if a==Work_Day :
                a=1
                f=False
             if f==True:
                 a=a+1

        else:
           if b==Rest_Day:
               f=True
               b=1
           if f == False:
                   b = b + 1
        y = y + timedelta(days=1)



    return List

date_str=(input("Введите начальную дату dd/mm/yyyy"))
v='21/03/2025'
start=datetime.datetime.strptime(date_str,'%d/%m/%Y')
Day=int(input("Введите общее количество дней "))
Day_W=int(input("Введите количество дней работы "))
Day_R=int(input("Введите общее количество дней отдыха "))
s=Rozklad(Day,Day_W,Day_R,start)
print(s)




