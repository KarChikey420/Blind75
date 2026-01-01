def Two_Sum(arr,target):
    dicti={}
    for i,num in enumerate(arr):
        diff=target-num
        if diff in dicti:
            return [dicti[diff],i]
        dicti[num]=i
    return None

if __name__=="__main__":
    arr=[2,5,7,9]
    target=9
    print(Two_Sum(arr,target))