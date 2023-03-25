from sys import getsizeof

_range = range(100*100)
_list = list(range(100))

size_r = getsizeof(_range)
size_l = getsizeof(_list)

print(size_r > size_l)