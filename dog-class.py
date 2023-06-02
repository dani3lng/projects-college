#dog class

class Dog:

    #initialize attributes
    def __init__(self, breed, size, sex, hair):

        #set attributes
        self.__breed = breed
        self.__size = size
        self.__sex = sex
        self.__hair = hair

    #acceptors for attributes
    def set_breed(self,breed):
        self.__breed = breed
    def set_size(self,size):
        self.__size = size
    def set_sex(self,sex):
        self.__sex = sex
    def set_hair(self,hair):
        self.__hair = hair

    #return attributes
    def get_Breed(self):
        return self.__breed
    def get_Size(self):
        return self.__size
    def get_Sex(self):
        return self.__sex
    def get_Hair(self):
        return self.__hair