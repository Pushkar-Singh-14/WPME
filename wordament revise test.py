import random
import matplotlib.pyplot as plt
from matplotlib import style

fig = plt.figure(figsize=(13,8), dpi=100)
ax1 = fig.add_subplot(1,1,1)

Data={}
i=1
lines=[]
count=0
path="/Users/pushkarsingh/Desktop/revise_words_training.txt"
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
last_150=len(Word)-150
last_100=len(Word)-100
last_50=len(Word)-50
for i in range(0,len(Word)):
    num_list.append(i)
    c=len(num_list)
for i in range(c):
    try:
        x=random.randint(0,len(num_list))
        y=num_list[x]
        num_list.remove(y)

        x_input = input()
        if (x_input)!="e":
            print("{}/{}".format(str(j),str(c)))
            print(Word[y])
            j+=1

        z_input = input()
        if (z_input)!="e":
            print(Def[y],page_number[y])
        
            
    except:
        pass

