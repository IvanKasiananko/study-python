def Pifagor(tri,a):
    Storoni = tri
    Storoni.sort()
    if len(tri)!=3 or Storoni[0]+Storoni[1]<=Storoni[2] or a==False:
        print("Не корректные данные")
        f=False
    else:

        if (Storoni[0]**2+Storoni[1]**2)==Storoni[2]**2:
            print("Таки да.Трехугольник пифагоров")
            f=True
    return  f
spisok=list()
flag=True
print("Введите стороны трехугольника")
for a in range(3):
    print(f"Сторона {a+1}")
    chek=float(input(spisok))
    VVod_storoni=int(chek)
    if chek==VVod_storoni:
       spisok.append(VVod_storoni)
    else:
        flag=False
        break


c=Pifagor(spisok,flag)
print(spisok,"->",c)