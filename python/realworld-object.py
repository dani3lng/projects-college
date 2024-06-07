#create class for tv
class Tv:
    #the init method initializes the attributes
    def __init__(self,brand,width,height,depth,size):
    
        #set the width,height,depth,size according to the input parameters
        self.__brand = brand
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__size = size
 
        #return the brand
        def get_brand(self):
            return self.__brand
        #return the width
        def get_width(self):
            return self.__width
        #return the height
        def get_height(self):
            return self.__height
        #return the depth
        def get_depth(self):
            return self.__depth
        #return the size
        def get_size(self):
            return self.__size
