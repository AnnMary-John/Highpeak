from itertools import combinations

#function to find difference of maximum and minimum value
def find_diff(l):
    a=max(l)
    b=min(l)
    return a-b

#open input file
fi = open(r"F:\highpeak\input.txt", "r")

#open output file
fo = open(r"F:\highpeak\answer.txt","w")

#read contents of the file
temp = fi.read().splitlines()

pricelist=[]
d={}
index=0

#find number of employees
nemp=int(temp[0][-1])

for i in range(4,14): # to get all goodies and prices mapped to a dictionary
    m=temp[i].split(":")
    d[int(m[1])]=m[0]
    pricelist.append(int(m[1]))

#get all combinations of the pricelist
combo=list(combinations(pricelist,nemp))

minval=find_diff(combo[0])

for i in range(1,len(combo)):
    val=find_diff(combo[i])
    if(minval>=val):
        minval=val      # minimum difference
        index=i         # index of combination with minval

#write output to file
fo.write("The goodies selected for distribution are:\n \n")
for i in combo[index]:
    s=d[i]+": "+str(i)
    fo.write(s+"\n")

fo.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(minval))

#close files
fo.close()
fi.close()




