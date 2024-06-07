#Property tax assessment

tax = 0.70

#ask for the value of property
value = float(input('What is the value of the property? '))

#calculatation
a_value = value * tax
p_tax = a_value/100

#display assessment value
#display property tax
print('Your assessment value is $%.2f' % a_value)
print('Your property tax is $%.2f '% p_tax,'per $100')