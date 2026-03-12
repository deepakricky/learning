#translate telugu to english taking input from user
# words={
#     "ekkada":"where",
#     "endhuku":"why",
#     "eppudu":"when"
# }
# word=input("Enter the telugu word:")
# print("The meaning in english is: ",words[word])

# s=set() #empty set
# n=int(input("enter num: "))
# s.add(n)
# n=int(input("enter num: "))
# s.add(n)
# n=int(input("enter num: "))
# s.add(n)
# n=int(input("enter num: "))
# s.add(n)
# n=int(input("enter num: "))
# s.add(n)
# print(s)

#creat emp dic, and take inp of frnds name and their fav lang

d={}

name=input("Enter friends name: ")
lang=input("Enter his fav lang: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter his fav lang: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter his fav lang: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter his fav lang: ")
d.update({name:lang})

print(d)
