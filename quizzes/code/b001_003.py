def foo(x):
    if x == 0:
        return 0
    else:
        return foo(x-1)

a = foo(3)
print(a)
