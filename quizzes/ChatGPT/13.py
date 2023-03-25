my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {v:k for k,v in my_dict.items()}
print(new_dict)
