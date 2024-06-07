#receive ticket costs
section_a = int(input('How much are seats in Section A? '))
section_b = int(input('How much are seats in Section B? '))
section_c = int(input('How much are seats in Section C? '))

#ask number of sales for each section
for sales in range (1):
    class_a = int(input('How many tickets were sold for Class A seats: '))
    total_a = class_a * section_a
    class_b = int(input('How many tickets were sold for Class B seats: '))
    total_b = class_b * section_b
    class_c = int(input('How many tickets were sold for Class C seats: '))
    total_c = class_c * section_c

#display sales
print('Total Class A seats sold is $%.2f'% total_a)
print('Total Class B seats sold is $%.2f'% total_b)
print('Total Class C seats sold is $%.2f'% total_c)
total_s = total_a+total_b+total_c
print('Total generated income from sales is $%.2f'% total_s)