## 8 Write a program to make a copy of a text file “this. txt”
with open("this.txt") as f:
    content=f.read()
with open("this_copy.txt","w") as f:
    f.write(content)

## 9. Write a program to find out whether a file is identical & matches the content of another file.
with open("this.txt") as f:
    content1=f.read()
with open("this_copy.txt") as f:
    content2=f.read()

if content1==content2:
    print("Yes the content is same")
else:
    print("No the content is not same")

## 10. Write a program to wipe out the content of a file using python. 

with open("this.txt","w") as f:
    f.write("")

## 11. Write a python program to rename a file to “renamed_by_ python.txt.

with open("old.txt") as f:
    content=f.read()
with open("renamed_by_ python.txt","w") as f:
    f.write(content)
