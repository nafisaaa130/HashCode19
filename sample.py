
f = open('a_example.txt', 'r')
array = f.readlines()
N = array[0]
del array[0]
Harr = []
Varr = []
final = [Harr,Varr]
slides = []

i=0;

for i in range(len(array)):
    array[i]= array[i].split()
    if(array[i][0]=='H'):
        Harr.append(array[i])
        
    if(array[i][0]=='V'):
        Varr.append(array[i])
        

        
        
i=0
for i in range(len(Harr)):
    slides.append(Harr[i])
#print(slides)

i=0
for i in range(len(Varr)):
    slides.append(Varr[i])
print(slides)




def interestfactor(i,j):
    c=0
    k=2
    l=2
    if(slides[i][1]>slides[j][1]):        
        for k in range(len(slides[i])):
            for l in range(len(slides[j])):
                if (slides[i][k]==slides[j][l]):
                    c +=1
                
                
    else: 
        for k in range(len(slides[j])):
            for l in range(len(slides[i])):
                if (slides[j][k]==slides[i][l]):
                    c +=1
        

    return 

    
f.close()
