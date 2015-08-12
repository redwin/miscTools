import math
maxval=1000
def solution(N):
    resList=[1]
    val1 = 0
    if N < -1 or N > 1000:
        return 0 

    for i in range(N):
        i+=1
        if i < 2:
             resList = [1] * (i + 1)
        else:
            resList[1:-1] = [(tmpNum + resList[j]) for j, tmpNum in enumerate(resList[1:])]


        for i,val in enumerate(resList):
            if i < 1:
                continue
            resList[i-1] = resList[i-1] + resList[i]/10 
            resList[i] = resList[i]%10 
        
    #print resList

    for i in resList:
        if i == 1:
            val1+=1

    return val1

def run_test():
    test_suit = range(maxval+1)
    #test_suit = range(15)

    for tc in test_suit:
        print "test data:",tc, "solution data:",solution(tc)
        #print "test data:",math.pow(11,tc), "solution data:",solution(tc)

if __name__=="__main__":
    run_test()

