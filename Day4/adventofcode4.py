import re

def pairup(str):
    results=[]
    for i in range(len(str)-1):
        results.append(str[i]+str[i+1])
    return results

def ascending(seq):
    for i in range(len(seq)-1):
        if (int(seq[i])>int(seq[i+1])):
            return False
    return True

def check_tripple(seq):
    if len(seq) == 1:
        return True
    elif((re.search(regex, seq[0])) or (re.search(regex, seq[-1]))):
        return True
    return False
#"""
#def reverse_pair(seq):
#    result=""
#    for s in seq:
#        result+=s[0]
#    result+=seq[-1][-1]
#    return result
#"""    

regex=r"([0-9])\1"
regex2=r"([0-9])\1\1+"
#2365
numbers=[str(i) for i in range(178416,676462)]
passwds=list(filter(lambda x: ascending(x), numbers))
passwds=list(filter(lambda x: re.search(regex,x), passwds))

print(len(numbers))
print(len(passwds))
passwds=list(map(lambda x: re.split(regex2,x), passwds))
passwds=list(filter(lambda x: check_tripple(x), passwds))
print(len(passwds))
with open("results2.txt","w") as f:
    for p in passwds:
        f.write(p+"\n")
