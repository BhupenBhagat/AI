def moveTower(height,fromPole,toPole,withPole):
    if height >=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print("move disk from",fp,"to",tp)
moveTower(3,"a","b","c")