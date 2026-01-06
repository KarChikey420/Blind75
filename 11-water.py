def water_problem(hieghts):
    l=0
    r=len(hieghts)-1
    res=0
    
    while l<r:
        area=(r-l)*min(hieghts[l],hieghts[r])
        res=max(res,area)
        
        if hieghts[l]<hieghts[r]:
            l+=1
        else:
            r-=1
    return res