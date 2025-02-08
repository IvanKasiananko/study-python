def Battle(Zombi,Plant):
    StrengthZ=sum(Zombi)
    StrengthP=sum(Plant)
    z=0
    p=0
    LenZ=len(Zombi)
    LenP=len(Plant)
    if LenZ>LenP:
        Razn=LenZ-LenP
        Max=LenP
        z=z+Razn
    else:
        Razn=LenP-LenZ
        Max=LenZ
        p=p+Razn

    for a in range(Max):
        if Zombi[a]>Plant[a]:
            z=z+1
        elif Plant[a]>Zombi[a]:
            p=p+1
    print(z,p)
    if z>p:
        f=False
    elif z==p:
        if StrengthZ>=StrengthP:
            f=True
        else:
            f=False
    else:
        f=True
    return f

def Vvod(who):
    Team=list()
    SolNum = 1
    a=1
    while a != 5:
        print(f"{who} номер {SolNum}")
        chek=input(Team)
        if chek!='':
           VVod_unit= int(chek)
           Team.append(VVod_unit)
           SolNum=SolNum+1

        else:
             a=5

    return Team

print("Введите спиок растений.Пустое значение конец списка(press Enter)")
Plants = Vvod("Растение")
print("Введите спиок зомби.Пустое значение конец списка(press Enter)")
Zombies=Vvod("Зомби")
win=Battle(Zombies,Plants)
print("Зомби",Zombies,"Растения ",Plants,"--->",win)



