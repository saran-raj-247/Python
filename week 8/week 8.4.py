count=0
temp=0
index=0

# Example usage
a=int(input())
votes=[]
for i in range(a):
    b=input().split()
    votes.append(b)

freq={}
for i in range(len(votes)):
    temp=votes.count(votes[i])
    
    if(temp>count):
        count=temp
        index=i
mf=votes[index]
hf=" ".join(mf)

print(hf)
    
