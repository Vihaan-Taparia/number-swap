# Initial values
a = 1
b = 2
c = 3

print("Initial value of a is",a)
print("Initial value of b is",b)
print("Initial value of c is",c)

# Swapping
a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
