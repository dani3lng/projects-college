# Class for computers

class Computer:
    #Defining a Function to set  the properties
    def __init__(self,model,speed, storage):
        self.model = model
        self.speed = speed
        self.storage = storage
    #defining a  retuen function to print the model of the computer    
    def name(self):
        print( self.model)

#Creating an instance of the class
c1 = Computer('Asus', '3.0 GHz', '500 GB' )

c1.name()
