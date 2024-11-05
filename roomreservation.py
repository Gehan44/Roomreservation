from asyncore import write
from itertools import repeat
import time

f = open("meeting_room.txt")
f1 = f.readline()
f2 = f.readline()                                  
f3 = f.readline()
room = int(f1.split(':')[1])
ff2 = int(f2.split(':')[1])
ff3 = f3.split(':')[1]
fff3 = ff3.split(',')
fk = ([int(x) for x in fff3])
f.close()

count = 0
x = 0
y = 0
hour = 7
rm = [[] for i in repeat(None,room)]
lst = []
def meetroom():
    global count
    global y
    if len(fk) == ff2:
        x = 0
        for yy in range(len(rm)):
            while len(fk) != 0:
                if (sum(rm[y]))+fk[x] <= hour:
                    rm[y].append(fk[x])
                    fk.pop(x)
                    count+=1
                    if sum(rm[y]) >= hour:
                        y+=1 
                else:
                    y=0
                    i=1
                    while i != len(rm):
                        if sum(rm[y+i])+fk[x] <= hour:
                            rm[y+i].append(fk[x])
                            fk.pop(x)
                            count+=1
                        else:
                            lst.append(fk[x])
                            fk.pop(x)
                            count+=1
                        i += 1         
            x+=1
    else:
        print("j and t not the same")

start = time.time()

ans = open("reservation.txt","w")
meetroom()
print(rm)
print(lst)
a = 1
for n in rm:
    ans.write('%s:'%a)
    for b in n:
        ans.write("(%s)"%b)
    a+=1
    ans.write("\n")
ans.write("0:%s"%lst)

end = time.time()

print("Second: %f"%((end-start)/1000))
print("Count: %s"%count)