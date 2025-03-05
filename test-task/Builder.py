from abc import ABCMeta

class Phone:
    def __init__(self):
        self.date:str=""

    def about_phone(self):
        return self.date



    def append_date(self,string:str):
        self.date+=string

class IDeveloper(metaclass=ABCMeta):
    def create_display(self):
        pass
    def create_box(self):
        pass
    def system_install(self):
        pass
    def get_phone(self):
        pass

class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone=Phone()

    def create_display(self):
        self.__phone.append_date("Произведен дисплей Samsung;")
    def create_box(self):
        self.__phone.append_date("Произведен корпус Samsung;")
    def system_install(self):
        self.__phone.append_date("Установлена система Андроид")
    def get_phone(self):
        return self.__phone

class IFoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_date("Произведен дисплей Ifone;")

    def create_box(self):
        self.__phone.append_date("Произведен корпус Ifone;")

    def system_install(self):
        self.__phone.append_date("Установлена система IOS")

    def get_phone(self):
        return self.__phone
class Director:
    def __init__(self,developer:IDeveloper):
        self.__developer=developer

    def set_developer(self,developer:IDeveloper):
        self.__developer=developer

    def mount_olny_phone(self):
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()

    def mount_full_phone(self):
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()
        return self.__developer.get_phone()

android_developer:IDeveloper=AndroidDeveloper()
director=Director(android_developer)

samsung:Phone=director.mount_full_phone()
print(samsung.about_phone())

iphone_developer:IDeveloper=IFoneDeveloper()
director.set_developer(iphone_developer)
iphone:Phone=director.mount_olny_phone()
print (iphone.about_phone())
