## 6. Write a program to mine a log file and find out whether it contains ‘python’. 
with open("log.txt") as f:
    c=f.read()
if("python" in c):
    print("Yes python is in log")
else:
    print("Not in the log")

##7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"yes python is in line {lineno}")
        break
    lineno += 1
else:
    print("Not in the list")
