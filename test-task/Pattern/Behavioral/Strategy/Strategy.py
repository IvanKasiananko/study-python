import abc

class Reader(metaclass=abc.ABCMeta):
    def parse(self,url:str):
        pass

class ResurseReader:
    def __init__(self,reader:Reader):
        self.__reader=reader

    def set_strategy(self,reader:Reader):
        self.__reader=reader

    def read(self,url:str):
        self.__reader.parse(url)

class NewSiteReader(Reader):
    def parse(self,url:str):
        print('Парсинг новостного сайта',url)

class SocialNetworkReader(Reader):
    def parse(self,url:str):
        print('парсинг ленты новостей соцсети')

class TelegramChannelReader(Reader):
    def parse(self,url:str):
        print('Парсинг канала телеграм')

resoure_reader=ResurseReader(NewSiteReader())
url='https://news.com'
resoure_reader.read(url)

url='https://facebook.com'
resoure_reader.set_strategy(SocialNetworkReader())
resoure_reader.read(url)

url='@new_channel_telegram'
resoure_reader.set_strategy(TelegramChannelReader())
resoure_reader.read(url)
