import copy


class Adress:
    def __init__(self,street_adress,city,country):
        self.street_adress=street_adress
        self.city=city
        self.country=country
    def __str__(self):
        return f"{self.street_adress},{self.city},{self.country}"

class Person:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
    def __str__(self):
        return f'{self.name} живет по адрессу {self.adress}'



oleg= Person('Oleg',Adress("Проспект Лютиков, д.5,кв 27","Киев","Украина"))
print(oleg)
olga=copy.deepcopy(oleg)
olga.name='Olga'
olga.adress.street_adress="улица Зеленая,д 67,кв 15"
print(olga)