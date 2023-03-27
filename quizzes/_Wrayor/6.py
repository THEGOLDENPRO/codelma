with open("resources\\anyfile.txt", 'r') as File:
    texts = File.readlines()

print(File.closed) # boolean attribute