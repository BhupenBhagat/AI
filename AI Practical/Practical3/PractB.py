import math
increment=0.1
starting_Point=[1,1]
point1=[1,5]
point2=[6,4]
point3=[5,2]
point4=[2,1]

def distance(x1,y1,x2,y2):
    dist=math.pow(x2-x1,2)+math.pow(y2-y1,2)
    return dist

def sum_of_distance(x1,y1,px1,py1,px2,py2,px3,py3,px4,py4):
    d1=distance(x1,y1,px1,py1)
    d2=distance(x1,y1,px2,py2)
    d3=distance(x1,y1,px3,py3)
    d4=distance(x1,y1,px4,py4)
    return d1+d2+d3+d4
def newDistance(x1,y1,point1,point2,point3,point4):
    d1=[x1,y1]
    d1temp=sum_of_distance(x1,y1,point1[0],point1[1],point2[0],point2[1],point3[0],point3[1],point4[0],point4[1])
    d1.append(d1temp)
    return d1
minDistance=sum_of_distance(starting_Point[0],starting_Point[1],point1[0],point1[1],point2[0],point2[1],point3[0],point3[1],point4[0],point4[1])
flag=True

def new_points(minimum,d1,d2,d3,d4):
    if d1[2]==minimum:
        return[d1[0],d1[1]]
    elif d2[2]==minimum:
        return [d2[0],d2[1]]
    elif d3[2]==minimum:
        return d3[2]==minimum
    elif d4[2]==minimum:
        return [d4[0],d4[1]]
    
i=1
while flag:
    d1=newDistance(starting_Point[0] + increment,starting_Point[1],point1,point2,point3,point4)
    d2=newDistance(starting_Point[0] - increment,starting_Point[1],point1,point2,point3,point4)
    d3=newDistance(starting_Point[0],starting_Point[1] + increment,point1,point2,point3,point4)
    d4=newDistance(starting_Point[0],starting_Point[1] - increment,point1,point2,point3,point4)
    print(i,": ",round(starting_Point[0],2),' ',round(starting_Point[1],2))
    minimum=min(d1[2],d2[2],d3[2],d4[2])
    if minimum<minDistance:
        starting_Point=new_points(minimum,d1,d2,d3,d4)
        minDistance=minimum
        i+=1
    else:
        flag=False
    
    