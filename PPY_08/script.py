gen = (val**2 if(val<0) else val**3  for val in range(-5, 7, 2))
print(gen)

lst = [val**2 if(val<0) else val**3  for val in range(-5, 7, 2)]
print(lst)

st = {val**2 if(val<0) else val**3  for val in range(-5, 7, 2)}
print(st)

dc = {val: val**2 if(val<0) else val**3  for val in range(-5, 7, 2)}
print(dc)

dc2 =  {k:v for k, v in zip(range(0, 10), range(50, 90))}
print(dc2)