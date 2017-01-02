x = input("enter the 1st number: ")
y = input("enter the 2nd number: ")
n = len(str(x))
idx = int(n / 2)
a = int(x[:idx])
b = int(x[idx:])
c = int(y[:idx])
d = int(y[idx:])
ac = a * c
bd = b * d
mul = ((ac*(10**(n))) + (((a+b)*(c+d)) - ac - bd)*((10**(n/2))) + bd)
print(mul)
