marks={"deepak":100,"naruto":69,"king":67,0:"zoro"}
print(marks["deepak"])
#dict methods
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"deepak":99,"KSI":67})
print(marks)

print(marks.get("jimmy"))     #gives none
# print(marks["jimmy"])       #gives error

print(marks.pop(0)) #removes a spec key and returns its value
print(marks)

print(marks.popitem()) #removes the last item from the dict
print(marks)
