def puissance(a,b):
 if not type(a) is int:
  raise TypeError ("erreur")
  for _ in range(b):
    result *= a
  return result if b < 0 else 1/result
