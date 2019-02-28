
# coding: utf-8

# In[ ]:




f = open('a_example.txt', 'r')
array = f.readlines()
N = array[0]
del array[0]
print(array)
Harr = []
Varr = []
final = [Harr,Varr]

i=0;
for i in range(len(array)):
    array[i]=array[i].split()
    del array[i][1]
    if(array[i][0]=='H'):
        Harr.append(array[i])
    if(array[i][0]=='V'):
        Varr.append(array[i])
print(array)

                 


    
    
f.close()

