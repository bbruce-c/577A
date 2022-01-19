file=open("in.txt", "r", encoding='utf-8')

# print(file.read())
fileR=file.read()
fileS=fileR.split()
print("input:", fileS)
N=len(fileS)
count=0
while (N-count-1)>0:
    temp = fileS[count]
    if(count<(N-count-1)):
        fileS[count]=fileS[N-count-1]
        fileS[N-count-1]=temp
    count=count+2
fileout=open("out.txt", "w")

#for item in fileS:
    #fileout.write(item,"\n")

#fileout.write(str(fileS))

# Ns=len(fileS)
# count=Ns
# while count>0
print("files:", fileS)
for i in range(0, N):
    fileout.write(fileS[i]+' ')
    #fileout.write("\s")
fileout.close()
