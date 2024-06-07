#House Class program

#create class
class House:
    def __init__(self,year_built,sqr_ft):
        self.__year_built = year_built
        self.__sqr_ft = int(sqr_ft)
        self.__num_beds = 1
        
    def add_bed(self):
        self.__num_beds += 1
    def addition(self):
        self.__sqr_ft += 100

    def get_num_beds(self):
        return self.__num_beds
    def get_sqr_ft(self):
        return self.__sqr_ft
    def get_year_built(self):
        return self.__year_built

h1 = House('2012','1600')

for i in range(5):
    h1.add_bed()
    beds = h1.get_num_beds()
    print('There are', beds,'bedrooms in the house.')
for i in range(5):
    h1.addition()
    sqr = h1.get_sqr_ft()
    print('The house is on', sqr,'square feet of land.')
