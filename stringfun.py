# name= "gaggasoftware" #0 is g, 1 is a ......
# name='gagga'
# name='''gagga'''
# print(len(name))
# #indexing
# nameshort=name[0:4]
# print(nameshort)
# character1=name[1]
# print(character1)
# print(name[-6:-2])
# print(name[:4]) # is same as print(name[0:4])
# print(name[1:]) # is same as print(name[1:5])
# print(name[1:5])

#skipslicing
anime=("naruto")
print(anime[0:6:2])

#str fun
print(len(anime))
print(anime.endswith("uto"))
print(anime.endswith("kkk"))
print(anime.startswith("NAR"))# N and n are diff char, this fun is case sensitive
print(anime.capitalize())
print(anime.replace("ut","mo"))

#Escpae seq characters
sentence="give me your number \n i will call \"you\""
print(sentence)
