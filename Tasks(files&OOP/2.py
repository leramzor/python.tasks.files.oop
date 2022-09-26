import sys
sum=0 #declare value
n=len(sys.argv)#count number of elements
for i in range(1, n):#loop for range
    sum+= int(sys.argv[i])
print(sum)