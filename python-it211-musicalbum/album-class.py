#create class
class Album:
    def __init__(self,artist,title,length,year):
        self.__artist = artist
        self.__title = title
        self.__length = length
        self.__year = year

    #set method
    def set_artist(self,artist):
        self.__artist = artist
    def set_title(self,title):
        self.__title = title
    def set_length(self,length):
        self.__length = length
    def set_year(self,year):
        self.__year = year

    #get method
    def get_artist(self):
        return self.__artist
    def get_title(self):
        return self.__title
    def get_length(self):
        return self.__length
    def get_year(self):
        return self.__year