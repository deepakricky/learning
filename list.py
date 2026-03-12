everything=["Naruto", 22.5, 5, False, "Deepak"] #list
print(everything)
print(everything[0]) #gives us Naruto as it add is 0
everything[0]="Itachi"
print(everything[0]) #unlike strings, lists are mutable
print(everything[0:2]) 
#list methods
everything.append("Dragon")
print(everything)

numbers=[2,7,4,1,9,6]
print(numbers)
numbers.sort()
print("after sort: ",numbers)
numbers.reverse()
print("reverse:",numbers)
numbers.insert(0, 55) #0 is index.
print(numbers)
numbers.pop(2)#delete number at index 2
print(numbers)
numbers.remove(55)
print(numbers)
