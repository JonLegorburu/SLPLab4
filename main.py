from funtions import *


def mainProgram():
    #EXERCISE 1
    list=[]
    print("Press any character to stop getting numbers")
    while(True):
        try:
            read = float(input("Please enter number:\n"))
            list.append(read)
        except:
            break

    resutl1=exercise1(list)
    print("Exercise 1 result:")
    print(resutl1,"\n")

    #EXERCISE 2
    exampleList=[2,4,10,6,8,4]
    print("Executing 2.Exercise without min/max Threshld: ")
    result2 = exercise2(exampleList)
    print("Result exercise2:",result2)

    minThres=0.3
    maxThres=1
    print("Executing 2.Exercise WITH min/max Threshld: ")
    result2=exercise2(exampleList,minThres,maxThres)
    print(result2)

    # EXERCISE 3.1
    exampleList311 = [9, 4, 15, 6, 867, 4]
    exampleList312 = [2, 4, 10, 6, 8, 4]
    result31 = exercise31(exampleList311, exampleList312)
    print("Exercise3.1:",result31)

    # EXERCISE3.2
    m1 = [9, 4, 15, 6, 867, 4]
    m2 = [9, 4, 15, 6, 867, 4]
    m3 = [9, 4, 15, 6, 867, 4]

    result32=exercise32(list1=m1, list2=m2, list3=m3)
    print("Exercise3.2:",result32)


mainProgram()
