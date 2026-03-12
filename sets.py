# e = set() # this is used to create a empty set# Dont use s = {} as it will create an empty dictionary
# s={1,2,4,4,4,55,66,"dragon"}
# print(s,type(s)) #this will not print repeated values

# #methods
# s.add(99)
# print(s)
# s.remove(55)
# print(s,type(s))
# s.pop()#removes random element
# print(s)

set1={1,2,4,10}
set2={2,5,10}
print(set1.union(set2))
print(set1.intersection(set2))
