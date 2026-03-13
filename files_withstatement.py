## how we learnt
f=open("file.txt")
print(f.read())
f.close()

# The above can also written with "with statment" where we dont need to close the file, cause its closes it aut after the with stat

with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the line here
