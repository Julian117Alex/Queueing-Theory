lamb = float(input("Please enter lambda: "))
mu = float(input("please enter mu: "))
server = int(input("please enter server: "))
def mmc(lamb, mu, server):
  p = lamb / (server * mu)
  f = idk(server, p)
  p0 = 1 / ((server * p)**server / (fact(server) * (1 - p) )+ f)
  lq = (p * (server * p)**server * p0) / (fact(server) * (1 - p)**2)
  l = lq + (lamb / mu)
  wq = (lq) /lamb
  w = l / lamb
  print ("p0")
  print (p0)
  print("lq")
  print(lq)
  print("l")
  print(l)
  print("wq")
  print(wq)
  print("w")
  print(w)

def idk(server, p):
  x = 0
  i = 0
  for i in range(server ):
    x = float(x + (server * p)**(i) / fact(i))
  return x

def fact (number):
  fact = 1
  for t in range(1 ,number + 1 ):
    fact = fact * t
  return fact

look = mmc(lamb, mu, server)
