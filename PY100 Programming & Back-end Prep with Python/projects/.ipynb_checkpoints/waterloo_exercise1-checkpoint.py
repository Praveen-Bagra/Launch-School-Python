x = 166
y = 379
z = 263

tmp = max(x,y)
x = min(x,y)
y = tmp
tmp = max(y,z)
y = min(y,z)
z = tmp
tmp = max(x,y)
x = min(x,y)
y = tmp

print(x, y, z)