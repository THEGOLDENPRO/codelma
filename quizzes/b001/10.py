x = [4, -5, 6]
y = lambda x: abs(x//2)
z = list(map(y, x))
print(z)
