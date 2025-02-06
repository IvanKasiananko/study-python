def Pifagor(tri):
    f=False
    Storoni = tri
    Storoni.sort()
    if len(tri)!=3 or Storoni[0]+Storoni[1]<=Storoni[2]:
        print("Не корректные данные")
    else:

        if (Storoni[0]**2+Storoni[1]**2)==Storoni[2]**2:
            print("Таки да.Трехугольник пифагоров")
            f=True
    return  f
spisok=list()
print("Введите стороны трехугольника")
for a in range(3):
    print(f"Сторона {a+1}")
    VVod_storoni=int(input(spisok))
    spisok.append(VVod_storoni)
c=Pifagor(spisok)
print(spisok,"->",c)