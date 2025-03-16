import abc
from typing import Dict

class ISite(metaclass=abc.ABCMeta):
    def get_page(self,num:int):
        pass

class Site(ISite):
    def get_page(self,num:int):
        return 'Это страница {}'.format(num)

class SiteProxy(ISite):
    def __init__(self,site:ISite):
        self.__site=site
        self.__cache:Dict[int,str]={}

    def  get_page(self,num:int):
         page:str=''
         if self.__cache.get(num) is not None:
             page=self.__cache[num]
             page='из кэша:'+ page
         else:
             page=self.__site.get_page(num)
             self.__cache[num]=page
         # print(self.__cache)
         return page
my_site=SiteProxy(Site())
print(my_site.get_page(1))
print(my_site.get_page(2))
print(my_site.get_page(3))

print(my_site.get_page(2))
