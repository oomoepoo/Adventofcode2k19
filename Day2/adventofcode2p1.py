file=r"C:\Users\Jan\Documents\input2"

def operate(opcode, arg1, arg2):
    if (opcode==1):
        return arg1+arg2
    elif (opcode==2):
        return arg1*arg2
with open(file, "r") as f:
    data=f.readline().split(",")
data=[int(d) for d in data]

data[1]=12
data[2]=2
#data=[1,0,0,0,99]
#data=[2,3,0,3,99]
#data=[2,4,4,5,99,0]
#data=[1,1,1,4,99,5,6,0,99]
i=0
while(1):
    #check if operation is 99 BEFORE anything else, to prevent index errors.
    if (data[i]==99):
        break
    j = operate(data[i],data[data[i+1]],data[data[i+2]]) #this is potentially dangerous but I guess the data takes care of not going oob
    data[data[i+3]]=j #this is potentially dangerous but I guess the data takes care of not going oob
    i+=4

for i in data:
    print(i)
    if i == 99:
        break