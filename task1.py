
maxlen=100000
minval=-1
maxval=200000
def solution(A):

    length=len(A)
    passedIndex=set()

    if length == 0 or length > maxlen:
        return 0

    i=A[0]
    passedIndex.add(0)

    if length == 1:
        if i == -1:
            return 1
        else:
            return 0

    while True:

        if i <minval or i >maxval :
            return 0

        #loop exists
        if i in passedIndex:
            return 0

        if i == -1:
            return len(passedIndex)

        #not valid index
        if i >= length  or i < -1:
            return 0

        passedIndex.add(i)
        i = A[i]


def run_test():
    test_suit = (
            [],

            [1],
            [200000],

            [1,1],
            [1,2],
            [2,1],
            [200000,200000],
            [1,-1],
            

            [2,1,2],
            [2,1,3],
            [2,1,-1],

            [1,4,-1,3,2],
            [1,4,5,3,2],

            [200000,4,5,3,2],

            [1,-5,5,3,2],
            [1,2,2000001,3,2],

            )

    for tc in test_suit:
        print "test data:",tc, "solution data:",solution(tc)

if __name__=="__main__":
    run_test()

