import math

n = 2  
somatorio = 0

while n < 1000:
  somatorio = somatorio + (1/(n * (math.log(n, math.e) ** 2)))
  print(somatorio)
  n = n + 1