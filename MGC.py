import math

lamb = float(input("Please enter the lambda: "))
mu = float(input("Please enter the mu: "))
a = float(input("Please enter the a: "))
b = float(input("Please enter the b: "))
server = float(input("Please enter the server: "))

p = lamb/mu
theta = math.sqrt(((a-b)**2)/12)
wq = (theta**2) + 1/(mu**2)
wq = (wq * lamb) / (2 * (1 - (lamb / mu)))
lq = lamb * wq
w = wq + server
l = lamb * w
print("W: ", w)
print("wq: ", wq)
print("L: ", l)
print("lq", lq)
print("p:", p)