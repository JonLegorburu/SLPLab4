def exercise1(list):

    mean=0
    for x in list:
        mean=mean+x

    if(len(list) > 0):
        mean=mean/len(list)

    return round(mean,2)


def exercise2(list, minThres=0, maxThres=1):
    result=0
    norm=[]
    processed=[]

    lMin,lMax=min(list),max(list)
    for i,value in enumerate(list):
        tmp=(value-lMin)/(lMax-lMin)
        norm.append(tmp)
        if(tmp>=minThres and tmp<=maxThres):
            processed.append(tmp)

    print("Input list",list)
    print("Normalized list",norm)
    print("Thresholds:",minThres,maxThres)
    print("Result output:",processed)
    print("Avg from normalized and filtered values:",exercise1(processed))
    print("\n")
    #print(list)

    result = processed


    return result


def exercise31(*args):
    if len(args) == 0:
        return "N/C"

    mean=0
    tmp=[]
    for i,x in enumerate(args):
        for j, p in enumerate(x):
            mean = mean + p
        mean = mean / len(x)
        #print(mean)
        tmp.append(mean)
        mean=0

    #to calculate the full mean
    for x in tmp:
        mean=mean+x
    mean=mean/len(args)

    print("\n")

    return round(mean,2)

def exercise32(**kwargs):
    mean=0
    tmp=[]
    for key, value in kwargs.items():
        if(len(value)>0):
            for x in value:
                mean = mean + x
            mean = mean / len(value)
            tmp.append(mean)
            mean=0
    for x in tmp:
        mean=mean+x
    mean=mean/len(tmp)

    return round(mean,2)