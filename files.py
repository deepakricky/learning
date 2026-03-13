## open and read a file and close
f= open("file.txt")
data=f.read()
print(data)
f.close()

##write in a file
st="Hey bro how are you"
f= open("myfile.txt","w")
f.write(st)
f.close()

## more file functions
f= open("file.txt")

# lines=f.readlines()
# print(lines, type(lines))

line1=f.readline()
print(line1, type(line1))

line2=f.readline()
print(line2, type(line2))

line3=f.readline()
print(line3, type(line3))

line4=f.readline()
print(line4, type(line4))

line5=f.readline()
print(line5, type(line5)) #this will print an empty string

f.close()

##print lines using while loop
f=open("file.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()

## append (adds a line at last)
str="\n Dhoni is our captain" 
f=open("myfile.txt","a")
f.write(str) #adds str to the file whenever i run this


