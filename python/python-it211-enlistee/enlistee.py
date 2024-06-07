#Enlistee and Private classes

#create enlistee class
class Enlistee:
    
    #set __init__ method for attributes
    def __init__ (self, name, number):
        #set attributes
        self.__name = name
        self.__number = number

    #create mutator method
    def set_name (self, name):
        self.__name = name
    def set_number (self, number):
        self.__number = number

    #create accessor method
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    
#create private subclass
class Private(Enlistee):

    #set __init__ method for attributes
    def __init__(self, name, number, platoon, years):
        Enlistee.__init__(self, name, number)
        self.__platoon = platoon
        self.__years = years

    #create mutator method
    def set_platoon(self, platoon):
        self.__platoon = platoon
    def set_year(self, years):
        self.__years = years

    #create accessor method
    def get_platoon(self):
        return self.__platoon
    def get_years(self):
        return self.__years

#create general subclass
class General(Enlistee):

    #set __init__ method
    def __init__(self,name,number,salary,bonus):
        Enlistee.__init__(self,name,number)
        self.__salary = salary
        self.__bonus = bonus
    #create mutator method
    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = bonus
    #create accessor method
    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus