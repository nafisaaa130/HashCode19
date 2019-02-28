
# coding: utf-8

# In[ ]:



f = open('a_example.txt', 'r')
array = f.readlines()
photosN = array[0]
del array[0]
print(array)


i=0;
for i in range(len(array)):
    array[i]=array[i].split()
    del array[i][1]
print(array)
                 

    
f.close()

