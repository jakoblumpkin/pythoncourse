
f = open("./student.txt", "r")

for i in f.readlines():
    print(i)
f.close()