
maxlen=100000
minval=-1000000000
maxval=1000000000
def solution(A):
    premax= None
    postmax = None
    maxabs = 0
    tmpabs = 0

    maxA=[]
    length=len(A)
    
    #not good list
    if length < 2 or length > maxlen:
        return 0

    #build max val list for #n element
    for i,val in enumerate(A):

        if val <minval or val >maxval:
            return 0

        if premax == None or val > premax:     
            premax = val 

        maxA.append(premax)

    #print maxA

    i=length-1
    for val in A[::-1]:
        if postmax == None or postmax < val:
            postmax = val

        #maxA[i] had the max val before #n 
        #and postmax had max val after #n
        tmpabs = abs(maxA[i]-postmax)
        if tmpabs > maxabs:
            maxabs = tmpabs

        #print i,maxabs,postmax,maxA[i]
        i-=1

    return maxabs

def run_test():
    test_suit = (
            [],

            [1],
            [minval],
            [maxval],
            [minval-1],
            [maxval+1],

            [1,1],
            [1,2],
            [1,2,3],
            [-3,-2,-1,1,2,3],
            [3,2,1,0,-1,-2,-3],

            [3,2,1,5,-1,-2,-3],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],

            [minval,maxval],
            )

    for tc in test_suit:
        print "test data:",tc, "solution data:",solution(tc)

if __name__=="__main__":
    run_test()

