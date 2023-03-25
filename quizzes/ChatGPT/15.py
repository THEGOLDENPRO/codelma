my_str = "Hello, World!"
new_str = "".join(list(filter(lambda x: x.isalpha(), my_str)))
print(new_str)
