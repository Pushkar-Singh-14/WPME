import random
import matplotlib.pyplot as plt
from matplotlib import style

fig = plt.figure(figsize=(13,8), dpi=100)
ax1 = fig.add_subplot(1,1,1)

Data={}
i=1
lines=[]
count=0
path="/Users/pushkarsingh/Desktop/word power made easy copy.txt"
path_report="/Users/pushkarsingh/Desktop/Tests/Reports/worament test.txt"

f_report=open(path,"r")
for name in f_report.readlines():
    lines.append(name)
    
f_report.close()

for line in lines:
    try:
        a=str()
        words= line.split()
        
        
        page_num=words[0]
        boo= words[1]
        for word in words[2:]:
            a=a+word+" "
        Data.update({i:[page_num,boo,a]})
        i+=1
        
    except:
        pass
 
page_number=[]
Word=[]
Def=[]
j=1
for key,value in Data.items():
    
    page_number.append(value[0])
    Word.append(value[1])
    Def.append(value[2])

num_list=[]
last_100=len(Word)-100
for i in range(last_100,len(Word)):
    num_list.append(i)
    c=len(num_list)
for i in range(10000):
    try:
        x=random.randint(0,len(num_list))
        y=num_list[x]
        num_list.remove(y)

        x_input = input()
        if (x_input)!="e":
            print("{}/{}".format(str(j),str(c)))
            print(Word[y])
            j+=1
        else:
            f_report=open(path_report,"a+")
            f_report.write(("{}\n".format(j)))
            f_report.close()
            break

        z_input = input()
        if (z_input)!="e":
            print(Def[y],page_number[y])
        else:
            f_report=open(path_report,"a+")
            f_report.write(("{}\n".format(j)))
            f_report.close()
            break
    except:
        pass
Data1=[]    
f_report=open(path_report,"r")    
for name in f_report.readlines():
    Data1.append(name)
f_report.close()
xar=[]
yar=[]
for data in Data1:
    xar.append(float(data))
    count+=1
    yar.append(count)
plt.plot(yar,xar)
plt.show()
