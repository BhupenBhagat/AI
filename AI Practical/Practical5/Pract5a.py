capacity=(12,8,5)
x=capacity[0]
y=capacity[1]
z=capacity[2]

memory={}
ans=[]
def get_allstates(state):
    a=state[0]
    b=state[1]
    c=state[2]
    if(a==6 and b==6):
        ans.append(state)
        return True
    if((a,b,c) in memory):
        return False
    memory[(a,b,c)]=1
    if(a>0):
        if(a+b<=y):
            if(get_allstates((0,a+b,c))):
                ans.append(state)
                return True
        else:
            if(get_allstates((a-(y-b),y,c))):
                ans.append(state)
                return True
        if(a+c<=z):
            if(get_allstates((a-(z-c),b,z))):
                ans.append(state)
                return True
        else:
            if(get_allstates((a-(z-c),b,z))):
                ans.append(state)
                return True
    if(b>0):
        if(a+b<=x):
            if(get_allstates((a+b,0,c))):
                ans.append(state)
                return True
        else:
            if(get_allstates((x,b-(x-a),c))):
                ans.append(state)
                return True
        if(b+c<=z):
            if(get_allstates((a,0,b+c))):
                ans.append(state)
                return True
            else:
                if(get_allstates((a,b-(z-c),z))):
                    ans.append(state)
                    return True
                    
    if(c>0):
        if(a+c<=x):
            if(get_allstates((a+c,b,0))):
                ans.append(state)
                return True
        else:
            if(get_allstates(x,b,c-(x-z))):
                ans.append(state)
                return True
        if(b+c<=y):
            if(get_allstates((a,b+c,0))):
                ans.append(state)
                return True
        else:
            if(get_allstates((a,y,c-(y-b)))):
                ans.append(state)
                return True
    return False
    
initial_state=(12,0,0)
print("starting work....\n")
get_allstates(initial_state)
ans.reverse()
for i in ans:
    print(i)    
                
                    