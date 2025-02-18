def pifagor(tri):
    sides = tri
    sides.sort()
    if sides[0]+sides[1]<=sides[2] :
        f=False
    else:

        if (sides[0]**2+sides[1]**2)==sides[2]**2:
            f=True
    return  f

triangle_list=[[5,4,3],[6,8,10],[100,3,65]]
for i in triangle_list:
    c = pifagor(i)
    print(i, "->", c)