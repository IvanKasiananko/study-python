class Point:

    """Hren"""
    def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z

    def chek_coord(self):
        for attr in self.__dict__:
            if getattr(self,attr,False)<0:
                print('координаты не могут быть меньше ноля')
                setattr(self,attr,0)
            elif getattr(self,attr,False)>100:
                print('координаты не могут быть больше 100')
                setattr(self, attr,100)
        print(self.__dict__)
    def get_attr(self):
        print(self.__dict__)

    def set_attr(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        print(self.__dict__)
coord1=Point(-1,101,60)
coord1.get_attr()
coord1.chek_coord()
coord1.set_attr(1000,1000,-5)
coord1.get_attr()
coord1.chek_coord()


