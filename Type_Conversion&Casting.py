# Type conversion
a = 2
b = 2.5

c = a + b
# c will be of type float since float is superior to int , int will be converted to float
print(c)

# TypeCasting
# Since in python addition of float with string is not allowed , we need to use typecasting

str = "32"
d = int(str)
print(d + 35)