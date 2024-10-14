def movetower(h,f,to,w):
    if h>=1:
        movetower(h-1,f,w,to)
        movedisc(f,to)
        movetower(h-1,w,to,f)
def movedisc(fp,tp):
    print("moved from ",fp," to ", tp)

movetower(3,'a','b','c')